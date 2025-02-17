import ssl
import socket

def extract_ssl_info(url):
    try:
        hostname = url.split('//')[-1].split('/')[0]  # Remove http:// or https://
        cert = ssl.get_server_certificate((hostname, 443))
        return cert
    except Exception as e:
        return f"SSL certificate info could not be retrieved: {str(e)}"
