import subprocess
import os
import sys
from colorama import Fore, Back, Style

def macspoof(mac, iface, default_iface=''):
    
    # If not sudo, don't allow to continue
    if not 'SUDO_UID' in os.environ.keys():
        print(f'[{Fore.RED}!{Style.RESET_ALL}] Permission error: {Fore.RED}You need root privileges for this feature.{Style.RESET_ALL}')
        sys.exit()

    try:

        if default_iface != '':
            iface = default_iface

        subprocess.call(['sudo', 'ifconfig', iface, 'down'])
        subprocess.call(['sudo','ifconfig', iface, 'hw', 'ether', mac])
        subprocess.call(['sudo','ifconfig', iface, 'up'])

    except Exception as e:
        print(f'[{Fore.RED}!{Style.RESET_ALL}] Error: {Fore.RED}{e}{Style.RESET_ALL}')
    else:
        
        output = str(subprocess.check_output(['ifconfig', iface,]))

        if f'{mac}' in output:
            print(f'[{Fore.GREEN}+{Style.RESET_ALL}] MAC succesfully changed to {Fore.GREEN}{mac}{Style.RESET_ALL} on {Fore.GREEN}{iface}{Style.RESET_ALL}')
        else:
            print(f"[{Fore.RED}!{Style.RESET_ALL}] Couldn't change MAC address.")
