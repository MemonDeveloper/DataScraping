import requests
import time
import re
import os
from bs4 import BeautifulSoup
from docx import Document
from docx.shared import Inches, Pt
from fpdf import FPDF
from datetime import datetime
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# Define folder name
output_folder = "OCX_InfoSyncEngine"

# Create folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

cookies = {
    '_ga': 'GA1.1.1490333756.1752502650',
    'QSI_SI_7WgrKZZwMjtuFh4_intercept': 'true',
    '_ga_CD30TTEK1F': 'GS2.1.s1752514458$o5$g0$t1752514458$j60$l0$h0',
    '_ga_Q5HVZK168H': 'GS2.1.s1752514811$o2$g1$t1752514900$j57$l0$h0',
    'aws-waf-token': '7410d63c-cc22-4642-8563-e0d0e2738959:BQoAqEqAINsuAAAA:7Z5tX16/G0wRLhrROmSckRcxC7xyYlasiJmgOc8vzsRqlkogqBY9Dcd/2m+45PHfz9NnhF41Lir5I4nj2s7ncPvwoxl5oISwygfFiuo7r1M3ro6GBbF7gDfWFgMYkeUv5u52IaPjpIdKufwNtFIZNUNsdMQWPRNPVdKyDEl53nnUvc5ARKm7ecyt+wuvskZuIi+iAGFp55UzcCXOq54m+OAysNyRjRhz1vJscSuWp/00mpZ4GHRA2pjEBhU12jQo',
    '_ga_M4L1KRPWXE': 'GS2.1.s1752517472$o1$g1$t1752517489$j43$l0$h0',
    '_ga_1KBHG37G8W': 'GS2.1.s1752514821$o3$g1$t1752517490$j60$l0$h0',
    '_ga_F4Q7EX1K95': 'GS2.1.s1752595279$o6$g1$t1752595298$j41$l0$h0',
    '_ga_CSLL4ZEK4L': 'GS2.1.s1752595279$o6$g1$t1752595298$j41$l0$h0',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json; charset=UTF-8',
    'origin': 'https://ppubs.uspto.gov',
    'priority': 'u=1, i',
    'referer': 'https://ppubs.uspto.gov/pubwebapp/',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    'x-access-token': 'eyJzdWIiOiJlODFlMzA1YS0xNjJiLTQ5NWUtOWRkZC05MjNiNzI0YmM1MmIiLCJ2ZXIiOiJhNWI2M2JjZS00MzFhLTRlODItYWFhOC00YmE5NzFmMjQwYmQiLCJleHAiOjB9',
    'x-requested-with': 'XMLHttpRequest',
    # 'cookie': '_ga=GA1.1.1490333756.1752502650; QSI_SI_7WgrKZZwMjtuFh4_intercept=true; _ga_CD30TTEK1F=GS2.1.s1752514458$o5$g0$t1752514458$j60$l0$h0; _ga_Q5HVZK168H=GS2.1.s1752514811$o2$g1$t1752514900$j57$l0$h0; aws-waf-token=7410d63c-cc22-4642-8563-e0d0e2738959:BQoAqEqAINsuAAAA:7Z5tX16/G0wRLhrROmSckRcxC7xyYlasiJmgOc8vzsRqlkogqBY9Dcd/2m+45PHfz9NnhF41Lir5I4nj2s7ncPvwoxl5oISwygfFiuo7r1M3ro6GBbF7gDfWFgMYkeUv5u52IaPjpIdKufwNtFIZNUNsdMQWPRNPVdKyDEl53nnUvc5ARKm7ecyt+wuvskZuIi+iAGFp55UzcCXOq54m+OAysNyRjRhz1vJscSuWp/00mpZ4GHRA2pjEBhU12jQo; _ga_M4L1KRPWXE=GS2.1.s1752517472$o1$g1$t1752517489$j43$l0$h0; _ga_1KBHG37G8W=GS2.1.s1752514821$o3$g1$t1752517490$j60$l0$h0; _ga_F4Q7EX1K95=GS2.1.s1752595279$o6$g1$t1752595298$j41$l0$h0; _ga_CSLL4ZEK4L=GS2.1.s1752595279$o6$g1$t1752595298$j41$l0$h0',
}

