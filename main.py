import hashlib
import os
import time
import colorama
from colorama import Fore, Back, Style
import pyfiglet

# Clear screen function
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Animation function
def animation(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()

# Tool interface
def tool_interface():
    clear_screen()
    banner = pyfiglet.figlet_format("HaSh-ED", font="slant")
    print(Fore.WHITE + banner)
    print(Fore.RED + "Author: LocalHost.07" + Style.RESET_ALL)
    print(Fore.YELLOW + "Encrypt , Decrypt [ crack ] Hashes . HaSh Ed Tool" + Style.RESET_ALL)
    print()

# Encrypt function
def encrypt():
    clear_screen()
    tool_interface()
    print(Fore.GREEN + "Encryption Mode" + Style.RESET_ALL)
    password = input(Fore.YELLOW + "Enter password to encrypt: " + Style.RESET_ALL)
    print(Fore.CYAN + "Select hash type:" + Style.RESET_ALL)
    print(Fore.WHITE + "1. MD5")
    print(Fore.WHITE + "2. SHA1")
    print(Fore.WHITE + "3. SHA256")
    print(Fore.WHITE + "4. SHA512")
    choice = input(Fore.BLUE + "Enter choice (1-4): " + Style.RESET_ALL)
    if choice == '1':
        hash_type = 'md5'
        encrypted_password = hashlib.md5(password.encode()).hexdigest()
    elif choice == '2':
        hash_type = 'sha1'
        encrypted_password = hashlib.sha1(password.encode()).hexdigest()
    elif choice == '3':
        hash_type = 'sha256'
        encrypted_password = hashlib.sha256(password.encode()).hexdigest()
    elif choice == '4':
        hash_type = 'sha512'
        encrypted_password = hashlib.sha512(password.encode()).hexdigest()
    else:
        print(Fore.RED + "Invalid choice. Please try again." + Style.RESET_ALL)
        return
    print(Fore.GREEN + "Encrypted password: " + Style.RESET_ALL + encrypted_password)

# Decrypt (Crack) function
def decrypt_crack():
    clear_screen()
    tool_interface()
    print(Fore.GREEN + "Buy Full tool to get crack method " + Style.RESET_ALL)

# Main function
def main():
    tool_interface()
    while True:
        print(Fore.WHITE + "Enter 'e' to Encrypt, 'd' to Decrypt (Crack), 'c' for credits, or 'q' to quit: " + Style.RESET_ALL, end='')
        choice = input().lower()
        if choice == 'e':
            encrypt()
        elif choice == 'd':
            decrypt_crack()
        elif choice == 'c':
            clear_screen()
            animation("HaSh ED - Password Encryption, Decryption, and Cracking Tool")
            print(Fore.GREEN + "\tCreated by LocalHost.07" + Style.RESET_ALL)
            input(Fore.BLUE + "Press enter to continue..." + Style.RESET_ALL)
        elif choice == 'q':
            break
        else:
            print(Fore.RED + "Invalid choice. Please try again." + Style.RESET_ALL)

if __name__ == "__main__":
    animation("Loading HaSh ED...")
    main()
        
