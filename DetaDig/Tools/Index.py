import sys

# Importing data extraction functions from separate files
from Tools.extract_emails import extract_emails
from Tools.extract_phone_numbers import extract_phone_numbers
from Tools.extract_addresses import extract_addresses
from Tools.extract_social_links import extract_social_links
from Tools.extract_product_pricing import extract_product_pricing
from Tools.extract_technology_stack import extract_technology_stack
from Tools.extract_ssl_info import extract_ssl_info
from Tools.extract_meta_tags import extract_meta_tags
from Tools.extract_internal_links import extract_internal_links

def main():
    print("Welcome to the Website Data Extractor!")
    url = input("Enter the website URL (e.g., https://example.com): ")

    while True:
        print("\nSelect the data you want to extract:")
        print("1. Extract Emails")
        print("2. Extract Phone Numbers")
        print("3. Extract Addresses")
        print("4. Extract Social Media Links")
        print("5. Extract Product Prices")
        print("6. Extract Technology Stack (CMS, Web Server, etc.)")
        print("7. Extract SSL/TLS Certificate Information")
        print("8. Extract Meta Tags")
        print("9. Extract Internal Links")
        print("10. Extract All Data")
        print("11. Exit")

        choice = input("Enter your choice (1-11): ")

        if choice == '1':
            emails = extract_emails(url)
            print(f"Emails found: {emails}")
        elif choice == '2':
            phone_numbers = extract_phone_numbers(url)
            print(f"Phone numbers found: {phone_numbers}")
        elif choice == '3':
            addresses = extract_addresses(url)
            print(f"Addresses found: {addresses}")
        elif choice == '4':
            social_links = extract_social_links(url)
            print(f"Social media links found: {social_links}")
        elif choice == '5':
            prices = extract_product_pricing(url)
            print(f"Product prices found: {prices}")
        elif choice == '6':
            tech_stack = extract_technology_stack(url)
            print(f"Technology Stack: {tech_stack}")
        elif choice == '7':
            ssl_info = extract_ssl_info(url)
            print(f"SSL Certificate Info: {ssl_info}")
        elif choice == '8':
            meta_tags = extract_meta_tags(url)
            print(f"Meta Tags: {meta_tags}")
        elif choice == '9':
            internal_links = extract_internal_links(url)
            print(f"Internal links found: {internal_links}")
        elif choice == '10':
            # Extract all data
            emails = extract_emails(url)
            print(f"Emails found: {emails}")

            phone_numbers = extract_phone_numbers(url)
            print(f"Phone numbers found: {phone_numbers}")

            addresses = extract_addresses(url)
            print(f"Addresses found: {addresses}")

            social_links = extract_social_links(url)
            print(f"Social media links found: {social_links}")

            prices = extract_product_pricing(url)
            print(f"Product prices found: {prices}")

            tech_stack = extract_technology_stack(url)
            print(f"Technology Stack: {tech_stack}")

            ssl_info = extract_ssl_info(url)
            print(f"SSL Certificate Info: {ssl_info}")

            meta_tags = extract_meta_tags(url)
            print(f"Meta Tags: {meta_tags}")

            internal_links = extract_internal_links(url)
            print(f"Internal links found: {internal_links}")
        elif choice == '11':
            print("Exiting the program. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()