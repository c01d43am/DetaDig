import re
import requests
from bs4 import BeautifulSoup

def extract_product_pricing(url):
    response = requests.get(url)
    if response.status_code != 200:
        return "Failed to retrieve website"
    
    soup = BeautifulSoup(response.text, 'html.parser')
    page_text = soup.get_text()
    
    price_pattern = r'[$₹]?\d{1,3}(?:,\d{3})*(?:\.\d{2})?'
    prices = set(re.findall(price_pattern, page_text))
    
    return prices if prices else "No product prices found"
