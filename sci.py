import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import certifi

os.environ['REQUESTS_CA_BUNDLE'] = certifi.where()

# Now try to load the HTML table again
df = pd.read_html('https://example.com/data.html')
login_url = 'https://login.i.ezproxy.nypl.org/login'  # Replace with the actual login URL
base_url = 'https://www-mergentintellect-com.i.ezproxy.nypl.org/index.php/advancesearch/runAdvanceSearch/refine/sales/1'    # Replace with the actual base URL

login_payload = {
    'username': 'sks2601',
    'password': 'Sahil@2601'
}
data = []
session = requests.Session()
response = session.post(login_url, data=login_payload, verify =False)

if response.status_code == 200:
    print('Login successful!')
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        df = pd.read_html(base_url.text)
        print(df[1])
            
    # for i in range(1, 10):  
    #     url = f'{base_url}{i}'  
        
    #     response = session.get(url)
        
    #     if response.status_code == 200:
#             soup = BeautifulSoup(response.content, 'html.parser')

#             title_tr = soup.find('tr',)
#             title = title_tr.get_text(strip=True) if title_tr else 'N/A'

#             company_name = soup.find('th', string ="Company Name").find_next('th').get_text(strip=True) if soup.find('th', string="Company Name") else 'N/A'
            
#             # Extract the location
#             location = soup.find('th', class_='sorttable', sortfield='PHYSICALSTATE').find_next('th').get_text(strip=True) if soup.find('th', class_='sorttable', sortfield='PHYSICALSTATE') else 'N/A'
            
#             # Extract the location type
#             location_type = soup.find('th', class_='sorttable', sortfield='LOCATIONTYPECODE').find_next('th').get_text(strip=True) if soup.find('th', class_='sorttable', sortfield='LOCATIONTYPECODE') else 'N/A'
            
#             # Extract the sales
#             sales = soup.find('div', class_='sort_header').find_next('div').get_text(strip=True) if soup.find('div', class_='sort_header') else 'N/A'
            
#             # Extract the SIC code
#             sic = soup.find('th', class_='sorttable', sortfield='SICCODE').find_next('td').get_text(strip=True) if soup.find('th', class_='sorttable', sortfield='SICCODE') else 'N/A'
            
#             # Extract the URL
#             company_url = soup.find('th', string="URL").find_next('td').find('a')['href'] if soup.find('th', string="URL") and soup.find('th', text="URL").find_next('td').find('a') else 'N/A'
            
#             # Extract the phone number
#             phone_number = soup.find('th', string="Phone Number").find_next('td').get_text(strip=True) if soup.find('th', string="Phone Number") else 'N/A'
#             data.append({
#                 'Company Name': company_name,
#                 'Location': location,
#                 'Location Type': location_type,
#                 'Sales': sales,
#                 'SIC': sic,
#                 'URL': company_url,
#                 'Phone Number': phone_number
#             })
            
#             # code for data into vba file
#             df = pd.DataFrame(data)
#             df.to_excel('scraped_data.xlsx', index=False)
#         else:
#             print(f'Failed to retrieve {url}, status code: {response.status_code}')
# else:
#     print('Login failed!')



# print("Data saved to 'scraped_data.xlsx'")
# # close the session
# session.close()


#             # print(f'Page {i} title: {title}') 
            
#             # Extract the desired information
#             # company_name = soup.find('th', class_='sorttable').get_text() if soup.find('th', class_='sorttable') else 'N/A'
#             # location = soup.find('span', class_='location').get_text() if soup.find('span', class_='location') else 'N/A'
#             # location_type = soup.find('span', class_='location-type').get_text() if soup.find('span', class_='location-type') else 'N/A'
#             # sales = soup.find('span', class_='sales').get_text() if soup.find('span', class_='sales') else 'N/A'
#             # sic = soup.find('span', class_='sic').get_text() if soup.find('span', class_='sic') else 'N/A'
#             # company_url = soup.find('a', class_='company-url').get('href') if soup.find('a', class_='company-url') else 'N/A'
#             # phone_number = soup.find('span', class_='phone-number').get_text() if soup.find('span', class_='phone-number') else 'N/A'