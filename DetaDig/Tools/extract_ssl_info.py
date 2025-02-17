# import ssl
# import socket
# from datetime import datetime
# import requests
# import re
# from bs4 import BeautifulSoup

# def extract_ssl_info(url):
#     try:
#         hostname = url.split('//')[-1].split('/')[0]  # Extract domain name

#         # Get SSL certificate
#         try:
#             context = ssl.create_default_context()
#             with socket.create_connection((hostname, 443)) as sock:
#                 with context.wrap_socket(sock, server_hostname=hostname) as ssock:
#                     cert = ssock.getpeercert()
#         except Exception as e:
#             cert = ssl.get_server_certificate((hostname, 443))

#         if isinstance(cert, dict):
#             cert_details = {
#                 "issuer": cert.get('issuer'),
#                 "subject": cert.get('subject'),
#                 "serial_number": cert.get('serialNumber'),
#                 "version": cert.get('version'),
#                 "notBefore": cert.get('notBefore'),
#                 "notAfter": cert.get('notAfter'),
#                 "signature_algorithm": cert.get('signatureAlgorithm', 'Not Available')
#             }

#             # Convert dates
#             not_after = datetime.strptime(cert_details['notAfter'], "%b %d %H:%M:%S %Y GMT")
#             time_remaining = not_after - datetime.utcnow()

#             return {
#                 "certificate_details": cert_details,
#                 "expiry_date": not_after,
#                 "time_remaining": time_remaining
#             }
#         else:
#             return "SSL certificate info could not be retrieved."
#     except Exception as e:
#         return f"SSL certificate info could not be retrieved: {str(e)}"


# def extract_product_pricing(url):
#     try:
#         response = requests.get(url, timeout=10)
#         if response.status_code != 200:
#             return "Failed to retrieve website"

#         soup = BeautifulSoup(response.text, 'html.parser')
#         page_text = soup.get_text()

#         price_pattern = r'[$₹]?\d{1,3}(?:,\d{3})*(?:\.\d{2})?'
#         prices = set(re.findall(price_pattern, page_text))

#         return prices if prices else "No product prices found"
#     except Exception as e:
#         return f"Error fetching product prices: {str(e)}"


# def main():
#     for url in url:
#         print(f"\nProcessing URL: {url}")

#         # Extract SSL Information
#         ssl_info = extract_ssl_info(url)
#         if isinstance(ssl_info, dict):
#             print("\nSSL Certificate Details:")
#             print(f"Issuer: {ssl_info['certificate_details']['issuer']}")
#             print(f"Subject: {ssl_info['certificate_details']['subject']}")
#             print(f"Serial Number: {ssl_info['certificate_details']['serial_number']}")
#             print(f"Version: {ssl_info['certificate_details']['version']}")
#             print(f"Not Before: {ssl_info['certificate_details']['notBefore']}")
#             print(f"Not After: {ssl_info['certificate_details']['notAfter']}")
#             print(f"Signature Algorithm: {ssl_info['certificate_details']['signature_algorithm']}")
#             print(f"Expiry Date: {ssl_info['expiry_date']}")
#             print(f"Time Remaining: {ssl_info['time_remaining']}")
#         else:
#             print(ssl_info)

#         # Extract Product Pricing
#         pricing_info = extract_product_pricing(url)
#         print("\nProduct Pricing Details:")
#         print(pricing_info)


# if __name__ == "__main__":
#     main()

# import ssl
# import socket
# from datetime import datetime
# import requests
# import re
# from bs4 import BeautifulSoup

# def extract_ssl_info(url):
#     try:
#         hostname = url.split('//')[-1].split('/')[0]  # Extract domain name

#         # Get SSL certificate
#         try:
#             context = ssl.create_default_context()
#             with socket.create_connection((hostname, 443)) as sock:
#                 with context.wrap_socket(sock, server_hostname=hostname) as ssock:
#                     cert = ssock.getpeercert()
#         except Exception as e:
#             cert = ssl.get_server_certificate((hostname, 443))

#         if isinstance(cert, dict):
#             cert_details = {
#                 "issuer": cert.get('issuer'),
#                 "subject": cert.get('subject'),
#                 "serial_number": cert.get('serialNumber'),
#                 "version": cert.get('version'),
#                 "notBefore": cert.get('notBefore'),
#                 "notAfter": cert.get('notAfter'),
#                 "signature_algorithm": cert.get('signatureAlgorithm', 'Not Available')
#             }

#             # Convert dates
#             not_after = datetime.strptime(cert_details['notAfter'], "%b %d %H:%M:%S %Y GMT")
#             time_remaining = not_after - datetime.utcnow()

#             return {
#                 "certificate_details": cert_details,
#                 "expiry_date": not_after,
#                 "time_remaining": time_remaining
#             }
#         else:
#             return "SSL certificate info could not be retrieved."
#     except Exception as e:
#         return f"SSL certificate info could not be retrieved: {str(e)}"

# def extract_product_pricing(url):
#     try:
#         response = requests.get(url, timeout=10)
#         if response.status_code != 200:
#             return "Failed to retrieve website"

#         soup = BeautifulSoup(response.text, 'html.parser')
#         page_text = soup.get_text()

