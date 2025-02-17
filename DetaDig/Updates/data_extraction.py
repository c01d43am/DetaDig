import importlib.util
import os

# Function to dynamically import a module
def dynamic_import(module_name, module_path):
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

# Determine the path to the tools directory
tools_dir = os.path.join(os.path.dirname(__file__), '..', 'tools')

# Importing data extraction functions from the tools directory
extract_emails = dynamic_import('extract_emails', os.path.join(tools_dir, 'extract_emails.py')).extract_emails
extract_phone_numbers = dynamic_import('extract_phone_numbers', os.path.join(tools_dir, 'extract_phone_numbers.py')).extract_phone_numbers
extract_addresses = dynamic_import('extract_addresses', os.path.join(tools_dir, 'extract_addresses.py')).extract_addresses
extract_social_links = dynamic_import('extract_social_links', os.path.join(tools_dir, 'extract_social_links.py')).extract_social_links
extract_product_pricing = dynamic_import('extract_product_pricing', os.path.join(tools_dir, 'extract_product_pricing.py')).extract_product_pricing
extract_technology_stack = dynamic_import('extract_technology_stack', os.path.join(tools_dir, 'extract_technology_stack.py')).extract_technology_stack
extract_ssl_info = dynamic_import('extract_ssl_info', os.path.join(tools_dir, 'extract_ssl_info.py')).extract_ssl_info
extract_meta_tags = dynamic_import('extract_meta_tags', os.path.join(tools_dir, 'extract_meta_tags.py')).extract_meta_tags
extract_internal_links = dynamic_import('extract_internal_links', os.path.join(tools_dir, 'extract_internal_links.py')).extract_internal_links

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
        return extract_ssl_info(url)
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
            "SSL/TLS Info": extract_ssl_info(url),
            "Meta Tags": extract_meta_tags(url),
            "Internal links": extract_internal_links(url)
        }
        return all_data
    else:
        return "Invalid choice"