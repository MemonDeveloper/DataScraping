# Bahsegel1200 Account Scraper

A Python automation tool with GUI (Tkinter) that logs into Bahsegel1200 accounts, extracts user profile details and balances, and saves the results into an Excel file.

---

## What it does

* Automates login for multiple accounts from Excel file
* Extracts user profile data including:

  * Username
  * First name & last name
  * Address, city, country
  * Email & phone number
  * Birth date & postal code
* Extracts account balances:

  * Total balance
  * Bonus balance
  * Real balance
  * Token balance
* Saves all data into a structured Excel file
* Creates backup of input file automatically
* Shows live progress in GUI (Tkinter)

---

## How to use

### 1. Install requirements

```bash
pip install pandas openpyxl selenium undetected-chromedriver requests beautifulsoup4
```

---

### 2. Prepare Excel file

File name:

```bash
bahsegel1200.xlsx
```

Sheet name:

```bash
bahsegel1200 List
```

Format:

| Column A | Column B |
| -------- | -------- |
| Account  | Password |

---

### 3. Run script

```bash
python main.py
```

Then click:

👉 **bahsegel1200 button** in GUI

---

## Output

A new Excel file will be generated:

```bash
bahsegel1200 - Result YYYY-MM-DD HH-MM-SS.xlsx
```

---

## Output columns

| Column       | Description      |
| ------------ | ---------------- |
| username     | Account username |
| firstname    | First name       |
| lastname     | Last name        |
| address      | Full address     |
| postalcode   | Postal code      |
| brithdate    | Date of birth    |
| city         | City             |
| country      | Country          |
| email        | Email address    |
| mobile_phone | Phone number     |
| totalbalance | Total balance    |
| bonusbalance | Bonus balance    |
| realbalance  | Real balance     |
| tokenbalance | Token balance    |

---

## ⚠️ Notes

* Requires Google Chrome installed
* Uses undetected-chromedriver for automation
* Website structure changes may break the script
* Use responsibly and only on authorized accounts

---

## Support My Work

If you find this project useful and would like to support its development, any contribution is appreciated.

You can support via cryptocurrency:

* **USDT (TRC20):** THqVrt9E7B9fRd8GZvAXuqBTtUkZSCuNNU
* **USDT (ERC20/BNB):** 0xfe7f29b963566a982bbea34ae7fd79ba7336d4c1

⚠️ Please ensure you send using the correct network. Sending on the wrong network may result in loss of funds.

Thank you for your support!

---
