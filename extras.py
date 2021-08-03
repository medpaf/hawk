from colorama import Fore, Back, Style

def printcolor(color, text):
    if color.upper() == 'RED':
        print(f'{Fore.RED}' + text + Style.RESET_ALL)
    elif color.upper() == 'GREEN':
        print(f'{Fore.GREEN}' + text + Style.RESET_ALL)
    elif color.upper() == 'BLUE':
        print(f'{Fore.BLUE}' + text + Style.RESET_ALL)

def inputcolor(color, text):
    if color.upper() == 'RED':
        comm = input(f'{Fore.RED}' + text + Style.RESET_ALL)
    elif color.upper() == 'GREEN':
        comm = input(f'{Fore.GREEN}' + text + Style.RESET_ALL)
    elif color.upper() == 'BLUE':
        comm = input(f'{Fore.BLUE}' + text + Style.RESET_ALL)
    return comm