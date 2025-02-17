import re
import requests
from bs4 import BeautifulSoup

def extract_phone_numbers(url):
    response = requests.get(url)
    if response.status_code != 200:
        return "Failed to retrieve website"
    
    soup = BeautifulSoup(response.text, 'html.parser')
    page_text = soup.get_text()
    
    phone_pattern = r'\(?\+?[0-9]*\)?[0-9_\- \(\)]*'
    phone_numbers = set(re.findall(phone_pattern, page_text))
    
    return phone_numbers if phone_numbers else "No phone numbers found"
