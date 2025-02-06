import phonenumbers
from phonenumbers import geocoder, carrier, phonenumberutil, timezone
import requests

# Judul ASCII dengan warna biru
title = r"""
  _  __           _       _        _        
 | |/ /    __ _  | |__   (_)  ___ | |_  ___ 
 | ' /    / _` | | '_ \  | | / _ \| __|/ __|
 | . \   | (_| | | | | | | ||  __/| |_ \__ \
 |_|\_\   \__,_| |_| |_|_/ | \___| \__||___/
                      |__/                   
"""
print("\033[1;34;40m" + title + "\033[m")  

print("📞 Welcome to the Phone Number & Location Tracker!")
print("Please enter the phone number below:")

# Input nomor telepon
phone_number = input("Enter the phone number (with country code, e.g., +628123456789): ")

try:
    # Parsing nomor telepon
    number = phonenumbers.parse(phone_number, None)
    
    # Informasi nomor telepon
    country_code = phonenumbers.region_code_for_number(number)
    country_name = geocoder.country_name_for_number(number, "en")
    location = geocoder.description_for_number(number, "en")
    carrier_name = carrier.name_for_number(number, "en") if carrier.name_for_number(number, "en") else "Unknown Carrier"
    number_type = phonenumbers.number_type(number)
    validity = "Valid" if phonenumbers.is_valid_number(number) else "Invalid"
    formatted_number = phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)

    # Zona waktu
    time_zones = timezone.time_zones_for_number(number)
    time_zones_description = f"Time Zones: {', '.join(time_zones)}" if time_zones else "Time zone info not available"
    
    # Informasi jenis nomor
    number_type_description = {
        phonenumberutil.PhoneNumberType.MOBILE: "Mobile",
        phonenumberutil.PhoneNumberType.FIXED_LINE: "Fixed-line",
        phonenumberutil.PhoneNumberType.TOLL_FREE: "Toll-free",
        phonenumberutil.PhoneNumberType.PREMIUM_RATE: "Premium rate",
        phonenumberutil.PhoneNumberType.SHARED_COST: "Shared cost",
        phonenumberutil.PhoneNumberType.VOIP: "VOIP",
    }.get(number_type, "Other")

    # Mencetak detail nomor
    print("\n🌐 Phone Number Details 🌐:")
    print(f"📍 Country: {country_name} ({country_code})")
    print(f"📌 Location: {location}")
    print(f"📡 Carrier: {carrier_name}")
    print(f"📲 Number Type: {number_type_description}")
    print(f"✅ Validity: {validity}")
    print(f"📞 Formatted: {formatted_number}")
    print(f"⏰ Time Zone: {time_zones_description}")

except phonenumbers.phonenumberutil.NumberParseException as e:
    print("❌ Number could not be parsed:", e)
    exit()

# ======================== 🔍 GEOLOCATION (IP-BASED) 🔍 ========================

def get_ip_location():
    """Mengambil lokasi berdasarkan alamat IP"""
    url = "http://ip-api.com/json/"
    response = requests.get(url)
    data = response.json()
    
    if data["status"] == "fail":
        print("\n❌ Tidak dapat menemukan lokasi berdasarkan IP.")
        return

    print("\n🌍 IP-Based Location Info 🌍:")
    print(f"🌎 Country: {data['country']} ({data['countryCode']})")
    print(f"🏙️ City: {data['city']}")
    print(f"📍 Latitude: {data['lat']}")
    print(f"📍 Longitude: {data['lon']}")
    print(f"🕵️ ISP: {data['isp']}")
    print(f"📡 IP Address: {data['query']}")

# Jalankan fungsi pelacakan lokasi berdasarkan IP
get_ip_location()
