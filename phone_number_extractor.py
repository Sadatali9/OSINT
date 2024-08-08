import re

def phone_number_extractor(text):
    """
    Phone number extractor to extract phone numbers from a text.
    """
    pattern = r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'
    phone_numbers = re.findall(pattern, text)
    return phone_numbers

def main():
    text = input("Enter the text to extract phone numbers: ")
    phone_numbers = phone_number_extractor(text)
    print("Extracted phone numbers:")
    for phone_number in phone_numbers:
        print(phone_number)

if __name__ == "__main__":
    main()