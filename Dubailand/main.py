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
    "developers",
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

take = 10000
P_FROM_DATE = "03/01/2026"
P_TO_DATE = yesterday.strftime("%m/%d/%Y")

def get_payload(endpoint, skip):
    """Har endpoint ka alag payload return karta hai"""
    payloads = {
        "transactions": {
            'P_AREA_ID': '', 'P_FROM_DATE': P_FROM_DATE, 'P_GROUP_ID': '',
            'P_IS_FREE_HOLD': '', 'P_IS_OFFPLAN': '', 'P_PROP_TYPE_ID': '',
            'P_SKIP': str(skip), 'P_SORT': 'TRANSACTION_NUMBER_ASC',
            'P_TAKE': str(take), 'P_TO_DATE': P_TO_DATE, 'P_USAGE_ID': '',
        },
        "rents": {
            'P_AREA_ID': '', 'P_DATE_TYPE': '0', 'P_FROM_DATE': P_FROM_DATE,
            'P_IS_FREE_HOLD': '', 'P_PROP_TYPE_ID': '', 'P_SKIP': str(skip),
            'P_SORT': 'REGISTRATION_DATE_ASC', 'P_TAKE': str(take),
            'P_TO_DATE': P_TO_DATE, 'P_USAGE_ID': '', 'P_VERSION': '',
        },
        "projects": {
            'P_AREA_ID': '', 'P_DATE_TYPE': '1', 'P_FROM_DATE': P_FROM_DATE,
            'P_PRJ_STATUS': '', 'P_PRJ_TYPE_ID': '', 'P_SKIP': str(skip),
            'P_SORT': 'PROJECT_NUMBER_ASC', 'P_TAKE': str(take),
            'P_TO_DATE': P_TO_DATE, 'P_ZONE_ID': '',
        },
        "valuations": {
            'P_AREA_ID': '', 'P_FROM_DATE': P_FROM_DATE, 'P_PROP_TYPE_ID': '',
            'P_SKIP': str(skip), 'P_SORT': 'PROPERTY_TOTAL_VALUE_ASC',
            'P_TAKE': str(take), 'P_TO_DATE': P_TO_DATE,
        },
        "lands": {
            'P_AREA_ID': '', 'P_IS_FREE_HOLD': '', 'P_LAND_TYPE_ID': '',
            'P_MASTER_PROJECT': '', 'P_PROJECT': '', 'P_PROP_SB_TYPE_ID': '',
            'P_SKIP': str(skip), 'P_SORT': 'LAND_TYPE_EN_ASC',
            'P_TAKE': str(take), 'P_ZONE_ID': '',
        },
        "buildings": {
            'P_AREA_ID': '', 'P_FROM_DATE': P_FROM_DATE, 'P_IS_FREE_HOLD': '',
            'P_IS_LEASE_HOLD': '', 'P_IS_OFFPLAN': '', 'P_SKIP': str(skip),
            'P_SORT': 'PROP_SUB_TYPE_EN_ASC', 'P_TAKE': str(take),
            'P_TO_DATE': P_TO_DATE, 'P_ZONE_ID': '',
        },
        "units": {
            'P_IS_OFFPLAN': '', 'P_IS_FREE_HOLD': '1', 'P_IS_LEASE_HOLD': '',
            'P_AREA_ID': '', 'P_ZONE_ID': '', 'P_TAKE': str(take),
            'P_SKIP': str(skip), 'P_SORT': 'UNIT_NUMBER_ASC',
        },
        "brokers": {
            "P_GENDER": "", "P_SKIP": str(skip),
            "P_SORT": "BROKER_NUMBER_ASC", "P_TAKE": str(take),
        },
        "developers": {
            'P_FROM_DATE': P_FROM_DATE, 'P_NAME': '', 'P_SKIP': str(skip),
            'P_SORT': 'DEVELOPER_NUMBER_ASC', 'P_TAKE': str(take),
            'P_TO_DATE': P_TO_DATE,
        },
    }
    return payloads[endpoint]

# ================= MAIN LOOP =================
for endpoint in endpoints:
    print(f"Starting endpoint: {endpoint.upper()}")
    
    all_rows = []
    skip = 0

    while True:
        payload = get_payload(endpoint, skip)

        try:
            conn.request(
                'POST',
                f'/open-data/{endpoint}',
                body=json.dumps(payload),
                headers=headers
            )
            response = conn.getresponse()

            # Status check
            if response.status != 200:
                print(f"Error: {response.status} - {response.reason}")
                break

            data = json.loads(response.read().decode('utf-8'))
            rows = data.get("response", {}).get("result", [])
            print(f"Fetched {len(rows)} rows | skip={skip}")

            if not rows:
                print(f"No more rows. Moving to next endpoint.")
                break

            all_rows.extend(rows)
            skip += take

        except Exception as e:
            print(f"Exception on {endpoint}: {e}")
            # Connection reset karke dobara try
            conn = http.client.HTTPSConnection('gateway.dubailand.gov.ae')
            break

    # ---------- CSV ----------
    if all_rows:
        filename = f"dubailand_{endpoint}_all.csv"
        fieldnames = sorted({k for row in all_rows for k in row.keys()})

        with open(filename, "w", newline="", encoding="utf-8-sig") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(all_rows)

        print(f"Saved: {filename} | Total rows: {len(all_rows)}")
    else:
        print(f"No data found for: {endpoint}")

print("ALL ENDPOINTS COMPLETE")