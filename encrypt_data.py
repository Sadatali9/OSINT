from cryptography.fernet import Fernet

def encrypt_data(plain_text, key):
    """
    Encrypt data using Fernet algorithm.
    """
    cipher_suite = Fernet(key)
    cipher_text = cipher_suite.encrypt(plain_text.encode())
    return cipher_text

def decrypt_data(cipher_text, key):
    """
    Decrypt data using Fernet algorithm.
    """
    cipher_suite = Fernet(key)
    plain_text = cipher_suite.decrypt(cipher_text).decode()
    return plain_text

def main():
    plain_text = input("Enter the plain text: ")
    key = Fernet.generate_key()
    cipher_text = encrypt_data(plain_text, key)
    print("Encrypted text:")
    print(cipher_text)
    plain_text = decrypt_data(cipher_text, key)
    print("Decrypted text:")
    print(plain_text)

if __name__ == "__main__":
    main()