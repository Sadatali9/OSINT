import os
import platform
import subprocess

def install_requirements(os_type):
    if os_type == "kali":
        # Install requirements for Kali Linux
        os.system("sudo apt-get update")
        os.system("sudo apt-get install -y python3-pip")
        subprocess.run(["sudo", "pip3", "install", "-r", "requirements.txt"])
        print("Requirements installed successfully for Kali Linux!")
    elif os_type == "windows":
        # Install requirements for Windows
        subprocess.run(["pip", "install", "-r", "requirements.txt"])
        print("Requirements installed successfully for Windows!")
    else:
        print("Invalid OS type. Please enter 'kali' or 'windows'.")

def main():
    print("Welcome to the OSINT Tool Installer!")
    print("----------------------------")
    if not os.path.exists("requirements.txt") or not os.path.isfile("requirements.txt"):
        print("Requirements file not found. Please create a requirements.txt file.")
    else:
        os_type = input("Which OS are you using? (kali/windows): ")
        install_requirements(os_type)

if __name__ == "__main__":
    main()