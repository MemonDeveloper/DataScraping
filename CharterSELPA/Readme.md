# IEE Assessor Scraper (AI Enriched)

A Python script that scrapes Independent Educational Evaluation (IEE) assessor data from `charterselpa.org` and enriches it using AI before saving to CSV.

## What it does
* Scrapes assessor lists from the website
* Extracts assessor names and profile links from tables
* Visits each assessor profile page
* Extracts structured data from HTML content
* Uses OpenAI GPT to convert HTML into structured JSON
* Performs a second AI pass to fill missing fields
* Uses caching to avoid duplicate API calls
* Saves final structured data into a CSV file

## How to use

1. **Install requirements**

```bash
pip install requests beautifulsoup4 openai
```

2. **Setup**

* Add your OpenAI API key in the script

```python
client = OpenAI(api_key="YOUR_API_KEY")
```

3. **Run the script**

```bash
python main.py
```

## Output

File is saved as:

```
assessor_list.csv
```

## CSV includes

* Company Name
* Areas of Assessment
* In-Person/Virtual Assessment
* Region
* Age Groups Supported
* First Name
* Last Name
* Phone
* Email
* Website
* LinkedIn
* Address
* City
* State
* Zip Code
* Social Media
* Notes
* Profile Link
* Assessor List

## Notes

* Script depends on current structure of `charterselpa.org` and may break if it changes
* OpenAI API usage costs may apply
* Add delays to avoid rate limiting
* Some profiles may have missing or inconsistent data

---

## Support My Work

If you find this script useful and would like to support its development, any contribution is greatly appreciated. Your support helps in maintaining and improving this tool.

Support via Crypto (USDT Only):

* **USDT (TRC20)**: THqVrt9E7B9fRd8GZvAXuqBTtUkZSCuNNU
* **USDT (ERC20/BNB)**: 0xfe7f29b963566a982bbea34ae7fd79ba7336d4c1

⚠️ Please make sure to send using the correct network. Sending funds on the wrong network may result in loss of funds.

Thank you for your support!

---
