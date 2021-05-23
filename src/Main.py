try:
    import random
    from time import sleep
    import colorama
    from colorama import Fore, Back, Style
    colorama.init(autoreset=False)

    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase_letters = uppercase_letters.lower()
    numbers = '0123456789'
    symbols = '$%&#/!'

    print(f"""
{Fore.MAGENTA}{Style.BRIGHT} _____ _____ _____ _____ _ _ _ _____ _____ ____        {Fore.RED} _____ _____ _____ _____ _____ _____ _____ _____ _____ 
{Fore.MAGENTA}{Style.BRIGHT}|  _  |  _  |   __|   __| | | |     | __  |    \       {Fore.RED}|   __|   __|   | |   __| __  |  _  |_   _|     | __  |
{Fore.MAGENTA}{Style.BRIGHT}|   __|     |__   |__   | | | |  |  |    -|  |  |      {Fore.RED}|  |  |   __| | | |   __|    -|     | | | |  |  |    -|
{Fore.WHITE}|__|  |__|__|_____|_____|_____|_____|__|__|____/       |_____|_____|_|___|_____|__|__|__|__| |_| |_____|__|__|

{Fore.BLUE}Coded By sl04zy on GitHub. Program under MIT License.
    """)

    sleep(1)
    default = str(input(f"\n{Fore.YELLOW}Do you want to use the default protocol? {Fore.WHITE}(y/n){Fore.RESET} "))


    if default == "y":
        upper, lower, digits, syms = True, True, True, False
        all = ""
        if upper:
            all += uppercase_letters
        if lower:
            all += lowercase_letters
        if digits:
            all += numbers
        if syms: 
            all += symbols
        lenght = int(input(f"\n{Fore.YELLOW}How many characters do you want the password to be? {Fore.WHITE}(Insert a number. {Fore.GREEN}Recommended: 16{Fore.WHITE}){Fore.RESET} "))
        amount = 20
        print(f"\n{Fore.GREEN}Here there are some fresh passwords. This are unique passwords. \n{Fore.GREEN}They are pretty safe and can be used to avoid begin pwned.{Fore.RESET}\n\n")
        sleep(1)
        for x in range(amount):
            password = "".join(random.sample(all, lenght))
            print(password)
            sleep(0.1)
        i = input(f"\n{Fore.RED}Once you have copied this passwords press ENTER to exit the program.{Fore.RESET}")
        exit()


    else:
        print("")
        upper = str(input(f"{Fore.YELLOW}Do you want to use uppercase letters? {Fore.WHITE}(y/n) "))
        print("")
        lower = str(input(f"{Fore.YELLOW}Do you want to use lowercase letters? {Fore.WHITE}(y/n) "))
        print("")
        digits = str(input(f"{Fore.YELLOW}Do you want to use numbers? {Fore.WHITE}(y/n) "))
        print("")
        syms = str(input(f"{Fore.YELLOW}Do you want to use symbols {Fore.GREEN}(e.g: @, #){Fore.YELLOW}? {Fore.WHITE}(y/n) "))
        print("")
        print("")
        all = ""
        if upper == "y":
            all += uppercase_letters
        if lower == "y":
            all += lowercase_letters
        if digits == "y":
            all += numbers
        if syms == "y":
            all += symbols
        lenght = int(input(f"\n{Fore.YELLOW}How many characters do you want the password to be? {Fore.WHITE}(Insert a number. {Fore.GREEN}Recommended: 16{Fore.WHITE}){Fore.RESET} "))
        amount = 20
        print(f"\n{Fore.GREEN}Here there are some fresh passwords. This are unique passwords. \n{Fore.GREEN}They are pretty safe and can be used to avoid begin pwned.{Fore.RESET}\n\n")
        sleep(1)
        for x in range(amount):
            password = "".join(random.sample(all, lenght))
            print(password)
            sleep(0.1)
        print("")
        i = input(f"\n{Fore.RED}Once you have copied this passwords press ENTER to exit the program.{Fore.RESET}")

except ModuleNotFoundError:
    print("""
Hello,

If you are seeing this message, means that the program was unable to find
the packages that he needed to work proprely.""")

    p = str(input("\nDo you want to install them? (y/n) "))
    if p == "y":
        import os
        import threading

        def color():
            os.system("pip3 install colorama")

        print("\n\nInstalling packages....")
        print("Note: The process might take a while to complete. Do not shutdown the pc.\n\nOnce the process is completed the program will shutdown himself.")

        thrd = threading.Thread(target=color)
        thrd.start()
        thrd.join()
        exit()
