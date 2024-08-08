import google

def advance_search(keyword, operators):
    """
    Advanced search with operators and Google Dorking.
    """
    url = f"https://www.google.com/search?q={operators} {keyword}"
    print(f"Searching for {keyword} with operators on Google...")
    # Open the Google search page using the default browser
    import webbrowser
    webbrowser.open(url)

def main():
    keyword = input("Enter a keyword to search: ")
    operators = input("Enter operators (e.g., site:, filetype:, etc.): ")
    advance_search(keyword, operators)

if __name__ == "__main__":
    main()