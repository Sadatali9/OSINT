import re

def ip_address_extractor(text):
    """
    IP address extractor to extract IP addresses from a text.
    """
    pattern = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
    ip_addresses = re.findall(pattern, text)
    return ip_addresses

def main():
    text = input("Enter the text to extract IP addresses: ")
    ip_addresses = ip_address_extractor(text)
    print("Extracted IP addresses:")
    for ip_address in ip_addresses:
        print(ip_address)

if __name__ == "__main__":
    main()