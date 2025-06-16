import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract_data_from_profile(profile_url):
    response = requests.get(profile_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract Name
    name_tag = soup.find('h1', {'id': 'pageTitle'})
    if name_tag:
        name_parts = name_tag.find_all('span')
        name = ' '.join(part.get_text() for part in name_parts).strip()
    else:
        name = ""

    # Extract Title
    title = soup.find('div', {'id': 'bioTitle'}).get_text(strip=True) if soup.find('div', {'id': 'bioTitle'}) else ""
    
    # Extract Office
    office = soup.find('div', {'id': 'bioOffice'}).get_text(strip=True) if soup.find('div', {'id': 'bioOffice'}) else ""
    
    # Extract Email
    email = soup.find('div', {'id': 'bioEmail'}).a.get_text(strip=True) if soup.find('div', {'id': 'bioEmail'}) and soup.find('div', {'id': 'bioEmail'}).a else ""
    
    # Extract Phone
    phone = soup.find('ul', {'id': 'bioContact'}).find('a', {'itemprop': 'telephone'}).get_text(strip=True) if soup.find('ul', {'id': 'bioContact'}) else ""
    
    # Extract Mobile
    mobile = None
    contact_list = soup.find('ul', {'id': 'bioContact'})
    if contact_list:
        mobile_tag = contact_list.find_all('li')
        for item in mobile_tag:
            text = item.get_text(strip=True)
            # Adjust this condition based on the actual content
            if 'Mobile:' in text or 'M:' in text:  # Use multiple keywords if necessary
                mobile = item.find('a', {'itemprop': 'telephone'}).get_text(strip=True) if item.find('a', {'itemprop': 'telephone'}) else ""
                break

    # Extract Fax (Tax)
    tax = ""
    if contact_list:
        fax_number_tag = contact_list.find('span', {'itemprop': 'faxNumber'})
        tax = fax_number_tag.get_text(strip=True) if fax_number_tag else ""
    
    # Extract Service (Practices)
    service = ""
    service_section = soup.find('div', {'id': 'bio_area', 'class': 'itemSection'})
    if service_section:
        service_list = service_section.find('ul', {'class': 'results_list'})
        if service_list:
            services = [li.get_text(strip=True) for li in service_list.find_all('li')]
            service = ', '.join(services)
    
    return {
        'Name': name,
        'Title': title,
        'Service': service,  # Insert extracted service here
        'Office': office,
        'Email': email,
        'Phone': phone,
        'Tax': tax,
        'Mobile': mobile if mobile else "",
    }

def get_profile_links(search_url):
    response = requests.get(search_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    profile_links = []
    results_list = soup.find('ul', {'class': 'results_list'})
    if results_list:
        for li in results_list.find_all('li'):
            link = li.find('a')['href']
            full_link = f"https://www.nossaman.com/{link}"
            profile_links.append(full_link)
    return profile_links

def main():
    search_url = 'https://www.nossaman.com/professionals-directory#form-search-results'
    
    profile_links = get_profile_links(search_url)
    data_list = []

    for index, link in enumerate(profile_links):
        profile_data = extract_data_from_profile(link)
        
        # Only append to the list if Name and Title are not empty
        if profile_data['Name'] and profile_data['Title']:
            profile_data['S.No'] = index
            data_list.append(profile_data)

    df = pd.DataFrame(data_list)
    df = df[['S.No', 'Name', 'Title', 'Service', 'Office', 'Email', 'Phone', 'Tax', 'Mobile']]
    df.to_excel('professionals_data.xlsx', index=False)

if __name__ == "__main__":
    main()
