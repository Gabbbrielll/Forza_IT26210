import socket
import requests
from datetime import datetime
import tkinter as tk


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


def get_current_time():
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


def fetch_ip_data():
    ipv4 = get_public_ip("ipv4")
    ipv6 = get_public_ip("ipv6")
    
    ipv4_location = get_location(ipv4) if "Error" not in ipv4 else {"error": ipv4}

    current_time = get_current_time()

    ipv4_label.config(text=f"IPv4: {ipv4}")
    ipv6_label.config(text=f"IPv6: {ipv6 if 'Error' not in ipv6 else 'Not found'}")
    
    if "error" not in ipv4_location:
        location_text = f"Location (IPv4): {ipv4_location['city']}, {ipv4_location['region']}, {ipv4_location['country']}"
    else:
        location_text = f"Error: {ipv4_location['error']}"
    
    location_label.config(text=location_text)
    time_label.config(text=f"Time/Date: {current_time}")

root = tk.Tk()
root.title("IP Address Finder")

background_color = "#B1D690"
root.configure(bg=background_color)

root.geometry("500x300")
root.resizable(False, False)

title_label = tk.Label(root, text="IP Address and Location Finder", font=("Helvetica", 16, "bold"), bg=background_color)
title_label.pack(pady=10)

ipv4_label = tk.Label(root, text="IPv4: Waiting...", font=("Helvetica", 12), bg=background_color)
ipv4_label.pack(pady=5)

ipv6_label = tk.Label(root, text="IPv6: Waiting...", font=("Helvetica", 12), bg=background_color)
ipv6_label.pack(pady=5)

location_label = tk.Label(root, text="Location (IPv4): Waiting...", font=("Helvetica", 12), bg=background_color)
location_label.pack(pady=5)

time_label = tk.Label(root, text="Time/Date: Waiting...", font=("Helvetica", 12), bg=background_color)
time_label.pack(pady=10)

fetch_button = tk.Button(root, text="Fetch IP Addresses", command=fetch_ip_data, font=("Helvetica", 12), bg="#A9C67A")
fetch_button.pack(pady=10)

root.mainloop()