import sys
import os

# Add the tools directory to sys.path
tools_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'tools')
sys.path.append(tools_dir)

# Importing data extraction functions from the tools directory
from ..Tools.extract_emails import extract_emails
from ..Tools.extract_phone_numbers import extract_phone_numbers
from ..Tools.extract_addresses import extract_addresses
from ..Tools.extract_social_links import extract_social_links
from ..Tools.extract_product_pricing import extract_product_pricing
from ..Tools.extract_technology_stack import extract_technology_stack
from ..Tools.extract_ssl_info import ssl_menu
from ..Tools.extract_meta_tags import extract_meta_tags
from ..Tools.extract_internal_links import extract_internal_links 

def extract_data(url, choice):
    if choice == '1':
        return extract_emails(url)
    elif choice == '2':
        return extract_phone_numbers(url)
    elif choice == '3':
        return extract_addresses(url)
    elif choice == '4':
        return extract_social_links(url)
    elif choice == '5':
        return extract_product_pricing(url)
    elif choice == '6':
        return extract_technology_stack(url)
    elif choice == '7':
        return ssl_menu()
    elif choice == '8':
        return extract_meta_tags(url)
    elif choice == '9':
        return extract_internal_links(url)
    elif choice == '10':
        # Extract All Data
        all_data = {
            "Emails": extract_emails(url),
            "Phone numbers": extract_phone_numbers(url),
            "Addresses": extract_addresses(url),
            "Social media links": extract_social_links(url),
            "Product prices": extract_product_pricing(url),
            "Technology Stack": extract_technology_stack(url),
            "SSL/TLS Info": ssl_menu(url),
            "Meta Tags": extract_meta_tags(url),
            "Internal links": extract_internal_links(url)
        }
        return all_data
    else:
        return "Invalid choice"