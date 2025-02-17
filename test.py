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
    
    # Extract title
    title = soup.title.string if soup.title else "No title"

    # Extract all meta tags
    meta_tags = soup.find_all('meta')
    meta_details = {meta.get('name', meta.get('property')): meta.get('content') for meta in meta_tags if meta.get('name') or meta.get('property')}

    # Extract all links (anchor tags)
    links = [a['href'] for a in soup.find_all('a', href=True)]
    
    # Extract all images (img tags)
    images = [img['src'] for img in soup.find_all('img', src=True)]
    
    # Extract headers (h1, h2, h3, h4, h5, h6)
    headers = {f"h{i}": [header.text for header in soup.find_all(f"h{i}")] for i in range(1, 7)}
    
    # Extract all scripts
    scripts = [script['src'] for script in soup.find_all('script', src=True)]
    
    # Extract all stylesheets
    stylesheets = [link['href'] for link in soup.find_all('link', href=True) if 'stylesheet' in link.get('rel', [])]

    # Store all extracted details in a dictionary
    website_data = {
        "Title": title,
        "Meta Tags": meta_details,
        "Links": links,
        "Images": images,
        "Headers": headers,
        "Scripts": scripts,
        "Stylesheets": stylesheets
    }
    
    return website_data

# Example usage
url = input("Enter the website URL to extract data: ")
if not url.startswith(('http://', 'https://')):
    url = 'https://' + url  # Add default scheme if not provided

data = extract_website_data(url)

# Display the extracted data
if data:
    print("\nWebsite Data Extracted:")
    print(f"Title: {data['Title']}")
    print(f"Meta Tags: {data['Meta Tags']}")
    print(f"Links: {data['Links'][:5]}...")  # Limiting the list size for display
    print(f"Images: {data['Images'][:5]}...")  # Limiting the list size for display
    print(f"Headers: {data['Headers']}")
    print(f"Scripts: {data['Scripts'][:5]}...")  # Limiting the list size for display
    print(f"Stylesheets: {data['Stylesheets'][:5]}...")  # Limiting the list size for display
else:
    print("No data found.")
