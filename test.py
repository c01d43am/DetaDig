import requests
from bs4 import BeautifulSoup
import re

def get_emails_from_website(url):
    # Send an HTTP request to the website
    response = requests.get(url)
    
    # Check if request is successful
    if response.status_code != 200:
        print(f"Failed to retrieve the website: {url}")
        return []

    # Parse the page content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract all text from the page
    page_text = soup.get_text()

    # Regular expression pattern to find email addresses
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    
    # Find all matches
    emails = re.findall(email_pattern, page_text)
    
    # Return unique emails
    return set(emails)

# Example usage
url = "https://bni-chennainorth.in/chennai-north-bravo/en-IN/index"  # Replace with the website URL
emails = get_emails_from_website(url)

if emails:
    print(f"Found emails: {', '.join(emails)}")
else:
    print("No emails found on this website.")
