# Nossaman Professional Directory Scraper 🌐📊

This Python script is designed to scrape professional data from the `nossaman.com` website. It extracts key information like names, titles, services, contact details, and office locations from individual professional profiles, then compiles everything into a clean Excel spreadsheet.

-----

## Features ✨

  * **Targeted Scraping**: Specifically extracts data from `nossaman.com`'s professionals directory.
  * **Detailed Information Extraction**: Gathers:
      * **Name**
      * **Title**
      * **Service (Practices)**
      * **Office Location**
      * **Email**
      * **Phone Number**
      * **Fax Number (labeled as 'Tax' in the output)**
      * **Mobile Number**
  * **Excel Output**: Organizes all scraped data into an easy-to-use Excel file (`.xlsx`).
  * **Error Handling**: Includes basic checks to ensure data is present before attempting to extract.
  * **Sequential Indexing**: Adds a serial number (`S.No`) to each entry for easy tracking.

-----

## Prerequisites 🛠️

Before you run this script, make sure you have the following installed:

  * **Python 3.x**: Download from [python.org](https://www.python.org/downloads/).
  * **Required Python Libraries**: These will be installed via `pip`.

-----

## Installation 💻

1.  **Clone the repository** (or download the `main.py` file directly):
    ```bash
    git clone https://github.com/MemonDeveloper/Data-Scraping/new/main/Nossaman-LLP.git
    cd Nossaman-LLP
    ```
2.  **Create a `requirements.txt` file**: In the root directory of your project, create a file named `requirements.txt` and paste the following content:
    ```
    requests
    beautifulsoup4
    pandas
    openpyxl # Pandas uses this to write .xlsx files
    ```
3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

-----

## Usage ▶️

1.  **Run the script**:
    ```bash
    python main.py
    ```

The script will automatically:

  * Navigate to the professionals directory page.
  * Collect all individual professional profile links.
  * Visit each profile link to extract the detailed information.
  * Compile all extracted data into a pandas DataFrame.
  * Save the DataFrame to an Excel file named `professionals_data.xlsx` in the same directory where you run the script.

-----

## Output Excel Format 📊

The generated Excel file (`professionals_data.xlsx`) will have the following columns in this specific order:

  * **S.No**: A serial number for each professional.
  * **Name**: The full name of the professional.
  * **Title**: Their professional title.
  * **Service**: A comma-separated list of their practice areas/services.
  * **Office**: Their primary office location.
  * **Email**: Their email address.
  * **Phone**: Their direct phone number.
  * **Tax**: Their fax number (labeled as 'Tax' as per the script's original naming).
  * **Mobile**: Their mobile phone number, if available.

-----

## Important Notes ⚠️

  * **Website Structure**: This script is tailored to the specific HTML structure of `nossaman.com` as observed at the time of creation. If the website's layout changes, the selectors (e.g., `'h1', {'id': 'pageTitle'}`) in the `extract_data_from_profile` function may need to be updated.
  * **Rate Limiting/Blocking**: Repeated or excessively fast requests to a website can lead to your IP being temporarily or permanently blocked. This script does not include advanced rate-limiting or proxy rotation. For large-scale scraping, consider adding delays between requests or using proxies.
  * **`Mobile` and `Tax` Extraction**: The extraction logic for 'Mobile' and 'Tax' (Fax) relies on specific text patterns or HTML attributes. If these patterns vary on the website, you might need to adjust the extraction logic.

-----

## Contributing 🤝

Feel free to fork this repository, open issues, and submit pull requests if you have suggestions for improvements or bug fixes.

-----
