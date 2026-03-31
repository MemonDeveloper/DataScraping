import requests
import pandas as pd
import json
import time
from bs4 import BeautifulSoup

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
BASE_URL = "https://www.nossaman.com"

# Just one Profile Test
# PROFILE_URL = "https://www.nossaman.com/professionals-john-flynn"

def extract_data_from_profile(profile_url):
    print(f"  Extracting: {profile_url}")

    try:
        response = requests.get(profile_url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')

        json_data = {}
        script_tag = soup.find('script', {'type': 'application/ld+json'})

        if script_tag:
            try:
                json_data = json.loads(script_tag.string)
            except Exception as e:
                print("    JSON parse error")

        # Name
        given_name = ""
        middle_name = ""
        family_name = ""

        given = soup.find('span', {'itemprop': 'givenName'})
        if given:
            given_name = given.get_text(strip=True)

        middle = soup.find('span', {'itemprop': 'additionalName'})
        if middle:
            middle_name = middle.get_text(strip=True)

        family = soup.find('span', {'itemprop': 'familyName'})
        if family:
            family_name = family.get_text(strip=True)

        name = " ".join(filter(None, [given_name, middle_name, family_name]))
        
        # Title
        title = ""
        title_tag = soup.find('div', {'id': 'bioTitle'})
        if title_tag:
            title = title_tag.get_text(strip=True)

        # Phone/Mobile/Fax
        phone = ""
        mobile = ""
        fax = ""

        contact_list = soup.find("ul", {"id": "bioContact"})
        if contact_list:
            phones = contact_list.select("a[href^='tel:']")

            if len(phones) > 0:
                phone = phones[0].get_text(strip=True)

            if len(phones) > 1:
                mobile = phones[1].get_text(strip=True)

            # fax if exists
            fax_tag = contact_list.find("span", {"itemprop": "faxNumber"})
            if fax_tag:
                fax = fax_tag.get_text(strip=True)

        # Social / Extras
        linkedin = ""
        vcard = ""
        pdf = ""

        accessories = soup.find('ul', {'id': 'bioAccessories'})
        if accessories:
            for li in accessories.find_all('li'):
                a = li.find('a')
                if not a:
                    continue

                href = a.get('href', '')
                text = a.get_text(strip=True)

                if "linkedin" in href:
                    linkedin = href
                elif "vcf" in href:
                    vcard = href
                elif "pdf" in href:
                    pdf = href

        # Image
        image = ""
        if json_data.get('image'):
            image = json_data.get('image')
        else:
            og_image = soup.find('meta', property='og:image')
            if og_image and og_image.get('content'):
                image = og_image['content'].strip()

        # Office
        office = ""
        office_tag = soup.find('div', {'id': 'bioOffice'})
        if office_tag:
            office = office_tag.get_text(" ", strip=True)

        # Email
        email = ""
        email_tag = soup.find('div', {'id': 'bioEmail'})
        if email_tag and email_tag.a:
            email = email_tag.a.get_text(strip=True)

        # Practices
        practice = ""
        practice_section = soup.find('div', {'id': 'bio_area'})
        if practice_section:
            practices = [li.get_text(strip=True) for li in practice_section.find_all('li')]
            practice = ",\n".join(practices)

        # Industries
        industry = ""
        industry_section = soup.find('div', {'id': 'bio_industry'})
        if industry_section:
            industrys = [li.get_text(strip=True) for li in industry_section.find_all('li')]
            industry = ",\n".join(industrys)

        # Education
        education = ""
        education_section = soup.find('div', {'id': 'bio_school'})
        if education_section:
            educations = [li.get_text(strip=True) for li in education_section.find_all('li')]
            education = ",\n".join(educations)

        # Admissions
        admission = ""
        admission_section = soup.find('div', {'id': 'bio_barcourt'})
        if admission_section:
            admissions = [li.get_text(strip=True) for li in admission_section.find_all('li')]
            admission = ",\n".join(admissions)

        # Overview
        overview = ""
        overview_section = soup.find('div', {'id': 'bio_content'})
        if overview_section:
            overview = "\n".join([p.get_text(strip=True) for p in overview_section.find_all('p')])

        # Experience
        experience = ""
        exp_section = soup.find('div', {'id': 'bio_expcontent'})
        if exp_section:
            experience = "\n".join([p.get_text(strip=True) for p in exp_section.find_all('p')])

        # Native American Affairs/Federal Government Experience/Other Experience
        other_experience = ""
        other_experience_section = soup.find('div', {'id': 'bio_flextabcontent1'})
        if other_experience_section:
            other_experience = "\n".join([p.get_text(strip=True) for p in other_experience_section.find_all('p')])

        # Honor
        honors = []
        honors_section = soup.find("div", {"id": "bio_honors"})
        if honors_section:
            honors = [el.get_text(" ", strip=True) for el in honors_section.find_all(["p", "li"])]

        # Publication/Events/News/Podcasts
        def extract_list(section_id):
            section = soup.find("div", {"id": section_id})
            if not section:
                return []
            return [li.get_text(" ", strip=True) for li in section.find_all("li")]

        publications = extract_list("bio_publication")
        events = extract_list("bio_event")
        news = extract_list("bio_news")
        podcasts = extract_list("bio_podepisode")

        print(f"    ✓ {name}")

        return {
            'Name': name,
            'Given Name': given_name,
            'Middle Name': middle_name,
            'Family Name': family_name,
            'Title': title,
            'Office': office,
            'Email': email,
            'Phone': phone,
            'Mobile': mobile,
            'Fax': fax,
            'LinkedIn': linkedin,
            'Image': image,
            'Practice': practice,
            'Industry': industry,
            'Education': education,
            'Admission': admission,
            'Overview': overview,
            'Experience': experience,
            'Other Experience': other_experience,
            'Publications': "\n".join(publications),
            'Events': "\n".join(events),
            'News': "\n".join(news),
            'Podcasts': "\n".join(podcasts),
            'Honors': "\n".join(honors),
        }

    except Exception as e:
        print(f"    ✗ Error: {e}")
        return None

def get_profile_links():
    print("Fetching profile links...")

    url = "https://www.nossaman.com/professionals?do_item_search=1"

    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')

        profile_links = []
        results_list = soup.find_all('a', href=True)

        for link in results_list:
            href = link['href']

            if "professionals-" in href:
                full_link = BASE_URL + "/" + href.strip("/")
                if full_link not in profile_links:
                    profile_links.append(full_link)

        print(f"Found {len(profile_links)} profiles")
        return profile_links

    except Exception as e:
        print(f"Error fetching links: {e}")
        return []

def main():
    print("NOSSAMAN SCRAPER STARTED")

    profile_links = get_profile_links()

    if not profile_links:
        print("No profiles found!")
        return

    data_list = []

    for i, link in enumerate(profile_links, 1):
        print(f"\n[{i}/{len(profile_links)}] Processing...")

        data = extract_data_from_profile(link)

        if data and data['Name'] and data['Title']:
            data['S.No'] = i
            data_list.append(data)

        # polite delay (avoid blocking)
        time.sleep(1)

    print("\nCreating DataFrame...")

    df = pd.DataFrame(data_list)

    if not df.empty:
        expected_cols = [
            'Name',
            'Given Name',
            'Middle Name',
            'Family Name',
            'Title',
            'Office',
            'Email',
            'Phone',
            'Mobile',
            'Fax',
            'LinkedIn',
            'Image',
            'Practice',
            'Industry',
            'Education',
            'Admission',
            'Overview',
            'Experience',
            'Other Experience',
            'Publications',
            'Events',
            'News',
            'Podcasts',
            'Honors'
        ]

        # ensure all columns exist (avoid KeyError)
        for col in expected_cols:
            if col not in df.columns:
                df[col] = ""

        df = df[expected_cols]
        file_name = "professionals_data.csv"
        df.to_csv(file_name, index=False)

        print(f"\n✅ Saved to {file_name}")
        print(f"Total records: {len(df)}")
    else:
        print("No data collected!")

    print("\nDONE ✅")

# Just one Profile Test
# def main():
#     print("SINGLE PROFILE SCRAPER STARTED")

#     data = extract_data_from_profile(PROFILE_URL)

#     if data:
#         df = pd.DataFrame([data])

#         file_name = "single_professional.csv"
#         df.to_csv(file_name, index=False)

#         print(f"\nSaved: {file_name}")
#     else:
#         print("No data found!")

if __name__ == "__main__":
    main()