import requests
from bs4 import BeautifulSoup

def extract_internal_links(url):
    response = requests.get(url)
    if response.status_code != 200:
        return "Failed to retrieve website"
    
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a', href=True)
    
    internal_links = [link['href'] for link in links if link['href'].startswith('/') or link['href'].startswith(url)]
    
    return internal_links if internal_links else "No internal links found"
