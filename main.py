# main.py

import os
import installer

def main():
    print("Welcome to the OSINT Tool!")
    print("----------------------------")

    # Check if requirements are installed
    if not os.path.exists("requirements.txt") or not os.path.isfile("requirements.txt"):
        print("Requirements file not found. Running installer...")
        installer.main()
        print("wait..")
        print("Requirements installed successfully!")
    
    # Main menu
    while True:
        print("\nMain Menu:")
        print("1. Link Extractor")
        print("2. Keyword Search")
        print("3. Advance Search")
        print("4. Google Dorking")
        print("5. Web Scraper")
        print("6. Email Extractor")
        print("7. Phone Number Extractor")
        print("8. IP Address Extractor")
        print("9. Database")
        print("10. PDF Parser")
        print("11. Image Analyzer")
        print("12. Social Media Analyzer")
        print("13. Network Scanner")
        print("14. Cryptography")
        print("15. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            import link_extractor
            link_extractor.main()
        elif choice == "2":
            import keyword_search
            keyword_search.main()
        elif choice == "3":
            import advance_search
            advance_search.main()
        elif choice == "4":
            import google_dorking
            google_dorking.main()
        elif choice == "5":
            import web_scraper
            web_scraper.main()
        elif choice == "6":
            import email_extractor
            email_extractor.main()
        elif choice == "7":
            import phone_number_extractor
            phone_number_extractor.main()
        elif choice == "8":
            import ip_address_extractor
            ip_address_extractor.main()
        elif choice == "9":
            import database
            database.main()
        elif choice == "10":
            import pdf_parser
            pdf_parser.main()
        elif choice == "11":
            import image_analyzer
            image_analyzer.main()
        elif choice == "12":
            import social_media_analyzer
            social_media_analyzer.main()
        elif choice == "13":
            import network_scanner
            network_scanner.main()
        elif choice == "14":
            import cryptography
            cryptography.main()
        elif choice == "15":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()