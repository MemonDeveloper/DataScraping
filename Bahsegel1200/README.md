# Bahsegel1200 Account Checker & Data Extractor 🤖📊

This Python application provides a graphical user interface (GUI) to automate the process of checking account details and balances on `bahsegel1200.com`. It reads account credentials from an Excel file, uses `undetected-chromedriver` to log in, extracts various personal and balance information, and then saves all the collected data into a new Excel file.

-----

## Features ✨

  * **GUI-Driven**: Easy-to-use interface built with `tkinter`.
  * **Automated Login**: Uses `undetected-chromedriver` to bypass bot detection and log into `bahsegel1200.com` accounts.
  * **Data Extraction**: Gathers comprehensive details from each account's profile, including:
      * Username, First Name, Last Name
      * Address, Postal Code, City, Country
      * Birth Date, Email, Mobile Phone
      * Total Balance, Bonus Balance, Real Balance, Token Balance
  * **Excel Integration**:
      * Reads account credentials from a specified Excel sheet (`bahsegel1200.xlsx`).
      * Generates a timestamped backup of the input file and writes extracted data to a new "Result" sheet within it.
      * Applies automatic column width and basic formatting to the output Excel.
  * **Progress Tracking**: Displays real-time updates and success/failure messages directly in the GUI.
  * **Error Handling**: Catches common errors during web navigation and data extraction, reporting them to the user.

-----

## Prerequisites 🛠️

Before running this application, ensure you have the following installed:

1.  **Python 3.x**: Download from [python.org](https://www.python.org/downloads/).
2.  **Google Chrome Browser**: `undetected-chromedriver` requires an installed version of Google Chrome.
3.  **Required Python Libraries**: These will be installed via `pip`.

-----

## Installation 💻

1.  **Clone the repository** (or download the `main.py` file directly):
    ```bash
    git clone https://github.com/MemonDeveloper/Bahsegel1200-Account-Checker.git
    cd Bahsegel1200-Account-Checker
    ```
2.  **Create a `requirements.txt` file**: In the root directory of your project, create a file named `requirements.txt` and paste the following content:
    ```
    tkinter # Often built-in, but good to list
    pandas
    openpyxl
    undetected-chromedriver
    requests
    beautifulsoup4
    selenium
    ```
3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

-----

## Usage ▶️

1.  **Prepare your input Excel file**:

      * Create an Excel file named `bahsegel1200.xlsx` in the same directory as the script.
      * Inside this Excel file, create a sheet named exactly `bahsegel1200 List`.
      * In this sheet:
          * Column **A** should contain the **Account usernames**.
          * Column **B** should contain the **Passwords** corresponding to the usernames.

    *Example `bahsegel1200.xlsx` structure:*

    | Account (Column A) | Password (Column B) |
    | :----------------- | :------------------ |
    | username1          | password1           |
    | username2          | password2           |
    | ...                | ...                 |

2.  **Run the script**:

    ```bash
    python main.py
    ```

3.  **Interact with the GUI**:

      * A simple Tkinter window titled "Quick Analytics v.1.1" will appear.
      * Click the **"bahsegel1200"** button to start the process.
      * The text area in the GUI will display real-time updates on the script's progress.
      * Once completed, a message box will confirm the process is finished, and the results will be saved.

-----

## Output Excel Format 📊

The script will create a new Excel file (e.g., `bahsegel1200 - Result YYYY-MM-DD HH-MM-SS.xlsx`) in the same directory. This file will contain two sheets:

1.  **`bahsegel1200 List`**: This is a copy of your original input sheet (Columns A and B).
2.  **`Result`**: This new sheet will contain the extracted data, with the following columns:
      * **Account (original)**
      * **Password (original)**
      * **username**
      * **firstname**
      * **lastname**
      * **address**
      * **postalcode**
      * **brithdate**
      * **city**
      * **country**
      * **email**
      * **mobile\_phone**
      * **totalbalance**
      * **bonusbalance**
      * **realbalance**
      * **tokenbalance**

-----

## Important Notes & Disclaimer ⚠️

  * **Website Specificity**: This script is **highly specialized** for the current HTML structure and login flow of `https://www.bahsegel1200.com/`. Any changes to the website's design (e.g., element IDs, class names, navigation paths) will likely break the script, requiring updates to the Selenium selectors.
  * **Ethical Use**: Please use this tool responsibly and in compliance with the terms of service of `bahsegel1200.com`. Unauthorized or excessive scraping can lead to your IP being blocked or account suspension. The developers of this script are not responsible for any misuse.
  * **Account Security**: Your account credentials from the Excel file are used directly by the script for login. Ensure your `bahsegel1200.xlsx` file is stored securely.
  * **`undetected-chromedriver`**: While `undetected-chromedriver` helps in bypassing basic bot detection, advanced measures by websites might still detect and block the automation.
  * **Internet Connection**: A stable internet connection is required for the script to function correctly.
  * **Performance**: Processing a large number of accounts may take a considerable amount of time.

-----

## Support My Work ❤️

If you find this project useful and would like to support its development, any contribution is greatly appreciated\! Your support helps in maintaining and improving this application.

Here are a few ways you can contribute financially:

  * **Patreon**: [Link to your Patreon page] (e.g., `https://www.patreon.com/YourUsername`)
  * **Buy Me a Coffee**: [Link to your Buy Me a Coffee page] (e.g., `https://www.buymeacoffee.com/YourUsername`)
  * **PayPal**: [Link to your PayPal.Me or direct PayPal donation link] (e.g., `https://paypal.me/YourUsername`)

Thank you for your support\!

-----

## Contributing 🤝

Feel free to fork this repository, open issues, and submit pull requests if you have suggestions for improvements or bug fixes. Ideas for future enhancements include:

  * Adding more robust error handling and retry mechanisms.
  * Implementing configurable delays to further mimic human behavior.
  * Expanding compatibility to other similar websites (requires significant code modification).
  * Adding proxy support.
  * Improving the GUI with more options or visual feedback.

-----
