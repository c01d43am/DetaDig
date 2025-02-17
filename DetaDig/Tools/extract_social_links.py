import requests
from bs4 import BeautifulSoup

def extract_social_links(url):
    response = requests.get(url)
    if response.status_code != 200:
        return "Failed to retrieve website"
    
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a', href=True)
    
    social_platforms = ['facebook', 'twitter', 'linkedin', 'instagram', 'youtube', 'pinterest']
    social_links = [link['href'] for link in links if any(platform in link['href'] for platform in social_platforms)]
    
    return social_links if social_links else "No social links found"
