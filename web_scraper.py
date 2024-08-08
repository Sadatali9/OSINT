import requests
from bs4 import BeautifulSoup

def web_scraper(url):
    """
    Web scraper to extract data from a website.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract data from the website
    data = []
    for element in soup.find_all('div', {'class': 'data'}):
        data.append(element.text.strip())

    return data

def main():
    url = input("Enter the URL to scrape: ")
    data = web_scraper(url)
    print("Extracted data:")
    for item in data:
        print(item)

if __name__ == "__main__":
    main()