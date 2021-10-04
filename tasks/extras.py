import time
from colorama import Fore, Back, Style

def printcolor(color, text):
    if color.upper() == 'RED':
        return(f'{Fore.RED}' + text + Style.RESET_ALL)
    elif color.upper() == 'GREEN':
        return(f'{Fore.GREEN}' + text + Style.RESET_ALL)
    elif color.upper() == 'BLUE':
        return(f'{Fore.BLUE}' + text + Style.RESET_ALL)
    elif color.upper() == 'YELLOW':
        return(f'{Fore.YELLOW}' + text + Style.RESET_ALL)

def inputcolor(color, text):
    if color.upper() == 'RED':
        comm = input(f'{Fore.RED}' + text + Style.RESET_ALL)
    elif color.upper() == 'GREEN':
        comm = input(f'{Fore.GREEN}' + text + Style.RESET_ALL)
    elif color.upper() == 'BLUE':
        comm = input(f'{Fore.BLUE}' + text + Style.RESET_ALL)
    return comm
