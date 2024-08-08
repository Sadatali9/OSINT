import google

def google_dorking(keyword):
    """
    Google Dorking with keyword.
    """
    url = f"https://www.google.com/search?q={keyword}"
    print(f"Searching for {keyword} on Google...")
    # Open the Google search page using the default browser
    import webbrowser
    webbrowser.open(url)

def main():
    keyword = input("Enter a keyword to search: ")
    google_dorking(keyword)

if __name__ == "__main__":
    main()