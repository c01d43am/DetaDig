import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def is_valid_address(address):
    common_suffixes = ["Street", "St", "Avenue", "Ave", "Boulevard", "Blvd", "Road", "Rd", "Lane", "Ln", "Drive", "Dr", "Court", "Ct", "Way", "Place", "Pl"]
    return any(suffix in address for suffix in common_suffixes)

def extract_addresses(url, visited=set()):
    if url in visited:
        return set()
    
    visited.add(url)
    response = requests.get(url)
    if response.status_code != 200:
        return set()
    
    soup = BeautifulSoup(response.text, 'html.parser')
    page_text = soup.get_text()
    
    address_pattern = r'\d{1,5}\s\w+(?:\s\w+)*\s(?:Street|St|Avenue|Ave|Boulevard|Blvd|Road|Rd|Lane|Ln|Drive|Dr|Court|Ct|Way|Place|Pl)'
    addresses = set(filter(is_valid_address, re.findall(address_pattern, page_text)))
    
    for link in soup.find_all('a', href=True):
        next_url = urljoin(url, link['href'])
        if urlparse(next_url).netloc == urlparse(url).netloc:
            addresses.update(extract_addresses(next_url, visited))
    
    return addresses if addresses else {"No addresses found"}
