import requests
import csv
import time
import re
import os
import sys
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE_RESULTS_URL = "https://www.iecaonline.com/independent-educational-consultant-search/results/"
SORT_PARAM       = "?_directory_sort=first_name_asc"
OUTPUT_DIR       = os.path.dirname(os.path.abspath(__file__))
CSV_FILE         = os.path.join(OUTPUT_DIR, "ieca_consultants.csv")
IMAGE_FOLDER     = os.path.join(OUTPUT_DIR, "consultant_images")
DELAY_BETWEEN_PAGES       = 1.5   # seconds between listing pages
DELAY_BETWEEN_CONSULTANTS = 1.0   # seconds between profile pages
DELAY_BETWEEN_IMAGES      = 0.3   # seconds between image downloads

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

def get(url, timeout=20):
    """Simple GET with retries."""
    for attempt in range(3):
        try:
            r = requests.get(url, headers=HEADERS, timeout=timeout)
            r.raise_for_status()
            return r
        except Exception as e:
            if attempt == 2:
                raise
            print(f"Retry {attempt+1} for {url}: {e}")
            time.sleep(2)

def text(el):
    return el.get_text(strip=True) if el else 'N/A'

def get_all_consultant_urls():
    consultant_urls = []
    page = 1

    while True:
        if page == 1:
            url = BASE_RESULTS_URL + SORT_PARAM
        else:
            url = f"{BASE_RESULTS_URL}page/{page}/{SORT_PARAM}"

        print(f"Fetching listing page {page}: {url}")
        try:
            r = get(url)
        except Exception as e:
            print(f"Could not fetch page {page}: {e} — stopping pagination.")
            break

        soup = BeautifulSoup(r.content, 'html.parser')

        # Collect consultant links on this page
        found_on_page = []
        for link in soup.find_all('a', href=True):
            href = link['href']
            if '/consultant/' in href and href.rstrip('/') != '/consultant':
                full = urljoin(BASE_RESULTS_URL, href)
                if full not in consultant_urls and full not in found_on_page:
                    found_on_page.append(full)

        if not found_on_page:
            print(f"No consultants on page {page} — pagination complete.")
            break

        print(f"Found {len(found_on_page)} profiles on page {page}")
        consultant_urls.extend(found_on_page)

        # Check whether a "Next" link exists
        next_link = soup.find('a', string=re.compile(r'Next', re.IGNORECASE))
        if not next_link:
            print("  No 'Next' link — last page reached.")
            break

        page += 1
        time.sleep(DELAY_BETWEEN_PAGES)

    print(f"\nTotal consultant profiles found: {len(consultant_urls)}")
    return consultant_urls

def extract_consultant_fields(soup):
    consultant_data = {}

    # 1. Bold-label paragraphs inside fl-rich-text divs
    for div in soup.find_all('div', class_='fl-rich-text'):
        for p in div.find_all('p'):
            full_text = p.get_text(strip=True)
            for strong in p.find_all('strong'):
                field_name = strong.get_text(strip=True).replace(':', '').strip()
                remaining  = full_text.replace(strong.get_text(strip=True), '').strip()
                remaining  = re.sub(r'^[:\s]+', '', remaining)
                for link in p.find_all('a'):
                    href = link.get('href', '')
                    if 'tel:' in href:
                        remaining = link.get_text(strip=True)
                    elif href.startswith('http'):
                        remaining = href
                if field_name and remaining:
                    clean = field_name.replace(' ', '_').replace('&', 'and')
                    consultant_data[clean] = remaining

    # 2. Website button  (OUTSIDE the loop — bug fix)
    btn = soup.find('a', string=re.compile('Go to Website', re.IGNORECASE))
    if btn and btn.get('href'):
        consultant_data['Website'] = btn['href']
    else:
        wd = soup.find('div', class_='fl-module-button', attrs={'data-node': 'dmhn8xvt2ope'})
        if wd:
            lnk = wd.find('a', href=True)
            consultant_data['Website'] = lnk['href'] if lnk else 'N/A'
        else:
            consultant_data['Website'] = 'N/A'

    # 3. Location
    addr_div = soup.find('div', class_='ieca-addresses')
    if addr_div:
        parts = []
        for cls in ('address-city', 'address-state', 'address-zip', 'address-country'):
            sp = addr_div.find('span', class_=cls)
            if sp:
                parts.append(sp.get_text(strip=True))
        if parts:
            consultant_data['Location'] = ', '.join(parts)

    # 4. Areas of Consulting Expertise
    expertise = []
    exp_div = soup.find('div', class_='ieca-consulting-areas')
    if exp_div:
        h3 = exp_div.find('h3')
        if h3:
            expertise.append(h3.get_text(strip=True))
        ch = exp_div.find('div', class_='ieca-consulting-areas-children')
        if ch:
            expertise += [s.get_text(strip=True) for s in ch.find_all('span')]
    consultant_data['Areas_of_Consulting_Expertise'] = ', '.join(expertise) if expertise else 'N/A'

    # 5. Additional Advising Areas
    adv = []
    adv_div = soup.find('div', class_='fl-additional-advising-area')
    if adv_div:
        for sp in adv_div.find_all('span'):
            inner = sp.find('span')
            t = (inner if inner else sp).get_text(strip=True)
            if t:
                adv.append(t)
    consultant_data['Additional_Advising_Areas'] = ', '.join(adv) if adv else 'N/A'

    # 6. Additional Languages Spoken
    lang_div = soup.find('div', class_='fl-additional-language-spoken')
    if lang_div:
        langs = [s.get_text(strip=True) for s in lang_div.find_all('span') if s.get_text(strip=True)]
        if langs:
            consultant_data['Additional_Languages_Spoken'] = ', '.join(langs)

    # 7. Education (h3 + p inside fl-rich-text)
    for edu_div in soup.find_all('div', class_='fl-rich-text'):
        h3 = edu_div.find('h3')
        if h3:
            deg = h3.get_text(strip=True)
            p   = edu_div.find('p')
            if p and deg:
                consultant_data[deg] = p.get_text(strip=True)

    return consultant_data

