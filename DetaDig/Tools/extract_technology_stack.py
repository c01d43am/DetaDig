import requests
from bs4 import BeautifulSoup

def extract_technology_stack(url):
    response = requests.get(url)
    if response.status_code != 200:
        return "Failed to retrieve website"
    
    soup = BeautifulSoup(response.text, 'html.parser')
    tech_stack = []
    
    if 'wordpress' in soup.get_text().lower():
        tech_stack.append('WordPress')
    if 'joomla' in soup.get_text().lower():
        tech_stack.append('Joomla')
    if 'apache' in soup.get_text().lower():
        tech_stack.append('Apache Web Server')
    
    return tech_stack if tech_stack else "No technology stack info found"
