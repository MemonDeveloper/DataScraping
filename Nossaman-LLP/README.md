# Nossaman Professional Directory Scraper

A Python script that extracts lawyer/professional data from `nossaman.com` and saves it to Excel.

## What it does
- Scrapes names, titles, practice areas, office locations, emails, phone numbers, fax, and mobile numbers
- Outputs data to an Excel file (`professionals_data.xlsx`)

## How to use

1. **Install requirements**
```bash
pip install requests beautifulsoup4 pandas openpyxl
```

2. **Run the script**
```bash
python main.py
```

## Output columns
- S.No | Name | Title | Service | Office | Email | Phone | Tax | Mobile

## Notes
- Script is built for the current structure of `nossaman.com` - may break if the website changes
- Add delays if scraping many pages to avoid being blocked

---

This version is shorter, removes technical details, and focuses on what the user actually needs to know.
