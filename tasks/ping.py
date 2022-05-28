import sys
from scapy.all import *
from colorama import Fore, Back, Style
from tasks.ns import nsconv

def ping(host, host_count):
    try:
        print(f'[{Fore.YELLOW}?{Style.RESET_ALL}] Pinging {Fore.YELLOW}{host}{Style.RESET_ALL}...')
        ip = nsconv(host)
        icmp = IP(dst=ip)/ICMP()
        resp = sr1(icmp, timeout=10, verbose= False)
        if resp == None:
            if host_count > 0:
                print(f'\n[{Fore.RED}!{Style.RESET_ALL}] {Fore.YELLOW}{host}{Style.RESET_ALL} is {Fore.RED}down{Style.RESET_ALL}.')
            else:
                print(f'[{Fore.RED}!{Style.RESET_ALL}] {Fore.YELLOW}{host}{Style.RESET_ALL} is {Fore.RED}down{Style.RESET_ALL}.')
        else:
            if host_count > 0:
                print(f'\n[{Fore.GREEN}+{Style.RESET_ALL}] {Fore.YELLOW}{host}{Style.RESET_ALL} is {Fore.GREEN}up{Style.RESET_ALL}.')
            else:
                print(f'[{Fore.GREEN}+{Style.RESET_ALL}] {Fore.YELLOW}{host}{Style.RESET_ALL} is {Fore.GREEN}up{Style.RESET_ALL}.')
    except Exception as e:
        print(f'[{Fore.RED}!{Style.RESET_ALL}] Error: {Fore.RED}{e}{Style.RESET_ALL}')
    except KeyboardInterrupt:
        sys.exit('^C\n')
    


