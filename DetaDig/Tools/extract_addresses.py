import re
import requests
from bs4 import BeautifulSoup

def extract_addresses(url):
    response = requests.get(url)
    if response.status_code != 200:
        return "Failed to retrieve website"
    
    soup = BeautifulSoup(response.text, 'html.parser')
    page_text = soup.get_text()
    
    address_pattern = r'\d{1,5}\s\w+\s\w+'
    addresses = set(re.findall(address_pattern, page_text))
    
    return addresses if addresses else "No addresses found"
