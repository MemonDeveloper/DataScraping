# OCX InfoSync Engine (Patent Scraper)

A Python script that extracts patent data from `ppubs.uspto.gov`, generates structured reports, and saves them as DOCX and PDF files.

## What it does

* Fetches patent data using multiple search queries
* Extracts detailed patent information (title, abstract, claims, etc.)
* Cleans and formats complex HTML content
* Generates structured reports in DOCX format
* Converts DOCX files to PDF
* Creates short AI summaries using Google Gemini
* Uploads final files to Google Drive

## How to use

1. **Install requirements**

```bash
pip install requests beautifulsoup4 python-docx docx2pdf google-generativeai google-api-python-client google-auth
```

2. **Setup**

* Add your Gemini API key in the script
* Add your `service_account.json` file for Google Drive

3. **Run the script**

```bash
python main.py
```

## Output

Files are saved in:

```
OCX_InfoSyncEngine/
```

### Generated files:

* `.docx` → Full patent report
* `.pdf` → Converted version

## Report includes

* Patent Number
* Title
* Abstract
* Claims
* Description
* Metadata
* AI-generated summary

## Notes

* Script depends on current structure of `ppubs.uspto.gov` and may break if it changes
* Headers/cookies may expire over time
* Add delays if running large batches to avoid blocking
* PDF conversion requires Microsoft Word

---

## Support My Work

If you find this script useful and would like to support its development, any contribution is greatly appreciated! Your support helps in maintaining and improving this tool.

Support via Crypto (USDT Only):
You can support me using USDT on the following networks:

* **USDT (TRC20)**: THqVrt9E7B9fRd8GZvAXuqBTtUkZSCuNNU
* **USDT (ERC20/BNB)**: 0xfe7f29b963566a982bbea34ae7fd79ba7336d4c1

⚠️ Please make sure to send using the correct network. Sending funds on the wrong network may result in loss of funds.

Thank you for your support!
