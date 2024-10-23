import socket
import requests
from datetime import datetime

# Function to get public IPv4 and IPv6 addresses using ipify API
def get_public_ip(version="ipv4"):
    if version == "ipv6":
        url = "https://api6.ipify.org?format=json"
    else:
        url = "https://api.ipify.org?format=json"
    
    try:
        response = requests.get(url)
        ip_data = response.json()
        return ip_data['ip']
    except Exception as e:
        return f"Error fetching {version}: {str(e)}"

# Function to get location information from ipinfo.io API (for IPv4 only)
def get_location(ip):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        data = response.json()
        return {
            'ip': data.get('ip', 'N/A'),
            'city': data.get('city', 'N/A'),
            'region': data.get('region', 'N/A'),
            'country': data.get('country', 'N/A'),
            'loc': data.get('loc', 'N/A'),  # Latitude and Longitude
            'timezone': data.get('timezone', 'N/A')
        }
    except Exception as e:
        return {"error": str(e)}

# Function to get the current time and date
def get_current_time():
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

# Main function to get both IPv4 and IPv6 along with location (IPv4 only)
def main():
    # Get the public IPv4 and IPv6 addresses
    ipv4 = get_public_ip("ipv4")
    ipv6 = get_public_ip("ipv6")
    
    # Get location details for IPv4 (only)
    ipv4_location = get_location(ipv4) if "Error" not in ipv4 else {"error": ipv4}
    
    # Get the current time and date
    current_time = get_current_time()

    # Output the results
    print(f"Public IPv4: {ipv4}")
    print(f"Location (IPv4): {ipv4_location}")
    print(f"Public IPv6: {ipv6}")
    print(f"Time/Date captured: {current_time}")

if __name__ == "__main__":
    main()

