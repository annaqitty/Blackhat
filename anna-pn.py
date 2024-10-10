import phonenumbers
from phonenumbers import geocoder, carrier
from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)

def validate_phone_number(phone_number, country_code):
    try:
        # Parse the phone number
        parsed_number = phonenumbers.parse(phone_number, country_code)
        
        # Check if the number is valid
        if phonenumbers.is_valid_number(parsed_number):
            return True, parsed_number
        else:
            return False, None
    except phonenumbers.NumberParseException:
        return False, None

def main():
    print("Please enter the path to a text file containing phone numbers.")
    print("The file should have one phone number per line.")
    print("You can use the following formats:")
    print("1. +[country_code] [phone_number] (e.g., +44 20 7946 0958)")
    print("2. [country_code] [phone_number] (e.g., 44 20 7946 0958)")
    print("3. [area_code] [phone_number] (e.g., 20 7946 0958)")
    
    file_path = input("Enter the path to the text file (or 'exit' to quit): ")
    if file_path.lower() == 'exit':
        return

    try:
        with open(file_path, 'r') as file:
            phone_numbers = [line.strip() for line in file if line.strip()]

        # Process the input phone numbers
        for entry in phone_numbers:
            is_valid = False
            parsed_number = None
            
            # Try different formats
            for format_type in range(1, 4):
                if format_type == 1:
                    # Format: +[country_code] [phone_number]
                    if entry.startswith('+'):
                        try:
                            country_code, phone_number = entry.split(maxsplit=1)
                            is_valid, parsed_number = validate_phone_number(phone_number, country_code[1:])
                            break
                        except ValueError:
                            continue
                
                elif format_type == 2:
                    # Format: [country_code] [phone_number]
                    try:
                        country_code, phone_number = entry.split(maxsplit=1)
                        is_valid, parsed_number = validate_phone_number(phone_number, country_code)
                        break
                    except ValueError:
                        continue
                
                elif format_type == 3:
                    # Format: [area_code] [phone_number] (Assuming no country code)
                    try:
                        phone_number = entry
                        is_valid, parsed_number = validate_phone_number(phone_number, None)
                        if is_valid:
                            break
                    except ValueError:
                        continue
            
            if is_valid:
                # Get country and carrier information
                country = geocoder.region_code_for_number(parsed_number)
                carrier_name = carrier.name_for_number(parsed_number, "en")
                formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
                print(f"{Fore.GREEN}Number {formatted_number} => PhoneNumber Is Valid => {country} - {carrier_name}{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}Invalid Phone Number: {entry}{Style.RESET_ALL}")

    except FileNotFoundError:
        print(f"{Fore.RED}Error '{file_path}' was not found.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}ERROR{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
