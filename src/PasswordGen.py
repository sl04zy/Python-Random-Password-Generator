try:
    import random
    from time import sleep
    import colorama
    from colorama import Fore, Back, Style
    from colorama import init
    init(autoreset=False)

    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase_letters = uppercase_letters.lower()
    numbers = '0123456789'
    symbols = '$%&#/!'

    print(f"""
{Fore.MAGENTA}{Style.BRIGHT} _____ _____ _____ _____ _ _ _ _____ _____ ____        {Fore.RED} _____ _____ _____ _____ _____ _____ _____ _____ _____ 
{Fore.MAGENTA}{Style.BRIGHT}|  _  |  _  |   __|   __| | | |     | __  |    \       {Fore.RED}|   __|   __|   | |   __| __  |  _  |_   _|     | __  |
{Fore.MAGENTA}{Style.BRIGHT}|   __|     |__   |__   | | | |  |  |    -|  |  |      {Fore.RED}|  |  |   __| | | |   __|    -|     | | | |  |  |    -|
{Fore.WHITE}|__|  |__|__|_____|_____|_____|_____|__|__|____/       |_____|_____|_|___|_____|__|__|__|__| |_| |_____|__|__|

{Fore.BLUE}Coded By sl04zy on GitHub. Program under MIT License.{Fore.RESET}
    """)

    sleep(1)
    print(f"{Fore.YELLOW}Do you want to use the default generation?{Fore.RESET}")
    print(f"{Fore.YELLOW}The default generation uses: {Fore.RED}Uppercase letters{Fore.YELLOW}, {Fore.RED}Lowercase letters {Fore.YELLOW}&{Fore.RED} Numbers{Fore.YELLOW}.{Fore.RESET}")
    default = str(input(f"Insert input (y/n): "))

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
        print(f"\n{Fore.YELLOW}How many characters do you want the password to be?{Fore.RESET}")
        lenght = int(input("Insert a number (Recommended 16, Max 62): "))
        amount = 20
        print(f"\n{Fore.GREEN}Here there are some fresh passwords. This are unique passwords. \nThey are pretty safe and can be used to avoid begin pwned.{Fore.RESET}\n\n")
        sleep(1)
        for x in range(amount):
            password = "".join(random.sample(all, lenght))
            print(password)
            sleep(0.1)
        print("")
        print(f"\n{Fore.RED}Once you have copied this passwords press ENTER to exit the program.{Fore.RESET}")
        i = input("Press ENTER to continue.....")
        exit()


    else:
        print("")
        print(f"{Fore.YELLOW}Do you want to use uppercase letters?{Fore.RESET}")
        upper = str(input(f"Insert input (y/n): "))
        print("")
        print(f"{Fore.YELLOW}Do you want to use lowercase letters?{Fore.RESET}")
        lower = str(input(f"Insert input (y/n): "))
        print("")
        print(f"{Fore.YELLOW}Do you want to use numbers?{Fore.RESET}")
        digits = str(input(f"Insert input (y/n): "))
        print("")
        print(f"{Fore.YELLOW}Do you want to use symbols (e.g: @, #)?{Fore.RESET}")
        syms = str(input(f"Insert input (y/n): "))
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
        print(f"\n{Fore.YELLOW}How many characters do you want the password to be?{Fore.RESET}")
        lenght = int(input("Insert a number (Recommended 16, Max 62): "))
        amount = 20
        print(f"\n{Fore.GREEN}Here there are some fresh passwords. This are unique passwords. \n{Fore.GREEN}They are pretty safe and can be used to avoid begin pwned.{Fore.RESET}\n\n")
        sleep(1)
        for x in range(amount):
            password = "".join(random.sample(all, lenght))
            print(password)
            sleep(0.1)
        print("")
        print(f"\n{Fore.RED}Once you have copied this passwords press ENTER to exit the program.{Fore.RESET}")
        i = input("Press ENTER to continue.....")
        exit()



except KeyboardInterrupt:
    exit()



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



except ValueError:
    print(f"\n\n{Fore.RED}Error:{Fore.GREEN} an error occurred during the process!{Fore.RESET}")
    print(f"{Fore.YELLOW}Please follow carefully the instructions before submitting any inputs.{Fore.RESET}")
    print(f"{Fore.RED}Closing the program, please wait....{Fore.RESET}")
    sleep(5)
    exit()

