import os
import re
from bs4 import BeautifulSoup
from PyPDF2 import PdfFileReader
import requests

def extract_links(file_path):
    """
    Extract links from a file and save them in a structured format.
    """
    links = []
    with open(file_path, 'r') as file:
        if file_path.endswith('.html'):
            soup = BeautifulSoup(file, 'html.parser')
            for link in soup.find_all('a'):
                links.append({
                    'webpage_name': link.text.strip(),
                    'purpose': link.get('title'),
                    'url': link.get('href')
                })
        elif file_path.endswith('.pdf'):
            pdf = PdfFileReader(file)
            for page in pdf.pages:
                text = page.extractText()
                links.extend(re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text))
        else:
            text = file.read()
            links.extend(re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text))
    return links

def save_links(links, folder_path):
    """
    Save the extracted links in a structured format to a file.
    """
    with open(os.path.join(folder_path, 'links.txt'), 'w') as file:
        for link in links:
            file.write(f"Webpage Name: {link['webpage_name']}\n")
            file.write(f"Purpose: {link['purpose']}\n")
            file.write(f"URL: {link['url']}\n\n")

def main():
    folder_path = 'extracted_links'
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    file_path = input("Enter the file path: ")
    links = extract_links(file_path)
    save_links(links, folder_path)

    print(f"Links extracted and saved to {folder_path}/links.txt")

if __name__ == "__main__":
    main()