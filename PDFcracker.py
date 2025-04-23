import PyPDF2
import os
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def crack_pdf():
    print("\n\n")
    print(Fore.CYAN + """▗▄▄▖ ▗▄▄▄ ▗▄▄▄▖     ▗▄▄▖▗▄▄▖  ▗▄▖  ▗▄▄▖▗▖ ▗▖▗▄▄▄▖▗▄▄▖ 
▐▌ ▐▌▐▌  █▐▌       ▐▌   ▐▌ ▐▌▐▌ ▐▌▐▌   ▐▌▗▞▘▐▌   ▐▌ ▐▌
▐▛▀▘ ▐▌  █▐▛▀▀▘    ▐▌   ▐▛▀▚▖▐▛▀▜▌▐▌   ▐▛▚▖ ▐▛▀▀▘▐▛▀▚▖
▐▌   ▐▙▄▄▀▐▌       ▝▚▄▄▖▐▌ ▐▌▐▌ ▐▌▝▚▄▄▖▐▌ ▐▌▐▙▄▄▖▐▌ ▐▌
                                                      
                                                      
                                                      
""")
    print(Fore.CYAN + "            ▂▃▅▇█▓▒░Author: XZT-01░▒▓█▇▅▃▂\n")
    print(Fore.YELLOW + "             ▂▃▅▇█▓▒░ V 1.00.00 ░▒▓█▇▅▃▂\n")
    print("=" * 40)

    # Step 1: Ask for the PDF file
    pdf_file_name = input(Fore.GREEN + "[ + ] ENTER PDF FILE NAME: ").strip()
    if not os.path.isfile(pdf_file_name):
        print(Fore.YELLOW + "[ ! ] The file does not exist try again!")
        return

    # Step 2: Ask for the password list file
    password_list_name = input(Fore.GREEN + "[ + ] ENTER PASSWORD LIST: ").strip()
    if not os.path.isfile(password_list_name):
        print(Fore.YELLOW + "[ ! ] the password list file does not exist try again!")
        return

    print("=" * 40)
    print(" ")

    # Step 3: Open and try cracking
    try:
        with open(pdf_file_name, "rb") as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)

            if not reader.is_encrypted:
                print(Fore.YELLOW + "[ ! ] This PDF is not password protected.")
                return

            with open(password_list_name, "r", encoding="utf-8", errors="ignore") as pass_file:
                for line in pass_file:
                    password = line.strip()
                    result = reader.decrypt(password)
                    if result == 1 or result == 2:
                        print(Fore.CYAN + f"[ 0 ] {password}")
                        print(Fore.CYAN + f">>> THE PASSWORD WAS CRACKED: [ {password} ] .")
                        return
                    else:
                        print(Fore.RED + f"[ - ] {password}")

            print(Fore.YELLOW + "[ ! ] Password not found in the list.")

    except Exception as e:
        print(Fore.YELLOW + f"[ ! ] An error occurred: {e}")

# Run the function
crack_pdf()