import re
import datetime
import requests
import json
import logging
from prettytable import PrettyTable
from time import sleep

# === Logging Setup ===
logging.basicConfig(filename='validator.log', level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] %(message)s')

BIN_LOOKUP_URL = "https://lookup.binlist.net/"

def luhn_check(card_number):
    card_number = ''.join(filter(str.isdigit, card_number))
    total = 0
    reverse_digits = card_number[::-1]
    for i, digit in enumerate(map(int, reverse_digits)):
        if i % 2 == 1:
            doubled = digit * 2
            total += doubled - 9 if doubled > 9 else doubled
        else:
            total += digit
    return total % 10 == 0

def get_bin_info(bin_number):
    try:
        resp = requests.get(BIN_LOOKUP_URL + bin_number, headers={"Accept-Version": "3"})
        if resp.status_code == 200:
            return resp.json()
    except Exception as e:
        logging.error(f"BIN lookup failed for {bin_number}: {e}")
    return {}

def validate_expiry(expiry):
    try:
        month, year = expiry.split('/')
        month = int(month)
        year = int(year)
        if year < 100:
            year += 2000
        now = datetime.datetime.now()
        exp_date = datetime.datetime(year, month, 1)
        return exp_date > now
    except:
        return False

def detect_card_type(number):
    number = ''.join(filter(str.isdigit, number))
    if number.startswith('4'):
        return 'Visa'
    elif number.startswith(('51', '52', '53', '54', '55')):
        return 'MasterCard'
    elif number.startswith(('34', '37')):
        return 'American Express'
    elif number.startswith('6011') or number.startswith('65'):
        return 'Discover'
    elif number.startswith('35'):
        return 'JCB'
    elif number.startswith('62'):
        return 'UnionPay'
    else:
        return 'Unknown'

def validate_card_entry(entry):
    number = entry["number"].replace(' ', '').replace('-', '')
    expiry = entry.get("expiry", "")
    cvv = entry.get("cvv", "")
    name = entry.get("name", "N/A")

    bin_info = get_bin_info(number[:6])
    card_type = detect_card_type(number)
    luhn = luhn_check(number)
    length_valid = len(number) in [13, 15, 16, 19]
    expiry_valid = validate_expiry(expiry)
    cvv_valid = len(cvv) in [3, 4]

    is_valid = all([luhn, length_valid, expiry_valid, cvv_valid])

    result = {
        "name": name,
        "number": number,
        "type": card_type,
        "brand": bin_info.get("scheme", "N/A"),
        "country": bin_info.get("country", {}).get("name", "N/A"),
        "bank": bin_info.get("bank", {}).get("name", "N/A"),
        "luhn": luhn,
        "length": length_valid,
        "expiry": expiry_valid,
        "cvv": cvv_valid,
        "status": "VALID ✅" if is_valid else "INVALID ❌"
    }

    log_msg = f"{name} | {number} | {result['status']} | Brand: {result['brand']} | Bank: {result['bank']}"
    logging.info(log_msg)

    return result

def run_bulk_validation_from_json(file_path):
    with open(file_path, 'r') as f:
        card_data = json.load(f)

    total = len(card_data)
    print(f"\n🧾 Loaded {total} card(s) from file.")
    print("🔍 Starting validation...\n")

    sleep(1)
    table = PrettyTable()
    table.field_names = ["#", "Name", "Card", "Type", "Brand", "Country", "Bank", "Luhn", "Length", "Expiry", "CVV", "Status"]

    valid_cards = []

    for idx, entry in enumerate(card_data, start=1):
        result = validate_card_entry(entry)
        table.add_row([
            idx,
            result['name'],
            result['number'],
            result['type'],
            result['brand'],
            result['country'],
            result['bank'],
            "✔" if result['luhn'] else "✘",
            "✔" if result['length'] else "✘",
            "✔" if result['expiry'] else "✘",
            "✔" if result['cvv'] else "✘",
            result['status']
        ])
        if result['status'] == "VALID ✅":
            valid_cards.append(result)
        sleep(0.3)  # Light throttle

    print(table)

    if valid_cards:
        with open("valid_cards.json", "w") as vf:
            json.dump(valid_cards, vf, indent=2)
        print(f"\n✅ {len(valid_cards)} valid card(s) saved to 'valid_cards.json'.")
    else:
        print("\n⚠️ No valid cards found.")

    print("📁 Full log written to 'validator.log'.")

if __name__ == "__main__":
    path = input("📂 Enter path to JSON card file: ").strip()
    run_bulk_validation_from_json(path)
