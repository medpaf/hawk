import socket
import sys
import requests
import ipinfo
from colorama import Fore, Back, Style

token = '8d53c2357c2a13'
handler = ipinfo.getHandler(token)

def ns(str):
    try:
        addr = socket.gethostbyname(str)
        name = socket.gethostbyaddr(str)
        details = handler.getDetails(addr)
    except Exception as e:
        e = sys.exc_info()[1]
        print(f'[{Fore.RED}!{Style.RESET_ALL}] Error: {Fore.RED}{e}{Style.RESET_ALL}')
    else:
        print(f'[{Fore.GREEN}+{Style.RESET_ALL}] Name: {name}')
        print(f'[{Fore.GREEN}+{Style.RESET_ALL}] Address: {addr}')
        print(f'[{Fore.GREEN}+{Style.RESET_ALL}] Country: {details.country_name}')
        print(f'[{Fore.GREEN}+{Style.RESET_ALL}] City: {details.city}')
        print(f'[{Fore.GREEN}+{Style.RESET_ALL}] Postal: {details.postal}')
        print(f'[{Fore.GREEN}+{Style.RESET_ALL}] Organization: {details.org}')
        print(f'[{Fore.GREEN}+{Style.RESET_ALL}] Location: {details.loc}')
        print(f'[{Fore.GREEN}+{Style.RESET_ALL}] Timezone: {details.timezone}\n')

# Function to return IP address of an URL
def nsconv(str):
    try:
        return socket.gethostbyname(str)
    except Exception as e:
        e = sys.exc_info()[1]
        print(f'[{Fore.RED}!{Style.RESET_ALL}] Error: {Fore.RED}{e}{Style.RESET_ALL}')
        sys.exit(1)

# Function to return URL of an IP address:
def nsconvurl(str):
    try:
        return socket.gethostbyaddr(str)
    except Exception as e:
        e = sys.exc_info()[1]
        print(f'[{Fore.RED}!{Style.RESET_ALL}] Error: {Fore.RED}{e}{Style.RESET_ALL}')
        sys.exit(1)