json_data1 = {
    'start': 0,
    'pageCount': 500,
    'sort': 'date_publ desc',
    'docFamilyFiltering': 'familyIdFiltering',
    'searchType': 1,
    'familyIdEnglishOnly': True,
    'familyIdFirstPreferred': 'US-PGPUB',
    'familyIdSecondPreferred': 'USPAT',
    'familyIdThirdPreferred': 'FPRS',
    'showDocPerFamilyPref': 'showEnglish',
    'queryId': 0,
    'tagDocSearch': False,
    'query': {
        'anchorDocIds': None,
        'querySource': 'brs',
        'caseId': 93845335,
        'hl_snippets': '2',
        'op': 'OR',
        'q': 'TTL ("system") AND ABST("data optimization" OR "information filtering")',
        'queryName': 'TTL ("system") AND ABST("data optimization" OR "information filtering")',
        'highlights': '1',
        'qt': 'brs',
        'spellCheck': False,
        'viewName': 'tile',
        'plurals': True,
        'britishEquivalents': True,
        'databaseFilters': [
            {
                'databaseName': 'US-PGPUB',
                'countryCodes': [],
            },
            {
                'databaseName': 'USPAT',
                'countryCodes': [],
            },
            {
                'databaseName': 'USOCR',
                'countryCodes': [],
            },
        ],
        'searchType': 1,
        'ignorePersist': True,
        'userEnteredQuery': 'TTL ("system") AND ABST("data optimization" OR "information filtering")',
    },
}

json_data2 = {
    'start': 0,
    'pageCount': 500,
    'sort': 'date_publ desc',
    'docFamilyFiltering': 'familyIdFiltering',
    'searchType': 1,
    'familyIdEnglishOnly': True,
    'familyIdFirstPreferred': 'US-PGPUB',
    'familyIdSecondPreferred': 'USPAT',
    'familyIdThirdPreferred': 'FPRS',
    'showDocPerFamilyPref': 'showEnglish',
    'queryId': 0,
    'tagDocSearch': False,
    'query': {
        'anchorDocIds': None,
        'querySource': 'brs',
        'caseId': 93845335,
        'hl_snippets': '2',
        'op': 'OR',
        'q': 'TTL ("platform") AND ABST("interactive engine" OR "multi-layer")',
        'queryName': 'TTL ("platform") AND ABST("interactive engine" OR "multi-layer")',
        'highlights': '1',
        'qt': 'brs',
        'spellCheck': False,
        'viewName': 'tile',
        'plurals': True,
        'britishEquivalents': True,
        'databaseFilters': [
            {
                'databaseName': 'US-PGPUB',
                'countryCodes': [],
            },
            {
                'databaseName': 'USPAT',
                'countryCodes': [],
            },
            {
                'databaseName': 'USOCR',
                'countryCodes': [],
            },
        ],
        'searchType': 1,
        'ignorePersist': True,
        'userEnteredQuery': 'TTL ("platform") AND ABST("interactive engine" OR "multi-layer")',
    },
}

json_data3 = {
    'start': 0,
    'pageCount': 500,
    'sort': 'date_publ desc',
    'docFamilyFiltering': 'familyIdFiltering',
    'searchType': 1,
    'familyIdEnglishOnly': True,
    'familyIdFirstPreferred': 'US-PGPUB',
    'familyIdSecondPreferred': 'USPAT',
    'familyIdThirdPreferred': 'FPRS',
    'showDocPerFamilyPref': 'showEnglish',
    'queryId': 0,
    'tagDocSearch': False,
    'query': {
        'anchorDocIds': None,
        'querySource': 'brs',
        'caseId': 93845335,
        'hl_snippets': '2',
        'op': 'OR',
        'q': 'TTL("module") AND ABST("coordination protocol") AND ABST("logic management")',
        'queryName': 'TTL("module") AND ABST("coordination protocol") AND ABST("logic management")',
        'highlights': '1',
        'qt': 'brs',
        'spellCheck': False,
        'viewName': 'tile',
        'plurals': True,
        'britishEquivalents': True,
        'databaseFilters': [
            {
                'databaseName': 'US-PGPUB',
                'countryCodes': [],
            },
            {
                'databaseName': 'USPAT',
                'countryCodes': [],
            },
            {
                'databaseName': 'USOCR',
                'countryCodes': [],
            },
        ],
        'searchType': 1,
        'ignorePersist': True,
        'userEnteredQuery': 'TTL("module") AND ABST("coordination protocol") AND ABST("logic management")',
    },
}

