from colorama import Fore, Back, Style

def printcolor(color, text):
    if color.upper() == 'RED':
        print(f'{Fore.RED}' + text + Style.RESET_ALL)
    elif color.upper() == 'GREEN':
        print(f'{Fore.GREEN}' + text + Style.RESET_ALL)
    elif color.upper() == 'BLUE':
        print(f'{Fore.BLUE}' + text + Style.RESET_ALL)
    elif color.upper() == 'YELLOW':
        print(f'{Fore.YELLOW}' + text + Style.RESET_ALL)

