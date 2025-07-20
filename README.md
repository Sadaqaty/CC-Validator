# 💳 CC Validator

**CC Validator** is a Python-based tool for bulk validation and enrichment of credit card data using BIN lookup, card structure validation, and data enrichment like ZIP code approximation. This project is intended strictly for **educational**, **testing**, or **internal store validation** purposes.

---

## ⚠️ Legal Disclaimer

> ❗ This tool does **NOT** and **must NOT** be used to validate stolen or unauthorized card data.  
> It is intended for validating **test cards**, verifying card structure, and enriching legitimate store card inputs.  
> Misuse of this tool can lead to violation of laws, terms of service of payment providers (like Stripe), and account bans.  
> Use responsibly and legally.

---

## 🚀 Features

- ✅ Bulk card validation from a JSON file.
- 🔍 BIN lookup using [Binlist API](https://lookup.binlist.net/) (no API key required).
- 🏦 Card enrichment with issuing bank, brand, and approximate ZIP code.
- 📋 Logging to file with timestamps.
- 📄 Outputs valid cards to a separate file with all details.
- 📊 Clean CLI output in a structured table.

---

## 📂 Input Format

Your `cards.json` file should be a JSON array of objects like:

```json
[
  {
    "type": "Visa",
    "name": "James Morris",
    "number": "4840416577300061",
    "cvv": "015",
    "expiry": "07/29"
  },
  {
    "type": "Visa",
    "name": "Brandon Edwards",
    "number": "4437628416964736",
    "cvv": "623",
    "expiry": "07/27"
  }
]
```
## 📦 Output

- `validator.log` – contains full logs of each validation with metadata.  
- `valid_cards.json` – contains only successfully validated cards with enriched info.  
- **CLI output table** – shows summary of each card’s status.

└─$ python3 ccv2.py
```
🔍 Loaded 80 card(s). Starting validation...

+----+--------------------+------------------+-------+------+-----+--------+------+------------+
| #  |        Name        |       Card       | Brand | Bank | ZIP | Expiry | CVV  |   Status   |
+----+--------------------+------------------+-------+------+-----+--------+------+------------+
| 1  |    James Morris    | ************0061 |   -   |  -   |  -  | 07/29  | 015  | INVALID ❌ |
| 2  |  Brandon Edwards   | ************4736 |   -   |  -   |  -  | 07/27  | 623  | INVALID ❌ |
| 3  |   Madison Perez    | ************9781 |   -   |  -   |  -  | 07/29  | 708  |  VALID ✅  |
| 4  |    Mason Watson    | ************0900 |   -   |  -   |  -  | 07/29  | 783  | INVALID ❌ |
| 5  |   Sophia Martin    | ************7908 |   -   |  -   |  -  | 07/26  | 335  | INVALID ❌ |
| 6  |   Zoey Peterson    | ************9157 |   -   |  -   |  -  | 07/27  | 501  | INVALID ❌ |
| 7  |    Tyler Torres    | ************2788 |   -   |  -   |  -  | 07/28  | 316  | INVALID ❌ |
| 8  |     Leah Clark     | ************0026 |   -   |  -   |  -  | 07/30  | 606  | INVALID ❌ |
| 9  |     Lucas Diaz     | ************8662 |   -   |  -   |  -  | 07/29  | 542  | INVALID ❌ |
| 10 |    Dylan Gomez     | ************4608 |   -   |  -   |  -  | 07/28  | 947  | INVALID ❌ |
| 11 |      Nora Cox      | ************9747 |   -   |  -   |  -  | 07/26  | 365  | INVALID ❌ |
| 12 |   Michael Lopez    | ************4281 |   -   |  -   |  -  | 07/26  | 370  | INVALID ❌ |
| 13 |   Jonathan Allen   | ************2380 |   -   |  -   |  -  | 07/27  | 309  |  VALID ✅  |
| 14 |    Robert Perez    | ************4882 |   -   |  -   |  -  | 07/27  | 939  | INVALID ❌ |
| 15 |    Evelyn Scott    | ************7441 |   -   |  -   |  -  | 07/27  | 552  |  VALID ✅  |
| 16 |  William Martinez  | ************1608 |   -   |  -   |  -  | 07/27  | 519  | INVALID ❌ |
| 17 | Madison Richardson | ************8503 |   -   |  -   |  -  | 07/30  | 968  | INVALID ❌ |
| 18 |  Isabella Parker   | ************2916 |   -   |  -   |  -  | 07/30  | 434  | INVALID ❌ |
| 19 |   Chloe Robinson   | ************0373 |   -   |  -   |  -  | 07/27  | 360  | INVALID ❌ |
| 20 |    Sophia Moore    | ************5266 |   -   |  -   |  -  | 07/27  | 782  | INVALID ❌ |
| 21 |   Andrew Bailey    | ************7700 |   -   |  -   |  -  | 07/27  | 2045 | INVALID ❌ |
| 22 |    Camila Hill     | ************1467 |   -   |  -   |  -  | 07/30  | 7004 |  VALID ✅  |
| 23 |  Anthony Thompson  | ************1940 |   -   |  -   |  -  | 07/26  | 6364 | INVALID ❌ |
| 24 |    Evelyn Ward     | ************6128 |   -   |  -   |  -  | 07/29  | 3250 | INVALID ❌ |
| 25 |     James Bell     | ************4522 |   -   |  -   |  -  | 07/26  | 6872 | INVALID ❌ |
| 26 |   Tyler Campbell   | ************0824 |   -   |  -   |  -  | 07/28  | 3893 | INVALID ❌ |
| 27 |     Ellie Wood     | ************9969 |   -   |  -   |  -  | 07/29  | 3459 | INVALID ❌ |
| 28 |   Tyler Sanchez    | ************4414 |   -   |  -   |  -  | 07/27  | 3066 |  VALID ✅  |
| 29 |   Nathan Howard    | ************3592 |   -   |  -   |  -  | 07/29  | 8910 | INVALID ❌ |
| 30 |    Nathan Young    | ************1038 |   -   |  -   |  -  | 07/26  | 0451 | INVALID ❌ |
| 31 |    Sophia Young    | ************8186 |   -   |  -   |  -  | 07/30  | 0542 |  VALID ✅  |
| 32 |   Michael Jones    | ************5536 |   -   |  -   |  -  | 07/30  | 4898 | INVALID ❌ |
| 33 |  Charlotte Morris  | ************8340 |   -   |  -   |  -  | 07/29  | 9915 | INVALID ❌ |
| 34 |   Avery Edwards    | ************9778 |   -   |  -   |  -  | 07/26  | 8922 | INVALID ❌ |
| 35 |   Stella Morgan    | ************2013 |   -   |  -   |  -  | 07/30  | 7372 | INVALID ❌ |
| 36 |     Leah White     | ************1157 |   -   |  -   |  -  | 07/26  | 7963 | INVALID ❌ |
| 37 |   Hannah Watson    | ************8000 |   -   |  -   |  -  | 07/28  | 9467 | INVALID ❌ |
| 38 |    Layla Adams     | ************1367 |   -   |  -   |  -  | 07/27  | 6892 | INVALID ❌ |
| 39 |  Gabriel Campbell  | ************2787 |   -   |  -   |  -  | 07/28  | 7120 | INVALID ❌ |
| 40 |     Sarah Lee      | ************6837 |   -   |  -   |  -  | 07/26  | 6231 | INVALID ❌ |
| 41 |   David Mitchell   | ************7160 |   -   |  -   |  -  | 07/26  | 558  | INVALID ❌ |
| 42 |    Zoey Nguyen     | ************4833 |   -   |  -   |  -  | 07/27  | 896  | INVALID ❌ |
| 43 |    Harper King     | ************2263 |   -   |  -   |  -  | 07/28  | 817  | INVALID ❌ |
| 44 |    Sophia Adams    | ************3310 |   -   |  -   |  -  | 07/29  | 016  | INVALID ❌ |
| 45 |     Jack Young     | ************0269 |   -   |  -   |  -  | 07/27  | 664  | INVALID ❌ |
| 46 |    Emma Bailey     | ************4355 |   -   |  -   |  -  | 07/26  | 964  | INVALID ❌ |
| 47 |   Chloe Campbell   | ************4047 |   -   |  -   |  -  | 07/30  | 862  | INVALID ❌ |
| 48 |   Abigail Walker   | ************0284 |   -   |  -   |  -  | 07/27  | 212  |  VALID ✅  |
| 49 |   Chloe Roberts    | ************6703 |   -   |  -   |  -  | 07/30  | 362  | INVALID ❌ |
| 50 |   Robert Nguyen    | ************4374 |   -   |  -   |  -  | 07/28  | 584  | INVALID ❌ |
| 51 |   Charlotte Bell   | ************3641 |   -   |  -   |  -  | 07/26  | 120  | INVALID ❌ |
| 52 |     Nora Davis     | ************8812 |   -   |  -   |  -  | 07/26  | 954  | INVALID ❌ |
| 53 |    Riley Miller    | ************9565 |   -   |  -   |  -  | 07/29  | 064  | INVALID ❌ |
| 54 |  Charlotte Harris  | ************9439 |   -   |  -   |  -  | 07/29  | 860  | INVALID ❌ |
| 55 |  Charlotte Wilson  | ************2401 |   -   |  -   |  -  | 07/30  | 500  | INVALID ❌ |
| 56 |    Nathan Green    | ************4866 |   -   |  -   |  -  | 07/29  | 613  | INVALID ❌ |
| 57 |  Joseph Peterson   | ************1779 |   -   |  -   |  -  | 07/26  | 100  | INVALID ❌ |
| 58 |   Gabriel Morgan   | ************3726 |   -   |  -   |  -  | 07/27  | 020  | INVALID ❌ |
| 59 |     Tyler Bell     | ************8824 |   -   |  -   |  -  | 07/30  | 025  |  VALID ✅  |
| 60 |   Gabriel Perez    | ************5328 |   -   |  -   |  -  | 07/28  | 850  | INVALID ❌ |
| 61 |  Joseph Rodriguez  | ************1669 |   -   |  -   |  -  | 07/26  | 190  | INVALID ❌ |
| 62 |    Avery Moore     | ************7876 |   -   |  -   |  -  | 07/26  | 059  | INVALID ❌ |
| 63 |     Riley Hall     | ************9231 |   -   |  -   |  -  | 07/29  | 053  | INVALID ❌ |
| 64 |   Jackson Howard   | ************3711 |   -   |  -   |  -  | 07/26  | 395  | INVALID ❌ |
| 65 |   Emily Ramirez    | ************9499 |   -   |  -   |  -  | 07/28  | 489  | INVALID ❌ |
| 66 |    Caleb Smith     | ************6300 |   -   |  -   |  -  | 07/30  | 818  | INVALID ❌ |
| 67 |    Robert Lewis    | ************4123 |   -   |  -   |  -  | 07/30  | 604  | INVALID ❌ |
| 68 |   Abigail Clark    | ************4722 |   -   |  -   |  -  | 07/26  | 186  | INVALID ❌ |
| 69 |   Nathan Wilson    | ************6179 |   -   |  -   |  -  | 07/26  | 902  | INVALID ❌ |
| 70 |  Benjamin Watson   | ************2535 |   -   |  -   |  -  | 07/26  | 896  | INVALID ❌ |
| 71 |   Michael Murphy   | ************1131 |   -   |  -   |  -  | 07/30  | 546  | INVALID ❌ |
| 72 |  Elijah Campbell   | ************8994 |   -   |  -   |  -  | 07/27  | 285  | INVALID ❌ |
| 73 |    Sofia Rivera    | ************5354 |   -   |  -   |  -  | 07/29  | 772  | INVALID ❌ |
| 74 |   Zoey Martinez    | ************5162 |   -   |  -   |  -  | 07/28  | 909  | INVALID ❌ |
| 75 |     Leah Diaz      | ************1000 |   -   |  -   |  -  | 07/30  | 917  |  VALID ✅  |
| 76 |     Amelia Lee     | ************1102 |   -   |  -   |  -  | 07/29  | 222  | INVALID ❌ |
| 77 |   Paisley Jones    | ************9805 |   -   |  -   |  -  | 07/30  | 269  | INVALID ❌ |
| 78 |   Abigail Nelson   | ************0555 |   -   |  -   |  -  | 07/26  | 999  | INVALID ❌ |
| 79 |    Aubrey Wood     | ************6335 |   -   |  -   |  -  | 07/28  | 338  | INVALID ❌ |
| 80 |     Aria Young     | ************7780 |   -   |  -   |  -  | 07/29  | 250  |  VALID ✅  |
+----+--------------------+------------------+-------+------+-----+--------+------+------------+
```

## 🛠️ Requirements

- Python 3.7+
- `requests`
- `prettytable`
- `colorama`

**Install dependencies:**

```bash
pip install -r requirements.txt
```
## ▶️ Usage

1. Place your `cards.json` file in the project directory.
2. Run the script:

```bash
python3 validator.py
```


---

## 🔐 ZIP Code Mapping

The script uses an internal ZIP code approximation system based on the issuing bank’s name.  
To customize this behavior, you can update or expand the `BANK_ZIP_MAP` dictionary inside the script with more banks and ZIPs.

---

## 🧠 How It Works

- 📥 **Reads cards** from a structured JSON input.
- ✅ **Validates numbers** using the Luhn algorithm.
- 🌐 **Performs BIN lookup** via [https://lookup.binlist.net/](https://lookup.binlist.net/).
- 📍 **Approximates ZIP** code from issuing bank name.
- 💾 **Stores all valid cards** with enriched metadata in `valid_cards.json`.

---

## 🤝 Contributions

Contributions are warmly welcome!  
If you’ve got a better enrichment strategy, support for more APIs (e.g., Stripe for actual store validations), or UI/UX ideas — feel free to **fork**, **commit**, and **pull request**!
