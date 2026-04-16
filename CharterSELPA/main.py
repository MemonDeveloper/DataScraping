import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv
import time
import json
from openai import OpenAI

# === OpenAI client ===
client = OpenAI(api_key="")  # <-- apna API key yahan daalein

# === Safe JSON loader ===
def safe_json_loads(content):
    try:
        content = content.strip()
        if content.startswith("```"):
            content = content.split("```")[1]
            if content.lower().startswith("json"):
                content = content[4:].strip()
        return json.loads(content)
    except Exception as e:
        print("JSON parse error:", e)
        return {}

# === First enrichment: HTML se data extraction ===
def enrich_with_chatgpt_using_html(html_content):
    prompt = f"""
    You are a data extraction assistant.

    Given the following HTML of an educational assessment company's profile, extract as many details as possible.
    - If "Name of Contact" has multiple names (e.g., "Dr. Timothy Castaneda, Jenny Elomaa"), 
      take the first full name as the main contact (ignore titles like Dr./Mr./Ms.) 
      and put any additional names in "Notes".
    - Split the first contact into "First Name" and "Last Name".
    - Fill all fields you can find; if missing, leave blank.

    Return strictly in JSON format with these fields:
    Company Name, Areas of Assessment, In-Person/Virtual Assessment, Region, Age Groups Supported,
    First Name, Last Name, Areas of Interest, Experience, State, County, Phone, Email, Website, LinkedIn,
    Address 1, City, Street Address, Zip Code, Type, Social Media, #2 Social Media, Notes.

    HTML:
    {html_content}
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4.1",
            messages=[
                {"role": "system", "content": "You are a helpful data extraction assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2
        )
        return safe_json_loads(response.choices[0].message.content)
    except Exception as e:
        print("Error in HTML enrichment:", e)
        return {}

# === Second enrichment: Missing fields ko web se fill karna ===
def enrich_with_chatgpt_by_name(company_name, current_data):
    missing_fields = [k for k, v in current_data.items() if not v and k not in ["Assessor List", "Profile Link"]]
    if not missing_fields:
        return current_data

    prompt = f"""
    You are a research assistant. 
    I have partial information about this educational assessment provider:

    Company Name: {company_name}

    These fields are missing: {', '.join(missing_fields)}.

    Please search the web and fill them. 
    Return ONLY valid JSON, without explanation or extra text.

    Fields:
    Company Name, Areas of Assessment, In-Person/Virtual Assessment, Region, Age Groups Supported,
    First Name, Last Name, Areas of Interest, Experience, State, County, Phone, Email, Website, LinkedIn,
    Address 1, City, Street Address, Zip Code, Type, Social Media, #2 Social Media, Notes.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4.1",
            messages=[
                {"role": "system", "content": "You are a helpful research assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2
        )
        enriched = safe_json_loads(response.choices[0].message.content)
        for k, v in enriched.items():
            if k in current_data and not current_data[k] and v:
                current_data[k] = v
        return current_data
    except Exception as e:
        print("Error in second GPT enrichment:", e)
        return current_data

# === Main scraper ===
base_url = "https://charterselpa.org/Independent-Educational-Evaluation-IEE-Assessor-List/"
output_file = "assessor_list.csv"
delay_seconds = 1.0

print("Opening the main assessor list page...")
response = requests.get(base_url)
print("Main page status:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")
all_data = []
company_cache = {}  # Cache to reuse company data

tables = soup.find_all("table")
print(f"Total assessor tables found: {len(tables)}")

for table_idx, table in enumerate(tables, start=1):
    heading_tag = table.find_previous(["h2", "h3", "h4"], class_="responsive-tabs__heading")
    if not heading_tag:
        alt_heading = table.find_previous(["h2", "h3", "h4"])
        assessor_list_name = alt_heading.get_text(strip=True) if alt_heading else f"List {table_idx}"
    else:
        assessor_list_name = heading_tag.get_text(strip=True)

    print(f"\nProcessing table {table_idx}: {assessor_list_name}")

    rows = table.find_all("tr")[1:]
    print(f"  Number of rows found: {len(rows)}")

    for row_idx, row in enumerate(rows, start=1):
        cols = row.find_all("td")
        if len(cols) < 4:
            continue

        name_tag = cols[0].find("a")
        if not name_tag:
            continue

        name = name_tag.get_text(strip=True)
        company_key = name.lower().strip()
        raw_href = name_tag["href"]

        if "__catapult_pages/" in raw_href:
            raw_href = raw_href.split("/", 2)[-1]
        if raw_href.endswith(".html"):
            raw_href = raw_href[:-5]

        link = urljoin(base_url, raw_href)
        print(f"    Row {row_idx}: {name} -> {link}")

        # Check cache for this company
        if company_key in company_cache:
            print(f"      Cached: Using previously scraped data for {name}")
            gpt_data = company_cache[company_key].copy()
            gpt_data["Assessor List"] = assessor_list_name
            gpt_data["Profile Link"] = link
            all_data.append(gpt_data)
            continue

        # Otherwise, fetch detail page
        try:
            detail_resp = requests.get(link)
        except Exception as e:
            print("      Error opening detail page:", e)
            continue

        detail_soup = BeautifulSoup(detail_resp.text, "html.parser")
        target_div = detail_soup.select_one('div#content-area-row-1 div#content-area-row-1-column-1')
        html_content = target_div.decode_contents() if target_div else ""

        if not html_content:
            print("      No target HTML found")
            continue

        gpt_data = enrich_with_chatgpt_using_html(html_content)

        gpt_data["Assessor List"] = assessor_list_name
        gpt_data["Profile Link"] = link

        if gpt_data.get("Company Name"):
            enriched_data = enrich_with_chatgpt_by_name(gpt_data["Company Name"], gpt_data)
            if enriched_data:
                gpt_data.update(enriched_data)

        # Cache this company's data
        company_cache[company_key] = gpt_data.copy()
        all_data.append(gpt_data)

        time.sleep(delay_seconds)

print("\nScraping complete! Total records collected:", len(all_data))

if all_data:
    with open(output_file, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=all_data[0].keys())
        writer.writeheader()
        writer.writerows(all_data)
    print(f"Data saved to {output_file}")
else:
    print("No data to save.")
