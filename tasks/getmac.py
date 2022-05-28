from scapy.all import *
import sys
from colorama import Fore, Back, Style

def getmac(host_ip, host_count):

    # If not sudo, don't allow to continue
    if not 'SUDO_UID' in os.environ.keys():
        print(f'[{Fore.RED}!{Style.RESET_ALL}] Permission error: {Fore.RED}You need root privileges for this feature.{Style.RESET_ALL}')
        sys.exit()

    try:
        
        if host_count > 0:
            print(f'\n[{Fore.YELLOW}?{Style.RESET_ALL}] Trying to get MAC address of {Fore.YELLOW}{host_ip}{Style.RESET_ALL}...')
        else:
            print(f'[{Fore.YELLOW}?{Style.RESET_ALL}] Trying to get MAC address of {Fore.YELLOW}{host_ip}{Style.RESET_ALL}...')
        
        packet = Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(op='who-has', pdst = host_ip)
        resp, _ = srp(packet, timeout = 2, retry = 10, verbose = False)

        if resp:
            for _, r in resp:
                print(f'[{Fore.GREEN}+{Style.RESET_ALL}] MAC address of {Fore.YELLOW}{host_ip}{Style.RESET_ALL}: {Fore.GREEN}{r[Ether].src.upper()}{Style.RESET_ALL}')
        else:
                print(f'[{Fore.RED}!{Style.RESET_ALL}] {Fore.RED}No MAC address for{Style.RESET_ALL} {Fore.YELLOW}{host_ip}{Style.RESET_ALL} {Fore.RED}was found.{Style.RESET_ALL}')

    except Exception as e:
        print(f'[{Fore.RED}!{Style.RESET_ALL}] Error: {Fore.RED}{e}{Style.RESET_ALL}')

    except KeyboardInterrupt:
        sys.exit('^C\n')
