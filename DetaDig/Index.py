import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from DetaDig.Updates.update_checker import check_for_updates
from DetaDig.Updates.data_extraction import extract_data
from DetaDig.Design.design import Font_banner

def main():
    # Display the banner
    Font_banner()
    # Check if repo is up to date before proceeding
    if not check_for_updates():
        print("Unable to proceed due to update issues.")
        return

    url = input("Enter the website URL (e.g., https://example.com): ")

    while True:
        print("\nSelect the data you want to extract (comma-separated for multiple choices):")
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

        choices = input("Enter your choices (e.g., 1,3,5): ").split(',')

        if '11' in choices:
            print("Exiting the program. Goodbye!")
            break

        for choice in choices:
            choice = choice.strip()
            result = extract_data(url, choice)
            if choice == '10':
                for key, value in result.items():
                    print(f"{key}: {value}")
            else:
                print(f"Result for choice {choice}: {result}")

if __name__ == "__main__":
    main()