#         price_pattern = r'[$₹]?\d{1,3}(?:,\d{3})*(?:\.\d{2})?'
#         prices = set(re.findall(price_pattern, page_text))

#         return prices if prices else "No product prices found"
#     except Exception as e:
#         return f"Error fetching product prices: {str(e)}"

# def main():
#     urls = url

#     for url in urls:
#         print("=" * 50)
#         print(f"Processing URL: {url}")
#         print("=" * 50)

#         # Extract SSL Information
#         ssl_info = extract_ssl_info(url)
#         if isinstance(ssl_info, dict):
#             print("\nSSL Certificate Details:")
#             print("-" * 50)
#             print(f"Issuer            : {ssl_info['certificate_details']['issuer']}\n")
#             print(f"Subject          : {ssl_info['certificate_details']['subject']}\n")
#             print(f"Serial Number  : {ssl_info['certificate_details']['serial_number']}\n")
#             print(f"Version          : {ssl_info['certificate_details']['version']}\n")
#             print(f"Not Before     : {ssl_info['certificate_details']['notBefore']}\n")
#             print(f"Not After      : {ssl_info['certificate_details']['notAfter']}\n")
#             print(f"Signature Algo  : {ssl_info['certificate_details']['signature_algorithm']}\n")
#             print(f"Expiry Date     : {ssl_info['expiry_date']}\n")
#             print(f"Time Remaining  : {ssl_info['time_remaining']}\n")
#         else:
#             print(ssl_info)

#         # Extract Product Pricing
#         print("\nProduct Pricing Details:")
#         print("-" * 50)
#         pricing_info = extract_product_pricing(url)
#         if isinstance(pricing_info, set):
#             for price in pricing_info:
#                 print(price)
#         else:
#             print(pricing_info)
#         print("\n")

# if __name__ == "__main__":
#     main()

import ssl
import socket
from datetime import datetime
import requests
import re
from bs4 import BeautifulSoup

def extract_ssl_info(url):
    try:
        hostname = url.split('//')[-1].split('/')[0]  # Extract domain name

        # Get SSL certificate
        try:
            context = ssl.create_default_context()
            with socket.create_connection((hostname, 443)) as sock:
                with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                    cert = ssock.getpeercert()
        except Exception as e:
            cert = ssl.get_server_certificate((hostname, 443))

        if isinstance(cert, dict):
            cert_details = {
                "issuer": cert.get('issuer'),
                "subject": cert.get('subject'),
                "serial_number": cert.get('serialNumber'),
                "version": cert.get('version'),
                "notBefore": cert.get('notBefore'),
                "notAfter": cert.get('notAfter'),
                "signature_algorithm": cert.get('signatureAlgorithm', 'Not Available')
            }

            # Convert dates
            not_after = datetime.strptime(cert_details['notAfter'], "%b %d %H:%M:%S %Y GMT")
            time_remaining = not_after - datetime.utcnow()

            return {
                "certificate_details": cert_details,
                "expiry_date": not_after,
                "time_remaining": time_remaining
            }
        else:
            return "SSL certificate info could not be retrieved."
    except Exception as e:
        return f"SSL certificate info could not be retrieved: {str(e)}"

def extract_product_pricing(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            return "Failed to retrieve website"

        soup = BeautifulSoup(response.text, 'html.parser')
        page_text = soup.get_text()

        price_pattern = r'[$₹]?\d{1,3}(?:,\d{3})*(?:\.\d{2})?'
        prices = set(re.findall(price_pattern, page_text))

        return prices if prices else "No product prices found"
    except Exception as e:
        return f"Error fetching product prices: {str(e)}"

def main():
    urls = url
    for url in urls:
        print("=" * 50)
        print(f"Processing URL: {url}")
        print("=" * 50)

        # Extract SSL Information
        ssl_info = extract_ssl_info(url)
        if isinstance(ssl_info, dict):
            print("\n🔐 SSL Certificate Details:")
            print("-" * 50)
            print(f"Issuer            : {ssl_info['certificate_details']['issuer']}\n")
            print(f"Subject          : {ssl_info['certificate_details']['subject']}\n")
            print(f"Serial Number    : {ssl_info['certificate_details']['serial_number']}\n")
            print(f"Version          : {ssl_info['certificate_details']['version']}\n")
            print(f"Not Before       : {ssl_info['certificate_details']['notBefore']}\n")
            print(f"Not After        : {ssl_info['certificate_details']['notAfter']}\n")
            print(f"Signature Algo   : {ssl_info['certificate_details']['signature_algorithm']}\n")
            print(f"Expiry Date      : {ssl_info['expiry_date']}\n")
            print(f"Time Remaining   : {ssl_info['time_remaining']}\n")
        else:
            print(f"{ssl_info}\n")

        # Extract Product Pricing
        print("\n💲 Product Pricing Details:")
        print("-" * 50)
        pricing_info = extract_product_pricing(url)
        if isinstance(pricing_info, set):
            for price in pricing_info:
                print(f"{price}\n")
        else:
            print(f"{pricing_info}\n")
        
        print("\n" + "=" * 50)

if __name__ == "__main__":
    main()
