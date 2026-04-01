import http.client
import json
import csv
from datetime import datetime, timedelta

# ================= ENDPOINT LIST =================
endpoints = [
    "transactions",
    "rents",
    "projects",
    "valuations",
    "lands",
    "buildings",
    "units",
    "brokers",
    "developers"
]

# ---------- CONNECTION ----------
yesterday = datetime.today() - timedelta(days=1)
conn = http.client.HTTPSConnection('gateway.dubailand.gov.ae')

headers = {
    'accept': 'application/json, */*',
    'content-type': 'application/json; charset=UTF-8',
    'origin': 'https://dubailand.gov.ae',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Mobile Safari/537.36',
    'consumer-id': 'gkb3WvEG0rY9eilwXC0P2pTz8UzvLj9F',
}

all_rows = []
skip = 0
take = 10000   # change this as needed
P_FROM_DATE = "03/01/2026"   # change this as needed
P_TO_DATE = yesterday.strftime("%d/%m/%Y")   # change this as needed

while True:
    transactions_payload = {
        'P_FROM_DATE': P_FROM_DATE,
        'P_TO_DATE': P_TO_DATE,
        'P_GROUP_ID': '',
        'P_IS_OFFPLAN': '',
        'P_IS_FREE_HOLD': '',
        'P_AREA_ID': '',
        'P_USAGE_ID': '',
        'P_PROP_TYPE_ID': '',
        'P_TAKE': str(take),
        'P_SKIP': str(skip),
        'P_SORT': 'TRANSACTION_NUMBER_ASC',
    }

    rents_payload = {
        'P_AREA_ID': '',
        'P_DATE_TYPE': '0',
        'P_FROM_DATE': P_FROM_DATE,
        'P_IS_FREE_HOLD': '',
        'P_PROP_TYPE_ID': '',
        'P_SKIP': str(take),
        'P_SORT': 'REGISTRATION_DATE_ASC',
        'P_TAKE': str(skip),
        'P_TO_DATE': P_TO_DATE,
        'P_USAGE_ID': '',
        'P_VERSION': '',
    }

    projects_payload = {
        'P_AREA_ID': '',
        'P_DATE_TYPE': '1',
        'P_FROM_DATE': P_FROM_DATE,
        'P_PRJ_STATUS': '',
        'P_PRJ_TYPE_ID': '',
        'P_SKIP': str(take),
        'P_SORT': 'PROJECT_NUMBER_ASC',
        'P_TAKE': str(skip),
        'P_TO_DATE': P_TO_DATE,
        'P_ZONE_ID': '',
    }

    valuations_payload = {
        'P_AREA_ID': '',
        'P_FROM_DATE': P_FROM_DATE,
        'P_PROP_TYPE_ID': '',
        'P_SKIP': str(take),
        'P_SORT': 'PROPERTY_TOTAL_VALUE_ASC',
        'P_TAKE': str(skip),
        'P_TO_DATE': P_TO_DATE,
    }

    lands_payload = {
        'P_AREA_ID': '',
        'P_IS_FREE_HOLD': '',
        'P_LAND_TYPE_ID': '',
        'P_MASTER_PROJECT': '',
        'P_PROJECT': '',
        'P_PROP_SB_TYPE_ID': '',
        'P_SKIP': str(take),
        'P_SORT': 'LAND_TYPE_EN_ASC',
        'P_TAKE': str(skip),
        'P_ZONE_ID': '',
    }

    buildings_payload = {
        'P_AREA_ID': '',
        'P_FROM_DATE': P_FROM_DATE,
        'P_IS_FREE_HOLD': '',
        'P_IS_LEASE_HOLD': '',
        'P_IS_OFFPLAN': '',
        'P_SKIP': str(take),
        'P_SORT': 'PROP_SUB_TYPE_EN_ASC',
        'P_TAKE': str(skip),
        'P_TO_DATE': P_TO_DATE,
        'P_ZONE_ID': '',
    }

    units_payload = {
        'P_IS_OFFPLAN': '',
        'P_IS_FREE_HOLD': '1',
        'P_IS_LEASE_HOLD': '',
        'P_AREA_ID': '',
        'P_ZONE_ID': '',
        'P_TAKE': str(skip),
        'P_SKIP': str(take),
        'P_SORT': 'UNIT_NUMBER_ASC',
    }

    brokers_payload = {
        "P_GENDER": "",
        "P_TAKE": "100",
        "P_SKIP": "0",
        "P_SORT": "BROKER_NUMBER_ASC"
    }

    developers_payload = {
        'P_FROM_DATE': P_FROM_DATE,
        'P_NAME': '',
        'P_SKIP': str(take),
        'P_SORT': 'DEVELOPER_NUMBER_ASC',
        'P_TAKE': str(skip),
        'P_TO_DATE': P_TO_DATE,
    }

    conn.request(
        'POST',
        f'/open-data/{endpoints[0]}',
        body=json.dumps(transactions_payload),
        headers=headers
    )

    response = conn.getresponse()
    # status check
    if response.status != 200:
        print(f"Error: {response.status} - {response.reason}")
        break

    # actual data
    data = json.loads(response.read().decode('utf-8'))
    rows = data.get("response", {}).get("result", [])
    print(f"Fetched {len(rows)} rows | skip={skip}")

    if not rows:
        break

    all_rows.extend(rows)
    skip += take

# ---------- CSV ----------
if all_rows:
    fieldnames = sorted({k for row in all_rows for k in row.keys()})

    with open("dubai_transactions_all.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_rows)

print(f"Done ✔ Total rows: {len(all_rows)}")