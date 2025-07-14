# USPTO Patent Scraper

This Python script automates the process of searching and retrieving patent data from the official USPTO Public Patent Search website. It performs multi-faceted queries, collects unique patent document IDs, and then fetches detailed information for each patent, such as its title, abstract, filing date, and inventors.

-----

## 📋 Features

  - **Multi-Query Execution**: Sends multiple, complex search queries to the USPTO database in a single run.
  - **Unique ID Aggregation**: Collects patent document IDs from all search results and automatically removes duplicates.
  - **Detailed Data Extraction**: Fetches comprehensive details for each patent, including:
      - Patent Number & Application Number
      - Invention Title
      - Full Abstract
      - All Claims (in HTML format)
      - Filing Date
      - Inventor Names
  - **Polite Scraping**: Includes a configurable delay between requests to avoid overwhelming the server.
  - **Customizable**: Easily modify search queries, headers, and cookies to match your specific needs.

-----

## ⚙️ How It Works

The script operates in two main phases:

### 1\. Phase 1: Search and ID Collection

1.  **Define Queries**: The script starts with one or more predefined JSON payloads (`json_data1`, `json_data2`, etc.). Each payload contains a specific search query using USPTO's search syntax (e.g., `TTL(...)` for Title, `ABST(...)` for Abstract).
2.  **Send POST Request**: For each query, it sends a `POST` request to the `https://ppubs.uspto.gov/api/searches/searchWithBeFamily` API endpoint. This mimics the action of a user performing a search on the website.
3.  **Collect IDs**: The API returns a list of patents matching the query. The script parses this response, extracts the `documentId` for each patent, and adds the top 100 IDs from each query to a Python `set` to ensure all collected IDs are unique.

### 2\. Phase 2: Detailed Data Fetching & Display

1.  **Iterate Through IDs**: The script then iterates through the list of unique document IDs gathered in Phase 1.
2.  **Send GET Request**: For each `documentId`, it constructs a new URL and sends a `GET` request to the `https://ppubs.uspto.gov/api/patents/highlight/{doc_id}` endpoint. This API provides the full details for a specific patent.
3.  **Extract and Display**: The script parses the detailed JSON response, extracts key information (title, abstract, claims, etc.), and prints it to the console in a clean, readable format.

-----

## 🚀 Getting Started

Follow these instructions to set up and run the script on your local machine.

### Prerequisites

  - Python 3.7 or higher
  - The `requests` library

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/your-repository-name.git
    cd your-repository-name
    ```

2.  **Install the required Python library:**

    ```bash
    pip install requests
    ```

### ⚠️ Important: Updating Session Tokens

The `cookies` and `headers` in the script contain **session-specific tokens** (`aws-waf-token`, `x-access-token`) that will expire. You **must** replace them with your own valid tokens before running the script.

**How to get new tokens:**

1.  Open your web browser (e.g., Chrome, Firefox).
2.  Go to the [USPTO Public Patent Search](https://ppubs.uspto.gov/pubwebapp/) website.
3.  Open the Developer Tools (usually by pressing `F12` or `Ctrl+Shift+I`).
4.  Go to the "Network" tab.
5.  Perform a search on the website.
6.  Find a `POST` request to `searchWithBeFamily` in the network log.
7.  Click on it, and under the "Headers" tab, find the `cookie` and `x-access-token` values.
8.  Copy these new values and paste them into the corresponding `cookies` and `headers` dictionaries in the Python script.

### Usage

Once you have updated the session tokens, simply run the script from your terminal:

```bash
python your_script_name.py
```

The script will print its progress, the total number of unique IDs found, and then the detailed information for each patent.

-----

## 🔧 Customization

You can easily customize the script's behavior by modifying the JSON query objects.

### Modifying Search Queries

To change the search terms, edit the `q` key within any of the `json_data` dictionaries. The query syntax uses boolean operators (`AND`, `OR`) and field codes:

  - `TTL(...)`: Search within the patent title.
  - `ABST(...)`: Search within the abstract.
  - `ACLM(...)`: Search within the claims.

**Example:** To search for patents with "database" in the title and "machine learning" in the abstract, you would set:

```python
'q': 'TTL("database") AND ABST("machine learning")'
```

You can add more `json_data` objects to the `all_json_queries` list to perform additional searches.

-----

## ⚖️ Disclaimer

  - This script is intended for educational purposes only.
  - Web scraping may be against the terms of service of the USPTO website. Use this script responsibly and at your own risk.
  - The website's API and structure may change at any time, which could break this script. Regular maintenance may be required.

-----

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
