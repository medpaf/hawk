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
        print(f'[{Fore.GREEN}+{Style.RESET_ALL}] Name: {Fore.GREEN}{name}{Style.RESET_ALL}')
        print(f'[{Fore.GREEN}+{Style.RESET_ALL}] Address: {Fore.GREEN}{addr}{Style.RESET_ALL}')
        print(f'[{Fore.GREEN}+{Style.RESET_ALL}] Country: {Fore.GREEN}{details.country_name}{Style.RESET_ALL}')
        print(f'[{Fore.GREEN}+{Style.RESET_ALL}] City: {Fore.GREEN}{details.city}{Style.RESET_ALL}')
        print(f'[{Fore.GREEN}+{Style.RESET_ALL}] Postal: {Fore.GREEN}{details.postal}{Style.RESET_ALL}')
        print(f'[{Fore.GREEN}+{Style.RESET_ALL}] Organization: {Fore.GREEN}{details.org}{Style.RESET_ALL}')
        print(f'[{Fore.GREEN}+{Style.RESET_ALL}] Location: {Fore.GREEN}{details.loc}{Style.RESET_ALL}')
        print(f'[{Fore.GREEN}+{Style.RESET_ALL}] Timezone: {Fore.GREEN}{details.timezone}{Style.RESET_ALL}\n')

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
