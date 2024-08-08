import sqlite3

def create_database(db_name):
    """
    Create a SQLite database.
    """
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS data (
                id INTEGER PRIMARY KEY,
                url TEXT,
                keyword TEXT,
                email TEXT,
                phone_number TEXT,
                ip_address TEXT
                )""")
    conn.commit()
    conn.close()

def insert_data(db_name, url, keyword, email, phone_number, ip_address):
    """
    Insert data into the database.
    """
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("INSERT INTO data (url, keyword, email, phone_number, ip_address) VALUES (?, ?, ?, ?, ?)",
              (url, keyword, email, phone_number, ip_address))
    conn.commit()
    conn.close()

def retrieve_data(db_name):
    """
    Retrieve data from the database.
    """
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("SELECT * FROM data")
    rows = c.fetchall()
    for row in rows:
        print(row)
    conn.close()

def main():
    db_name = "osint.db"
    create_database(db_name)
    url = input("Enter the URL: ")
    keyword = input("Enter the keyword: ")
    email = input("Enter the email: ")
    phone_number = input("Enter the phone number: ")
    ip_address = input("Enter the IP address: ")
    insert_data(db_name, url, keyword, email, phone_number, ip_address)
    retrieve_data(db_name)

if __name__ == "__main__":
    main()