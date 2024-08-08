import os
import re
import requests
from bs4 import BeautifulSoup
import webbrowser

def read_urls_from_file(file_name):
    """Read URLs from a file and return them as a list."""
    urls = []
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            urls.append(line.strip())
    return urls

def search_google(query):
    """Search Google for a query and return the results."""
    url = f'https://www.google.com/search?q={query}'
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    results = []
    for result in soup.find_all('div', class_='g'):
        link = result.find('a')['href']
        title = result.find('h3').text
        purpose = re.search(r'/url\?q=(.*)&sa=', link).group(1)
        results.append((purpose, title))
    return results

def modify_file(file_name, urls):
    """Modify a file by replacing each URL with its purpose."""
    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            for line in file:
                for url in urls:
                    line = line.replace(url, url['purpose'])
                file.write(line)
    except IOError:
        print('Error: Unable to modify file.')

def filter_urls(urls, keywords):
    """Filter URLs based on keywords."""
    filtered_urls = []
    for url in urls:
        if any(keyword.lower() in url['purpose'].lower() for keyword in keywords):
            filtered_urls.append(url)
    return filtered_urls

def main():
    """Find websites related to the given keywords."""
    folder_name = 'urls'
    urls = []
    for file_name in os.listdir(folder_name):
        if file_name.endswith('.txt'):
            urls += read_urls_from_file(os.path.join(folder_name, file_name))
    keywords = input('Enter your keywords (separated by commas): ').split(',')
    results = search_google(' OR '.join(keywords))
    urls = [{'purpose': purpose, 'title': title} for purpose, title in results]
    if os.path.exists('unfiltered.txt'):
        modify_file('unfiltered.txt', urls)
    else:
        print('Error: unfiltered.txt file not found.')
        print('Redirecting to Google...')
        webbrowser.open('https://www.google.com/search?q=' + '+'.join(keywords))
        return
    filtered_urls = filter_urls(urls, keywords)
    print('Filtered URLs:')
    for url in filtered_urls:
        print(url['purpose'])
    if filtered_urls:
        redirect = input('Do you want to redirect to one of these websites? (yes/no) ').lower()
        if redirect == 'yes':
            url_title = input('Enter the title of the website you want to redirect to: ')
            url = next((url for url in filtered_urls if url['title'].lower() == url_title.lower()), None)
            if url:
                webbrowser.open(url['purpose'])
            else:
                print('Error: Website not found.')
        elif redirect == 'no':
            print('Redirect cancelled.')
        else:
            print('Invalid input.')
    else:
        print('No websites found.')

if __name__ == '__main__':
    main()