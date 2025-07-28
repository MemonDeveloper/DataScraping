# Charter SELPA Assessor Scraper with AI Enrichment 🤖🔍

This Python script scrapes educational assessor information from the Charter SELPA IEE Assessor List website. It uses a two-phase AI enrichment process with OpenAI's GPT-4 to intelligently extract detailed data from profile pages and find missing information from the web, compiling it all into a single CSV file.

## Features ✨

  * **Targeted Scraping**: Specifically scrapes data from the assessor tables on `charterselpa.org`.
  * **Two-Phase AI Enrichment**:
    1.  **HTML Extraction**: Sends the raw HTML of an assessor's profile to GPT-4 for initial data extraction.
    2.  **Web Research**: If the initial pass misses key details, it uses the company name to ask GPT-4 to search the web and fill in the blanks.
  * **Detailed Information Extraction**: Gathers a wide range of fields, including: `Company Name`, `Contact Person`, `Areas of Assessment`, `Contact Details (Phone, Email, Website)`, `Location (State, County, Address)`, `Social Media`, and more.
  * **Efficient Caching**: Caches company data to avoid redundant scraping and API calls if the same assessor appears in multiple lists, saving time and money.
  * **Robust Data Handling**: Includes a safe JSON parser to handle potential formatting issues in the AI's response.
  * **CSV Output**: Organizes all scraped and enriched data into a clean `assessor_list.csv` file.

## Prerequisites 🛠️

Before you run this script, make sure you have the following:

  * **Python 3.x**: Download from [python.org](https://www.python.org/).
  * **OpenAI API Key**: You need an API key from OpenAI with access to GPT-4 models.
  * **Required Python Libraries**: These will be installed via `pip`.

## Installation 💻

1.  **Clone the repository** (or download the script file directly):

    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2.  **Create a `requirements.txt` file**: In the root directory of your project, create a file named `requirements.txt` and paste the following content:

    ```
    requests
    beautifulsoup4
    openai
    ```

3.  **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

## Configuration 🔑

You must add your OpenAI API key to the script. Open the script file and find this line:

```python
client = OpenAI(api_key="YOUR API")  # <-- apna API key yahan daalein
```

Replace `"YOUR API"` with your actual OpenAI API key.

## Usage ▶️

1.  Ensure you have completed the Installation and Configuration steps.
2.  Run the script from your terminal:
    ```bash
    python your_script_name.py
    ```

The script will then:

1.  Navigate to the main assessor list page.
2.  Identify and loop through each assessor table on the page.
3.  For each assessor, visit their profile link.
4.  Use the AI enrichment functions to extract and supplement data.
5.  Cache the results for each unique company.
6.  Save the complete dataset to `assessor_list.csv` in the same directory.

## Output CSV Format 📊

The generated CSV file (`assessor_list.csv`) will have the following columns:

`Company Name`, `Areas of Assessment`, `In-Person/Virtual Assessment`, `Region`, `Age Groups Supported`, `First Name`, `Last Name`, `Areas of Interest`, `Experience`, `State`, `County`, `Phone`, `Email`, `Website`, `LinkedIn`, `Address 1`, `City`, `Street Address`, `Zip Code`, `Type`, `Social Media`, `#2 Social Media`, `Notes`, `Assessor List`, `Profile Link`.

## Important Notes ⚠️

  * **API Costs**: This script uses the `gpt-4.1` model, which is a powerful but paid service. Scraping a large number of profiles will incur costs on your OpenAI account. Monitor your usage and set spending limits if necessary.
  * **Website Structure**: The script is tailored to the specific HTML structure and selectors (e.g., `div#content-area-row-1`) of `charterselpa.org`. If the website's design changes, the script may require updates.
  * **AI Data Accuracy**: The quality of the extracted data is dependent on the AI's ability to correctly parse the HTML and find information online. Always review the output for accuracy.
  * **Rate Limiting**: The script includes a `time.sleep()` delay to be polite to the server. Aggressive scraping can still lead to your IP address being blocked.
  * **API Model**: The script is hardcoded to use `gpt-4.1`. If you wish to use a different model (e.g., `gpt-3.5-turbo` to reduce costs), you must update the `model="..."` parameter in both `enrich_with_chatgpt_` functions.

## Contributing 🤝

Feel free to fork this repository, open issues, and submit pull requests if you have suggestions for improvements or bug fixes.
