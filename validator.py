import json
import requests
import logging
from datetime import datetime
from prettytable import PrettyTable

# Logging
logging.basicConfig(filename="validator.log", level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Map common banks to estimated ZIP
BANK_ZIP_MAP = {
    "JPMorgan Chase": "10001",
    "Bank of America": "28202",
    "Wells Fargo": "94104",
    "Citi": "10013",
    "Capital One": "22314",
    "American Express": "10285",
    "Discover": "60015",
    "US Bank": "55107",
    "PNC Bank": "15222",
    "TD Bank": "07030",
    "BB&T": "27601",
    "SunTrust": "30303",
    "Barclays": "10019",
    "HSBC": "10018",
    "Synchrony": "75038",
    "Fifth Third Bank": "45263",
    "KeyBank": "44114",
    "Regions": "35203",
    "Ally Bank": "48116",
    "Chime": "94103"
}

def luhn_check(card_number):
    digits = [int(d) for d in str(card_number)]
    for i in range(len(digits)-2, -1, -2):
        doubled = digits[i] * 2
        digits[i] = doubled - 9 if doubled > 9 else doubled
    return sum(digits) % 10 == 0

def get_bin_info(card_number):
    bin_prefix = str(card_number)[:6]
    try:
        res = requests.get(f"https://lookup.binlist.net/{bin_prefix}", timeout=5)
        if res.status_code == 200:
            return res.json()
        else:
            logging.warning(f"BIN lookup failed for {bin_prefix}: {res.status_code}")
            return {}
    except Exception as e:
        logging.error(f"BIN lookup error for {bin_prefix}: {e}")
        return {}

def validate_expiry(expiry):
    try:
        exp_date = datetime.strptime(expiry, "%m/%y")
        return exp_date > datetime.now()
    except Exception as e:
        logging.error(f"Expiry date parse failed: {expiry} - {e}")
        return False

def validate_card(card):
    number = str(card["number"]).replace(" ", "").replace("-", "")
    cvv = str(card["cvv"])
    expiry = card["expiry"]

    if not number.isdigit() or len(number) < 13:
        return False, "Invalid card number format"

    if not luhn_check(number):
        return False, "Luhn check failed"

    if len(cvv) not in [3, 4] or not cvv.isdigit():
        return False, "Invalid CVV"

    if not validate_expiry(expiry):
        return False, "Card expired"

    return True, "Valid"

def estimate_zip(bank_name):
    return BANK_ZIP_MAP.get(bank_name, "Unknown")

def main():
    # Load cards
    with open("cards.json") as f:
        cards = json.load(f)

    print(f"🔍 Loaded {len(cards)} card(s). Starting validation...\n")

    table = PrettyTable()
    table.field_names = ["#", "Name", "Card", "Brand", "Bank", "ZIP", "Expiry", "CVV", "Status"]

    valid_cards = []

    for idx, card in enumerate(cards, 1):
        number = card.get("number", "N/A")
        name = card.get("name", "N/A")
        expiry = card.get("expiry", "N/A")
        cvv = card.get("cvv", "N/A")

        valid, reason = validate_card(card)
        bin_info = get_bin_info(number)

        brand = bin_info.get("scheme", "-")
        bank = bin_info.get("bank", {}).get("name", "-")
        zip_code = estimate_zip(bank)

        status = "VALID ✅" if valid else "INVALID ❌"
        if valid:
            valid_cards.append({
                "name": name,
                "number": number,
                "expiry": expiry,
                "cvv": cvv,
                "brand": brand,
                "bank": bank,
                "zip_code": zip_code
            })
        else:
            logging.info(f"{number} - {reason}")

        table.add_row([idx, name, number, brand, bank, zip_code, expiry, cvv, status])

    print(table)

    # Save valid cards
    if valid_cards:
        with open("valid_cards.json", "w") as f:
            json.dump(valid_cards, f, indent=2)
        print(f"\n✅ {len(valid_cards)} valid card(s) saved to 'valid_cards.json'")
    else:
        print("\n⚠ No valid cards found.")

    print("📁 Full log written to 'validator.log'.")

if __name__ == "__main__":
    main()