def scrape_consultant_details(url):
    try:
        r    = get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        data = {}

        # Name
        h1 = soup.find('h1', class_='fl-heading')
        data['Name'] = text(h1.find('span', class_='fl-heading-text') if h1 else None)

        # Tagline
        tg = soup.find('div', class_='fl-rich-text', attrs={'data-node': 'ts74v5pzfd8x'})
        data['Tagline'] = text(tg.find('p') if tg else None)

        # Image URL
        img_col = soup.find('div', class_='fl-col', attrs={'data-node': 'pb4fkx1n9irl'})
        if img_col:
            img = img_col.find('img')
            data['Image_URL'] = img['src'] if img and img.get('src') else 'N/A'
        else:
            mob = soup.find('div', class_='fl-module-photo fl-node-lsrxzvf486i7')
            if mob:
                img = mob.find('img')
                data['Image_URL'] = img['src'] if img and img.get('src') else 'N/A'
            else:
                data['Image_URL'] = 'N/A'

        # Bio
        bio_div = soup.find('div', class_='fl-module-fl-post-content')
        data['Bio'] = text(bio_div.find('p') if bio_div else None)

        # All dynamic fields
        data.update(extract_consultant_fields(soup))

        # Profile URL
        data['Profile_URL'] = url

        # Sanitise
        data = {k: (v if v else 'N/A') for k, v in data.items()}
        return data

    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return None

def save_to_csv(records):
    if not records:
        print("No data to save.")
        return []

    all_keys = set()
    for r in records:
        if r:
            all_keys.update(r.keys())

    for f in ('Name', 'Tagline', 'Bio', 'Image_URL', 'Profile_URL'):
        all_keys.add(f)

    fieldnames = sorted(all_keys)

    with open(CSV_FILE, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for r in records:
            if r:
                writer.writerow(r)

    print(f"CSV saved to {CSV_FILE}  ({len(fieldnames)} columns, {len(records)} rows)")
    return fieldnames

def download_images(records):
    if not records:
        return

    os.makedirs(IMAGE_FOLDER, exist_ok=True)
    for data in records:
        if not data or not data.get('Image_URL') or data['Image_URL'] == 'N/A':
            continue
        try:
            name    = data.get('Name', 'unknown').replace(' ', '_').replace('/', '_').replace('\\', '_')
            img_url = data['Image_URL']
            ext     = img_url.split('.')[-1].split('?')[0].lower()
            if ext not in ('jpg', 'jpeg', 'png', 'gif', 'webp', 'bmp'):
                ext = 'jpg'
            filepath = os.path.join(IMAGE_FOLDER, f"{name}.{ext}")
            if not os.path.exists(filepath):
                ir = requests.get(img_url, headers=HEADERS, timeout=15)
                ir.raise_for_status()
                with open(filepath, 'wb') as f:
                    f.write(ir.content)
                print(f"Downloaded: {name}.{ext}")
                time.sleep(DELAY_BETWEEN_IMAGES)
            else:
                print(f"Already exists: {name}.{ext}")
        except Exception as e:
            print(f"Image error ({data.get('Name', '?')}): {e}")

def main():
    # ── Step 1: collect all profile URLs across all pages ──────────────────
    urls = get_all_consultant_urls()

    if not urls:
        print("No URLs found — check website structure or network.")
        sys.exit(1)

    # ── Step 2: scrape each profile ────────────────────────────────────────
    print(f"\n[STEP 2] Scraping {len(urls)} consultant profiles…")
    records = []
    total   = len(urls)

    for i, url in enumerate(urls, 1):
        print(f"[{i}/{total}] Scraping {url}")
        data = scrape_consultant_details(url)
        if data:
            records.append(data)
            print(f"{data.get('Name', 'Unknown')}")
        else:
            print(f"Failed")
        time.sleep(DELAY_BETWEEN_CONSULTANTS)

    # ── Step 3: save CSV ───────────────────────────────────────────────────
    print(f"\n[STEP 3] Saving CSV…")
    fieldnames = save_to_csv(records)

    # ── Step 4: download images ────────────────────────────────────────────
    print(f"\n[STEP 4] Downloading images…")
    download_images(records)

if __name__ == "__main__":
    main()