# JSON queries (already defined)
all_json_queries = [json_data1, json_data2, json_data3]

all_ids = set()          # ensures uniqueness
doc_type_pairs = []      # stores (documentId, type)

# STEP 1: Fetch documentId and type
for idx, json_data in enumerate(all_json_queries, start=1):
    print(f"🔍 Sending query {idx}...")
    response = requests.post("https://ppubs.uspto.gov/api/searches/searchWithBeFamily", json=json_data, headers=headers, cookies=cookies)

    if response.status_code == 200:
        data = response.json()
        patents = data.get('patents', [])
        
        doc_ids_this_round = []
        for doc in patents:
            if 'documentId' in doc and 'type' in doc:
                doc_id = doc['documentId'].replace(" ", "-")
                doc_type = doc['type']
                doc_type_pairs.append((doc_id, doc_type))
                doc_ids_this_round.append(doc_id)
        
        # Use top 100 document IDs from current result
        top_100_ids = doc_ids_this_round[:100]
        all_ids.update(top_100_ids)
    else:
        print(f"❌ Query {idx} failed: {response.status_code} - {response.text}")

# Convert to sorted list
unique_ids = sorted(all_ids)

# Output result
print(f"\n✅ Total unique document IDs: {len(unique_ids)}")

# --- Clean HTML content ---
def clean_html(text):
    if not text:
        return None
    soup = BeautifulSoup(text, "html.parser")

    # Replace all <br> or <br/> tags with newlines
    for br in soup.find_all("br"):
        br.replace_with("\n")

    # Keep other tags (like <b>, <i>) intact — just get text
    return soup.get_text().strip()

# --- Flatten JSON ignoring nulls ---
def flatten_json(y, parent_key='', sep='.'):
    items = []
    for k, v in y.items():
        if v is None:
            continue
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_json(v, new_key, sep=sep).items())
        elif isinstance(v, list):
            if all(isinstance(i, dict) for i in v):
                for idx, item in enumerate(v):
                    items.extend(flatten_json(item, f"{new_key}[{idx}]", sep=sep).items())
            else:
                cleaned_list = [str(i) for i in v if i is not None]
                if cleaned_list:
                    items.append((new_key, ', '.join(cleaned_list)))
        else:
            items.append((new_key, v))
    return dict(items)

