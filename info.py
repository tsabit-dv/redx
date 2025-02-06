import phonenumbers
from phonenumbers import geocoder, carrier, phonenumberutil, timezone

title = """
  ____  _____ ____      __  __  ___ _   _ _____ ___  
 |  _ \| ____|  _ \     \ \/ / |_ _| \ | |  ___/ _ \ 
 | |_) |  _| | | | |_____\  /   | ||  \| | |_ | | | |
 |  _ <| |___| |_| |_____/  \   | || |\  |  _|| |_| |
 |_| \_\_____|____/     /_/\_\ |___|_| \_|_|   \___/ 
"""

print("\033[1;32;40m" + title + "\033[m")  
print("📞 Welcome to the Phone Number Details Extractor by Redx! 📞")
print("Please enter the phone number below:")

phone_number = input("Enter the phone number: ")

try:
    number = phonenumbers.parse(phone_number, None)
    country_code = phonenumbers.region_code_for_number(number)
    location = geocoder.description_for_number(number, "en")
    carrier_name = carrier.name_for_number(number, "en") if carrier.name_for_number(number, "en") else "Unknown Carrier"
    
    number_type = phonenumberutil.number_type(number)
    number_type_description = {
        phonenumbers.PhoneNumberType.MOBILE: "Mobile",
        phonenumbers.PhoneNumberType.FIXED_LINE: "Fixed-line",
        phonenumbers.PhoneNumberType.TOLL_FREE: "Toll-free",
        phonenumbers.PhoneNumberType.PREMIUM_RATE: "Premium rate",
        phonenumbers.PhoneNumberType.SHARED_COST: "Shared cost",
        phonenumbers.PhoneNumberType.VOIP: "VOIP"
    }.get(number_type, "Other")

    validity = "Valid" if phonenumbers.is_valid_number(number) else "Invalid"
    formatted_number = phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    country_name = geocoder.country_name_for_number(number, "en")
    is_possible = "Possible" if phonenumbers.is_possible_number(number) else "Not possible"

    time_zones = timezone.time_zones_for_number(number)
    time_zones_description = f"Time Zones: {', '.join(time_zones)}" if time_zones else "Time zone information not available"

    national_number = phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.NATIONAL)
    extension = number.extension if number.extension else "No extension"

    is_possible_mobile = "Possible" if phonenumbers.is_possible_number_for_type(number, phonenumbers.PhoneNumberType.MOBILE) else "Not possible"
    is_possible_fixed = "Possible" if phonenumbers.is_possible_number_for_type(number, phonenumbers.PhoneNumberType.FIXED_LINE) else "Not possible"

    possible_lengths = [match.raw_string for match in phonenumbers.PhoneNumberMatcher(phone_number, "ZZ")]
    possible_lengths_description = f"Possible lengths: {', '.join(str(len(num)) for num in possible_lengths)}" if possible_lengths else "Unknown length"

    details = {
        "Country Code": country_code,
        "Country Name": country_name,
        "Location": location,
        "Carrier": carrier_name,
        "Number Type": number_type_description,
        "Validity": validity,
        "Formatted Number": formatted_number,
        "Possible Lengths": possible_lengths_description,
        "Is Possible Number": is_possible,
        "Time Zones": time_zones_description,
        "National Number": national_number,
        "Extension": extension,
        "Possible Mobile Number": is_possible_mobile,
        "Possible Fixed-line Number": is_possible_fixed,
    }

    print("\n🌐 Phone Number Details 🌐:")
    for key, value in details.items():
        print(f"{key}: {value}")
        
except phonenumbers.phonenumberutil.NumberParseException as e:
    print("❌ Number could not be parsed:", e)
