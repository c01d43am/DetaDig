import requests
from bs4 import BeautifulSoup

def extract_website_data(url):
    # Send an HTTP request to the website
    response = requests.get(url)
    
    # Check if request is successful
    if response.status_code != 200:
        print(f"Failed to retrieve the website: {url}")
        return {}

    # Parse the page content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract the title of the website
    title = soup.title.string if soup.title else "No title found"

    # Extract all links on the page
    links = [a.get('href') for a in soup.find_all('a', href=True)]

    # Extract all headings (h1, h2, h3, etc.)
    headings = {}
    for i in range(1, 7):  # Extract h1 to h6 tags
        headings[f'h{i}'] = [h.get_text().strip() for h in soup.find_all(f'h{i}')]

    # Return extracted data
    return {
        "title": title,
        "links": links,
        "headings": headings
    }

# Ask user to input the URL
url = input("Enter the website URL to extract data: ")

data = extract_website_data(url)

# Print the extracted data
if data:
    print(f"Website Title: {data['title']}")
    print("\nLinks found on the website:")
    for link in data['links']:
        print(link)
    print("\nHeadings found on the website:")
    for heading, values in data['headings'].items():
        print(f"{heading}: {', '.join(values)}")
else:
    print("No data extracted from the website.")