# --- Fetch patent details ---
def fetch_patent_details(doc_id, doc_type):
    global success_count, fail_count
    detail_url = f"https://ppubs.uspto.gov/api/patents/highlight/{doc_id}"
    params = {
        'queryId': '87362852',
        'source': doc_type,
        'includeSections': 'true',
        'uniqueId': ''
    }
    try:
        response = requests.get(detail_url, params=params, cookies=cookies, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except Exception as e:
        print(f"❌ Exception occurred: {e}")
        return None

# --- Init PDF & DOCX ---
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_font('ArialUnicode', '', 'ArialUnicodeMS.ttf', uni=True)
pdf.set_font('ArialUnicode', '', 10)

doc = Document()
doc.add_heading('Patent Details Report', 0)

success_count = 0
fail_count = 0

for i, (doc_id, doc_type) in enumerate(doc_type_pairs[:5], start=1):
    result = fetch_patent_details(doc_id, doc_type)
    if not result:
        fail_count += 1
        print(f"❌ Failed #{fail_count}: {doc_id} ({doc_type})")
        continue

    # Clean known HTML fields before flattening
    for html_key in ["abstractHtml", "descriptionHtml", "claimsHtml", "backgroundTextHtml"]:
        if html_key in result:
            result[html_key] = clean_html(result[html_key])

    flat_data = flatten_json(result)
    success_count += 1
    patent_number = flat_data.get("documentId", "")
    title = flat_data.get("inventionTitle", "Patent Details")

    # --- PDF Output ---
    try:
        pdf.add_page()
        pdf.set_font('ArialUnicode', '', 12)
        pdf.cell(0, 10, f"Patent Number: {patent_number}", ln=True)
        pdf.set_font('ArialUnicode', '', 10)
        for k, v in flat_data.items():
            pdf.multi_cell(0, 6, f"{k}: {v}")
        pdf.multi_cell(0, 6, "-" * 100)
    except Exception as e:
        print(f"❌ PDF generation failed for {doc_id}: {e}")

    # --- DOCX Output ---
    try:
        doc.add_heading(title, level=1)
        for k, v in flat_data.items():
            paragraph = doc.add_paragraph()
            run_label = paragraph.add_run(f"{k}: ")
            run_label.bold = True
            run_label.font.size = Pt(12)
            run_value = paragraph.add_run(str(v))
            run_value.font.size = Pt(12)
        doc.add_paragraph("-" * 100)
    except Exception as e:
        print(f"❌ DOCX generation failed for {doc_id}: {e}")

    print(f"✅ Success #{success_count}: {doc_id} ({doc_type})")
    time.sleep(1)

# --- Save files ---
timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
output_folder = "OCX_InfoSyncEngine"
os.makedirs(output_folder, exist_ok=True)

pdf_path = os.path.join(output_folder, f"OCX_InfoSyncEngine_{timestamp}.pdf")
docx_path = os.path.join(output_folder, f"OCX_InfoSyncEngine_{timestamp}.docx")

pdf.output(pdf_path)
doc.save(docx_path)

print("\n📊 Fetch Summary:")
print(f"✅ Total Success: {success_count}")
print(f"❌ Total Failed : {fail_count}")
print(f"\n✅ Combined PDF saved as: {pdf_path}")
print(f"✅ Combined DOCX saved as: {docx_path}")

# --- Google Drive Upload Setup ---
# gauth = GoogleAuth()
# gauth.LoadCredentialsFile("credentials.json")

# if gauth.credentials is None:
#     # First time authorization
#     gauth.LocalWebserverAuth()
# elif gauth.access_token_expired:
#     # Refresh token if expired
#     gauth.Refresh()
# else:
#     # Already authorized
#     gauth.Authorize()

# # Save credentials for future runs
# gauth.SaveCredentialsFile("credentials.json")

# # Create Drive instance AFTER authentication
# drive = GoogleDrive(gauth)

# # --- Step 1: Check if folder already exists ---
# folder_name = "OCX_InfoSyncEngine"
# folder_id = None

# print(f"🔍 Searching for folder: {folder_name}")

# file_list = drive.ListFile({
#     'q': f"title='{folder_name}' and mimeType='application/vnd.google-apps.folder' and trashed=false"
# }).GetList()

# if file_list:
#     folder_id = file_list[0]['id']
#     print(f"📂 Folder already exists: {folder_name} (ID: {folder_id})")
# else:
#     # --- Step 2: Create folder ---
#     print(f"📁 Creating folder: {folder_name}")
#     folder_metadata = {
#         'title': folder_name,
#         'mimeType': 'application/vnd.google-apps.folder'
#     }
#     folder = drive.CreateFile(folder_metadata)
#     folder.Upload()
#     folder_id = folder['id']
#     print(f"✅ Folder created with ID: {folder_id}")

# # --- Step 3: Upload files into the folder ---
# print(f"🚀 Uploading files to folder: {folder_name}")

# for filename in os.listdir(output_folder):
#     filepath = os.path.join(output_folder, filename)
#     if os.path.isfile(filepath):
#         try:
#             file_drive = drive.CreateFile({
#                 'title': filename,
#                 'parents': [{'id': folder_id}]
#             })
#             file_drive.SetContentFile(filepath)
#             file_drive.Upload()
#             print(f"✅ Uploaded: {filename}")
#         except Exception as e:
#             print(f"❌ Failed to upload {filename}: {e}")
