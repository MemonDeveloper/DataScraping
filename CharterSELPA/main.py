import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv
import time

base_url = "https://charterselpa.org/Independent-Educational-Evaluation-IEE-Assessor-List/"
print("Opening the main assessor list page...")
response = requests.get(base_url)
print("Main page status:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")
all_data = []

tables = soup.find_all("table")
print(f"Total assessor tables found: {len(tables)}")

for table_idx, table in enumerate(tables, start=1):
    # Find the Assessor List name (heading before the table)
    heading_tag = table.find_previous(["h2", "h3", "h4"], class_="responsive-tabs__heading")
    if not heading_tag:
        # Agar heading_tag nahi mila, alternate dhoondho
        alt_heading = table.find_previous(["h2", "h3", "h4"])
        assessor_list_name = alt_heading.get_text(strip=True) if alt_heading else f"List {table_idx}"
    else:
        assessor_list_name = heading_tag.get_text(strip=True)

    print(f"Processing table {table_idx}: {assessor_list_name}")

    rows = table.find_all("tr")[1:]  # Skip header row
    print(f"  Number of rows found: {len(rows)}")

    for row_idx, row in enumerate(rows, start=1):
        cols = row.find_all("td")
        if len(cols) < 4:
            continue
        
        name_tag = cols[0].find("a")
        if not name_tag:
            continue

        name = name_tag.get_text(strip=True)
        raw_href = name_tag["href"]

        # Fix URL: remove "__catapult_pages/<UUID>/" and ".html"
        if "__catapult_pages/" in raw_href:
            raw_href = raw_href.split("/", 2)[-1]
        if raw_href.endswith(".html"):
            raw_href = raw_href[:-5]

        link = urljoin(base_url, raw_href)

        areas = cols[1].get_text(" ", strip=True)
        assessment_type = cols[2].get_text(" ", strip=True)
        region = cols[3].get_text(" ", strip=True)

        print(f"    Row {row_idx}: {name} -> {link}")

        try:
            detail_resp = requests.get(link)
        except Exception as e:
            print("      Error opening detail page:", e)
            continue

        detail_soup = BeautifulSoup(detail_resp.text, "html.parser")
        details_text = detail_soup.get_text(" ", strip=True)

        first_name = last_name = note = address = state = phone = email = website = remark = None

        # Extract main and secondary contacts
        if "Contact:" in details_text:
            contact = details_text.split("Contact:")[1].split("Primary")[0].strip()
            contacts = [c.strip() for c in contact.split(",") if c.strip()]

            if contacts:
                main_contact_parts = contacts[0].split(" ")
                if len(main_contact_parts) > 1:
                    first_name = " ".join(main_contact_parts[:-1])
                    last_name = main_contact_parts[-1]
                else:
                    first_name = main_contact_parts[0]

                if len(contacts) > 1:
                    note = ", ".join(contacts[1:])

        # Extract address
        if "Address(es):" in details_text:
            address = details_text.split("Address(es):")[1].split("Region")[0].strip()
        elif "Address(es):" in details_text:
            address = details_text.split("Address(es):")[1].split("Region")[0].strip()

        # Extract state
        if "Address(es):" in details_text:
            state = details_text.split("Address(es):")[1].split("Region")[0].strip()

        # Extract phone
        if "Phone Number:" in details_text:
            phone = details_text.split("Phone Number:")[1].split("Email")[0].strip()

        # Extract email
        if "Email Address:" in details_text:
            email = details_text.split("Email Address:")[1].split("Website Link:")[0].strip()

        # Extract website
        if "Website Link:" in details_text:
            website = details_text.split("Website Link:")[1].split("_____")[0].strip()
        
        # Extract remark
        if "Approved as an NPA/S by CDE" in details_text:
            remark = details_text.split("Approved as an NPA/S by CDE:")[1].split("Areas of Assessment")[0].strip()

        all_data.append({
            "Assessor List": assessor_list_name,
            "Name": name,
            "Link": link,
            "Areas of Assessment": areas,
            "In-Person/Virtual Assessment": assessment_type,
            "Region": region,
            "First Name": first_name,
            "Last Name": last_name,
            "Secondary Contact": note,
            "Address": address,
            "State": state,
            "Phone": phone,
            "Email": email,
            "Website": website,
            "Remark": remark
        })

        time.sleep(0.5)  # Be polite to the server

print("\nScraping complete! Total records collected:", len(all_data))

# Save to CSV
output_file = "assessor_list.csv"
with open(output_file, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=all_data[0].keys())
    writer.writeheader()
    writer.writerows(all_data)

print(f"Data saved to {output_file}")