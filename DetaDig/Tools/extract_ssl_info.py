import ssl
import socket
from datetime import datetime

def extract_ssl_info(url):
    try:
        # Extract hostname from the URL
        hostname = url.split('//')[-1].split('/')[0]  # Remove http:// or https://

        # Create an SSL context and connect to the server
        context = ssl.create_default_context()
        with socket.create_connection((hostname, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                # Get the certificate from the server
                cert = ssock.getpeercert()

        # Extract certificate details
        cert_details = {
            "issuer": cert.get('issuer'),
            "subject": cert.get('subject'),
            "serial_number": cert.get('serialNumber'),
            "version": cert.get('version'),
            "notBefore": cert.get('notBefore'),
            "notAfter": cert.get('notAfter'),
            "signature_algorithm": cert.get('signatureAlgorithm')
        }

        # Convert the 'notBefore' and 'notAfter' dates to readable datetime format
        not_before = datetime.strptime(cert_details['notBefore'], "%b %d %H:%M:%S %Y GMT")
        not_after = datetime.strptime(cert_details['notAfter'], "%b %d %H:%M:%S %Y GMT")

        # Calculate time remaining until expiry
        current_date = datetime.utcnow()
        time_remaining = not_after - current_date

        # Prepare final output
        result = {
            "certificate_details": cert_details,
            "expiry_date": not_after,
            "time_remaining": time_remaining
        }

        return result

    except Exception as e:
        return f"SSL certificate info could not be retrieved: {str(e)}"

# Example usage
url = "https://www.example.com"  # Replace with the target URL
ssl_info = extract_ssl_info(url)

if isinstance(ssl_info, dict):
    print(f"SSL Certificate Details:")
    print(f"Issuer: {ssl_info['certificate_details']['issuer']}")
    print(f"Subject: {ssl_info['certificate_details']['subject']}")
    print(f"Serial Number: {ssl_info['certificate_details']['serial_number']}")
    print(f"Version: {ssl_info['certificate_details']['version']}")
    print(f"Not Before: {ssl_info['certificate_details']['notBefore']}")
    print(f"Not After: {ssl_info['certificate_details']['notAfter']}")
    print(f"Signature Algorithm: {ssl_info['certificate_details']['signature_algorithm']}")
    print(f"Expiry Date: {ssl_info['expiry_date']}")
    print(f"Time Remaining: {ssl_info['time_remaining']}")
else:
    print(ssl_info)
