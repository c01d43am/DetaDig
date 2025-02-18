import ssl
import socket
from datetime import datetime

def extract_ssl_info(url):
    """
    Extract SSL certificate details and its expiry date from the given URL.
    """
    try:
        hostname = url.split('//')[-1].split('/')[0]  # Extract domain name

        # Attempt to get the SSL certificate
        context = ssl.create_default_context()
        with socket.create_connection((hostname, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()

        # If cert is retrieved as a dictionary
        cert_details = {
            "issuer": cert.get('issuer'),
            "subject": cert.get('subject'),
            "serial_number": cert.get('serialNumber'),
            "version": cert.get('version'),
            "notBefore": cert.get('notBefore'),
            "notAfter": cert.get('notAfter'),
            "signature_algorithm": cert.get('signatureAlgorithm', 'Not Available')
        }

        # Convert dates and calculate time remaining
        not_after = datetime.strptime(cert_details['notAfter'], "%b %d %H:%M:%S %Y GMT")
        time_remaining = not_after - datetime.utcnow()

        return {
            "certificate_details": cert_details,
            "expiry_date": not_after,
            "time_remaining": time_remaining
        }

    except (ssl.SSLError, socket.error, Exception) as e:
        return f"SSL certificate info could not be retrieved: {str(e)}"

def display_ssl_info(ssl_info):
    """
    Display SSL certificate details.
    """
    if isinstance(ssl_info, dict):
        print("\nSSL Certificate Details:")
        cert_details = ssl_info['certificate_details']
        print(f"  Issuer: {cert_details['issuer']}")
        print(f"  Subject: {cert_details['subject']}")
        print(f"  Serial Number: {cert_details['serial_number']}")
        print(f"  Version: {cert_details['version']}")
        print(f"  Not Before: {cert_details['notBefore']}")
        print(f"  Not After: {cert_details['notAfter']}")
        print(f"  Signature Algorithm: {cert_details['signature_algorithm']}")
        print(f"  Expiry Date: {ssl_info['expiry_date']}")
        print(f"  Time Remaining: {ssl_info['time_remaining']}")
    else:
        print(ssl_info)

def single_scan():
    url = url
    ssl_info = extract_ssl_info(url)
    display_ssl_info(ssl_info)

def bulk_scan():
    file_path = input("Enter file path with URLs: ")
    try:
        with open(file_path, 'r') as file:
            urls = file.readlines()
        for url in urls:
            url = url.strip()
            if url:
                print(f"\nScanning: {url}")
                ssl_info = extract_ssl_info(url)
                display_ssl_info(ssl_info)
    except FileNotFoundError:
        print("File not found. Please enter a valid file path.")

def ssl_menu(url):
    while True:
        print("\nSSL Certificate Scanner")
        print("1. Single URL Scan")
        print("2. Bulk Scan from File")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            single_scan(url)
        elif choice == '2':
            bulk_scan()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    ssl_menu()