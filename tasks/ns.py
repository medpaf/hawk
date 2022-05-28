import socket
import sys
import requests
import ipinfo
from colorama import Fore, Back, Style


def ns(host, api_key):

    try:
        print(f'[{Fore.YELLOW}?{Style.RESET_ALL}] DNS check on {Fore.YELLOW}{host}{Style.RESET_ALL}...')
        api_key = api_key
        handler = ipinfo.getHandler(api_key)
        
        addr = socket.gethostbyname(host)
        name = socket.gethostbyaddr(host)
        details = handler.getDetails(addr)
    except Exception as e:
        e = sys.exc_info()[1]
        print(f'[{Fore.RED}!{Style.RESET_ALL}] Error: {Fore.RED}{e}{Style.RESET_ALL}\n')
    else:
        try:
            print(f'[{Fore.GREEN}+{Style.RESET_ALL}] Name: {Fore.GREEN}{name[0]}{Style.RESET_ALL}')
            print(f'[{Fore.GREEN}+{Style.RESET_ALL}] Address: {Fore.GREEN}{addr}{Style.RESET_ALL}')
            print(f'[{Fore.GREEN}+{Style.RESET_ALL}] Country: {Fore.GREEN}{details.country_name}{Style.RESET_ALL}')
            print(f'[{Fore.GREEN}+{Style.RESET_ALL}] City: {Fore.GREEN}{details.city}{Style.RESET_ALL}')
            print(f'[{Fore.GREEN}+{Style.RESET_ALL}] Postal: {Fore.GREEN}{details.postal}{Style.RESET_ALL}')
            print(f'[{Fore.GREEN}+{Style.RESET_ALL}] Organization: {Fore.GREEN}{details.org}{Style.RESET_ALL}')
            print(f'[{Fore.GREEN}+{Style.RESET_ALL}] Location: {Fore.GREEN}{details.loc}{Style.RESET_ALL}')
            print(f'[{Fore.GREEN}+{Style.RESET_ALL}] Timezone: {Fore.GREEN}{details.timezone}{Style.RESET_ALL}\n')
        except Exception as e:
            pass


# Function to return IP address of an URL
def nsconv(host):
    try:
        return socket.gethostbyname(host)
    except Exception as e:
        e = sys.exc_info()[1]
        print(f'[{Fore.RED}!{Style.RESET_ALL}] Error: {Fore.RED}{e}{Style.RESET_ALL}')
        sys.exit(1)
    except KeyboardInterrupt:
        sys.exit('^C\n')

# Function to return URL of an IP address:
def nsconvurl(host):
    try:
        return socket.gethostbyaddr(host)
    except Exception as e:
        e = sys.exc_info()[1]
        print(f'[{Fore.RED}!{Style.RESET_ALL}] Error: {Fore.RED}{e}{Style.RESET_ALL}')
        sys.exit(1)
