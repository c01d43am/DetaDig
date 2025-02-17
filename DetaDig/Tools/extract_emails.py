import re
import requests
from bs4 import BeautifulSoup

def extract_emails(url):
    response = requests.get(url)
    if response.status_code != 200:
        return "Failed to retrieve website"
    
    soup = BeautifulSoup(response.text, 'html.parser')
    page_text = soup.get_text()
    
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = set(re.findall(email_pattern, page_text))
    
    return emails if emails else "No emails found"
