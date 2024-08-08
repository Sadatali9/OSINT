import re

def email_extractor(text):
    """
    Email extractor to extract email addresses from a text.
    """
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(pattern, text)
    return emails

def main():
    text = input("Enter the text to extract emails: ")
    emails = email_extractor(text)
    print("Extracted emails:")
    for email in emails:
        print(email)

if __name__ == "__main__":
    main()