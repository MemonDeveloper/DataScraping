# IECA Consultant Directory Scraper

A Python script that extracts independent educational consultant data from iecaonline.com and saves it to CSV.

## What it does

- Scrapes comprehensive consultant data including personal details, expertise areas, education, and contact information
- Outputs data to a CSV file (`ieca_consultants.csv`)
- Optionally downloads profile images to a local folder

## How to use

### Install requirements

```bash
pip install requests beautifulsoup4
```

### Run the script

```bash
python main.py
```

## Output columns

| Column | Description |
|--------|-------------|
| Name | Consultant's full name |
| Tagline | Professional title/tagline |
| Bio | Biography description |
| Image_URL | Profile image URL |
| Profile_URL | Link to consultant's profile page |
| Website | Personal/company website |
| Location | City, state, zip code, country |
| Areas_of_Consulting_Expertise | Main consulting expertise areas |
| Additional_Advising_Areas | Secondary advising specialties |
| Additional_Languages_Spoken | Languages offered besides English |
| Education | Educational background and degrees |

> **Note:** Additional dynamic columns may appear based on bold-labeled fields found in each profile.

## Output Files

| File | Description |
|------|-------------|
| `ieca_consultants.csv` | All scraped consultant data |
| `consultant_images/` | Folder containing downloaded profile images |

## Configuration Options

You can adjust these delays in the script:

```python
DELAY_BETWEEN_PAGES       = 1.5   # Seconds between listing pages
DELAY_BETWEEN_CONSULTANTS = 1.0   # Seconds between profile pages
DELAY_BETWEEN_IMAGES      = 0.3   # Seconds between image downloads
```

## Notes

- Script is built for the current structure of `iecaonline.com` - may break if the website changes
- Add longer delays if scraping many pages to avoid being blocked
- Respect the website's `robots.txt` and terms of service

## Support My Work

If you find this script useful and would like to support its development, any contribution is greatly appreciated! Your support helps in maintaining and improving this tool. Here are a few ways you can contribute financially:

### Support via Crypto (USDT Only)

You can support me using USDT on the following networks:

| Network | Address |
|---------|---------|
| USDT (TRC20) | `THqVrt9E7B9fRd8GZvAXuqBTtUkZSCuNNU` |
| USDT (ERC20/BNB) | `0xfe7f29b963566a982bbea34ae7fd79ba7336d4c1` |

⚠️ **Please make sure to send using the correct network.** Sending funds on the wrong network may result in loss of funds.

Thank you for your support!
