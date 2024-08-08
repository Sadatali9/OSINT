import sqlite3

def create_database(db_path):
    """
    Create a database to store the extracted links.
    """
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS links
                 (webpage_name TEXT, purpose TEXT, url TEXT)''')
    conn.commit()
    conn.close()

def insert_links(db_path, links):
    """
    Insert the extracted links into the database.
    """
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.executemany('INSERT INTO links VALUES (?,?,?)', links)
    conn.commit()
    conn.close()

def search_links(db_path, keyword):
    """
    Search the database for links matching the keyword.
    """
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("SELECT * FROM links WHERE webpage_name LIKE ? OR purpose LIKE ?", (f"%{keyword}%", f"%{keyword}%"))
    results = c.fetchall()
    conn.close()
    return results

def main():
    db_path = 'links.db'
    create_database(db_path)

    folder_path = 'extracted_links'
    file_path = input("Enter the file path: ")
    links = extract_links(file_path)
    insert_links(db_path, links)

    keyword = input("Enter a keyword to search: ")
    results = search_links(db_path, keyword)

    print("Matching webpages:")
    for result in results:
        print(f"Webpage Name: {result[0]}")
        print(f"Purpose: {result[1]}")
        print(f"URL: {result[2]}\n")

    open_option = input("Do you want to open the matching webpages? (y/n): ")
    if open_option.lower() == 'y':
        for result in results:
            url = result[2]
            print(f"Opening {url}...")
            # Open the webpage using the default browser
            import webbrowser
            webbrowser.open(url)

    google_search_option = input("Do you want to search the keyword on Google? (y/n): ")
    if google_search_option.lower() == 'y':
        google_search(keyword)

def google_search(keyword):
    """
    Search the keyword on Google using operators or Google Dorking.
    """
    url = f"https://www.google.com/search?q={keyword}"
    print(f"Searching for {keyword} on Google...")
    # Open the Google search page using the default browser
    import webbrowser
    webbrowser.open(url)

def advance_search():
    """
    Advanced search with operators and Google Dorking.
    """
    keyword = input("Enter a keyword to search: ")
    operators = input("Enter operators (e.g., site:, filetype:, etc.): ")
    url = f"https://www.google.com/search?q={operators} {keyword}"
    print(f"Searching for {keyword} with operators on Google...")
    # Open the Google search page using the default browser
    import webbrowser
    webbrowser.open(url)

if __name__ == "__main__":
    main()