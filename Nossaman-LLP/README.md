# Nossaman Professional Directory Scraper

A Python script that extracts lawyer/professional data from `nossaman.com` and saves it to Excel.

## What it does
- Scrapes comprehensive professional data including personal details, contact information, and career information
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

| Column | Description |
|--------|-------------|
| Name | Full name |
| Given Name | First name |
| Middle Name | Middle name |
| Family Name | Last name |
| Title | Professional title |
| Office | Office location |
| Email | Email address |
| Phone | Phone number |
| Mobile | Mobile number |
| Fax | Fax number |
| LinkedIn | LinkedIn profile URL |
| Image | Profile image URL |
| Practice | Practice areas |
| Industry | Industries served |
| Education | Educational background |
| Admission | Bar admissions |
| Overview | Biography overview |
| Experience | Professional experience |
| Other Experience | Additional experience |
| Publications | Publications |
| Events | Events participated |
| News | News mentions |
| Podcasts | Podcast appearances |
| Honors | Awards and honors |

## Notes
- Script is built for the current structure of `nossaman.com` - may break if the website changes
- Add delays if scraping many pages to avoid being blocked

---

## Support My Work
If you find this script useful and would like to support its development, any contribution is greatly appreciated! Your support helps in maintaining and improving this tool.
Here are a few ways you can contribute financially:

- **Patreon**: [Link to your Patreon page]
- **Buy Me a Coffee**: [Link to your Buy Me a Coffee page]
- **PayPal**: [Link to your PayPal.Me or direct PayPal donation link]

Thank you for your support!

---

This version is shorter, removes technical details, and focuses on what the user actually needs to know.
