import requests
import time

cookies = {
    '_ga': 'GA1.1.1490333756.1752502650',
    '_ga_Q5HVZK168H': 'GS2.1.s1752503812$o1$g1$t1752504521$j22$l0$h0',
    '_ga_CD30TTEK1F': 'GS2.1.s1752502649$o1$g1$t1752504532$j59$l0$h0',
    '_ga_1KBHG37G8W': 'GS2.1.s1752503435$o1$g1$t1752504587$j59$l0$h0',
    'QSI_SI_7WgrKZZwMjtuFh4_intercept': 'true',
    '_ga_F4Q7EX1K95': 'GS2.1.s1752502659$o3$g1$t1752506540$j53$l0$h0',
    '_ga_CSLL4ZEK4L': 'GS2.1.s1752502649$o1$g1$t1752506540$j53$l0$h0',
    'aws-waf-token': '7410d63c-cc22-4642-8563-e0d0e2738959:BQoAjBRqxQJEAAAA:sNszoI9S1RE6Zaz15XbwP9X+3+KlN1o50jXR2X1S+bt41jzDBRJRjSmjs6397u0eoTXnBH49oKKY3Tjc5xcUhWfx31qyycdZYLSv6GkMtHffwKtm7nq4ex+ldX7QEAEvLcfOdZz+1T/BRl2k5fFEM5dKyerhyQQVPeUv33CGnRtXIIaejkzEdMo3eTz0GzoBaDGaVPxyIf6UOd0Xb875+0NA5bsEf+wdaDTGulhUeHMc49xkLVEq5AmlH146x+pW',
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
    'x-access-token': 'eyJzdWIiOiI5MmVmNjRhMS1kMjQwLTQxOGUtOWY2Mi03ZTVlMzAzM2Q0NGQiLCJ2ZXIiOiIyMGNiMWMxMy1iZjE1LTQ2NjctOTBjYi0wOWRiYjUwOTkxODkiLCJleHAiOjB9',
    'x-requested-with': 'XMLHttpRequest',
    # 'cookie': '_ga=GA1.1.1490333756.1752502650; QSI_SI_7WgrKZZwMjtuFh4_intercept=true; _ga_CD30TTEK1F=GS2.1.s1752514458$o5$g0$t1752514458$j60$l0$h0; _ga_Q5HVZK168H=GS2.1.s1752514811$o2$g1$t1752514900$j57$l0$h0; aws-waf-token=7410d63c-cc22-4642-8563-e0d0e2738959:BQoAqEqAINsuAAAA:7Z5tX16/G0wRLhrROmSckRcxC7xyYlasiJmgOc8vzsRqlkogqBY9Dcd/2m+45PHfz9NnhF41Lir5I4nj2s7ncPvwoxl5oISwygfFiuo7r1M3ro6GBbF7gDfWFgMYkeUv5u52IaPjpIdKufwNtFIZNUNsdMQWPRNPVdKyDEl53nnUvc5ARKm7ecyt+wuvskZuIi+iAGFp55UzcCXOq54m+OAysNyRjRhz1vJscSuWp/00mpZ4GHRA2pjEBhU12jQo; _ga_M4L1KRPWXE=GS2.1.s1752517472$o1$g1$t1752517489$j43$l0$h0; _ga_1KBHG37G8W=GS2.1.s1752514821$o3$g1$t1752517490$j60$l0$h0; _ga_F4Q7EX1K95=GS2.1.s1752514456$o4$g1$t1752517941$j54$l0$h0; _ga_CSLL4ZEK4L=GS2.1.s1752514456$o4$g1$t1752517941$j54$l0$h0',
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
        'caseId': 93659606,
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
        'caseId': 93659606,
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
        'caseId': 93659606,
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

# JSON queries: json_data1, json_data2, json_data3 (already defined)
all_json_queries = [json_data1, json_data2, json_data3]

all_ids = set()  # using a set to ensure uniqueness

for idx, json_data in enumerate(all_json_queries, start=1):
    print(f"🔍 Sending query {idx}...")
    response = requests.post("https://ppubs.uspto.gov/api/searches/searchWithBeFamily", json=json_data, headers=headers, cookies=cookies)

    if response.status_code == 200:
        data = response.json()
        document_ids = [doc.get('documentId', '').replace(" ", "-") for doc in data.get('patents', [])]
        top_100_ids = document_ids[:100]
        all_ids.update(top_100_ids)  # set ensures uniqueness
    else:
        print(f"❌ Query {idx} failed: {response.status_code} - {response.text}")

# Convert to sorted list
unique_ids = sorted(all_ids)

# Output result
print(f"\n✅ Total unique document IDs: {len(unique_ids)}")
for doc_id in unique_ids:
    print(doc_id)

# --- STEP 2: PATENT DETAIL FETCH ---
def fetch_patent_details(doc_id):
    detail_url = f"https://ppubs.uspto.gov/api/patents/highlight/{doc_id}"
    cookies = {
        '_ga': 'GA1.1.1490333756.1752502650',
        'QSI_SI_7WgrKZZwMjtuFh4_intercept': 'true',
        '_ga_CD30TTEK1F': 'GS2.1.s1752514458$o5$g0$t1752514458$j60$l0$h0',
        '_ga_Q5HVZK168H': 'GS2.1.s1752514811$o2$g1$t1752514900$j57$l0$h0',
        'aws-waf-token': '7410d63c-cc22-4642-8563-e0d0e2738959:BQoAqEqAINsuAAAA:7Z5tX16/G0wRLhrROmSckRcxC7xyYlasiJmgOc8vzsRqlkogqBY9Dcd/2m+45PHfz9NnhF41Lir5I4nj2s7ncPvwoxl5oISwygfFiuo7r1M3ro6GBbF7gDfWFgMYkeUv5u52IaPjpIdKufwNtFIZNUNsdMQWPRNPVdKyDEl53nnUvc5ARKm7ecyt+wuvskZuIi+iAGFp55UzcCXOq54m+OAysNyRjRhz1vJscSuWp/00mpZ4GHRA2pjEBhU12jQo',
        '_ga_M4L1KRPWXE': 'GS2.1.s1752517472$o1$g1$t1752517489$j43$l0$h0',
        '_ga_1KBHG37G8W': 'GS2.1.s1752514821$o3$g1$t1752517490$j60$l0$h0',
        '_ga_F4Q7EX1K95': 'GS2.1.s1752514456$o4$g1$t1752522329$j55$l0$h0',
        '_ga_CSLL4ZEK4L': 'GS2.1.s1752514456$o4$g1$t1752522329$j55$l0$h0',
    }
    detail_headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json; charset=UTF-8',
        'priority': 'u=1, i',
        'referer': 'https://ppubs.uspto.gov/pubwebapp/',
        'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
        'x-access-token': 'eyJzdWIiOiI5MmVmNjRhMS1kMjQwLTQxOGUtOWY2Mi03ZTVlMzAzM2Q0NGQiLCJ2ZXIiOiJhNzUzYTZiYy1hZGM5LTQ5MWYtOGNkYi0yOTVmZjE5ZDE4OTIiLCJleHAiOjB9',
        'x-requested-with': 'XMLHttpRequest',
        # 'cookie': '_ga=GA1.1.1490333756.1752502650; QSI_SI_7WgrKZZwMjtuFh4_intercept=true; _ga_CD30TTEK1F=GS2.1.s1752514458$o5$g0$t1752514458$j60$l0$h0; _ga_Q5HVZK168H=GS2.1.s1752514811$o2$g1$t1752514900$j57$l0$h0; aws-waf-token=7410d63c-cc22-4642-8563-e0d0e2738959:BQoAqEqAINsuAAAA:7Z5tX16/G0wRLhrROmSckRcxC7xyYlasiJmgOc8vzsRqlkogqBY9Dcd/2m+45PHfz9NnhF41Lir5I4nj2s7ncPvwoxl5oISwygfFiuo7r1M3ro6GBbF7gDfWFgMYkeUv5u52IaPjpIdKufwNtFIZNUNsdMQWPRNPVdKyDEl53nnUvc5ARKm7ecyt+wuvskZuIi+iAGFp55UzcCXOq54m+OAysNyRjRhz1vJscSuWp/00mpZ4GHRA2pjEBhU12jQo; _ga_M4L1KRPWXE=GS2.1.s1752517472$o1$g1$t1752517489$j43$l0$h0; _ga_1KBHG37G8W=GS2.1.s1752514821$o3$g1$t1752517490$j60$l0$h0; _ga_F4Q7EX1K95=GS2.1.s1752514456$o4$g1$t1752522329$j55$l0$h0; _ga_CSLL4ZEK4L=GS2.1.s1752514456$o4$g1$t1752522329$j55$l0$h0',
    }
    params = {
        'queryId': '87342637',
        'source': 'US-PGPUB',
        'includeSections': 'true',
        'uniqueId': '',
    }
    response = requests.get(detail_url, params=params, cookies=cookies, headers=detail_headers)
    if response.status_code == 200:
        print(f'{response}')
        return response.json()
    else:
        print(f"❌ Failed for {doc_id}: {response.status_code}")
        return None

# --- STEP 3: DISPLAY RESULTS ---
print("\n📑 Extracted Patent Details:\n" + "-" * 100)

for doc_id in top_100_ids:
    result = fetch_patent_details(doc_id)
    if not result:
        continue

    patent_number = result.get("documentId", "")
    app_number = result.get("applicationNumber", "N/A")
    title = result.get("inventionTitle", "N/A")
    abstract = result.get("abstractHtml", "").replace("<br />", "").strip()

    filing_dates = result.get("applicationFilingDate", [])
    filing_date = filing_dates[0][:10] if filing_dates else "N/A"

    inventors = result.get("inventorsName", [])
    inventor_names = "; ".join(inventors) if inventors else "N/A"

    claims_html = result.get("claimsHtml", 0)

    print(f"Patent Number   : {patent_number}")
    print(f"Application No. : {app_number}")
    print(f"Title           : {title}")
    print(f"Abstract        : {abstract}")
    print(f"All Claims     : {claims_html}")
    print(f"Filing Date     : {filing_date}")
    print(f"Inventors       : {inventor_names}")
    print("-" * 100)
    
    time.sleep(1)  # Be polite to the server
