import subprocess
import os
from colorama import Fore, Back, Style

def turn_monitor(iface, default_iface = ''):

    # If not sudo, don't allow to continue
    if not 'SUDO_UID' in os.environ.keys():
        print(f'[{Fore.RED}!{Style.RESET_ALL}] Permission error: {Fore.RED}You need root privileges for this feature.{Style.RESET_ALL}')
        sys.exit()

    if default_iface != '':
        iface = default_iface

    try:

        subprocess.call(['sudo', 'systemctl', 'stop', 'NetworkManager'])
        subprocess.call(['sudo', 'ifconfig', iface, 'down'])
        subprocess.call(['sudo','iwconfig', iface, 'mode', 'monitor'])
        subprocess.call(['sudo','ifconfig', iface, 'up'])

    except Exception as e:
        print(f'[{Fore.RED}!{Style.RESET_ALL}] Error: {Fore.RED}{e}{Style.RESET_ALL}')
    else:
        output = str(subprocess.check_output(['iwconfig', iface,]))
        if 'Monitor' in output:
            print(f'[{Fore.GREEN}+{Style.RESET_ALL}] {Fore.GREEN}{iface}{Style.RESET_ALL} succesfully changed to {Fore.GREEN}monitor{Style.RESET_ALL} mode.')
        else:
            print(f"[{Fore.RED}!{Style.RESET_ALL}] Couldn't change to monitor mode.")


def turn_managed(iface, default_iface = ''):

    # If not sudo, don't allow to continue
    if not 'SUDO_UID' in os.environ.keys():
        print(f'[{Fore.RED}!{Style.RESET_ALL}] Permission error: {Fore.RED}You need root privileges for this feature.{Style.RESET_ALL}')
        sys.exit()

    if default_iface != '':
        iface = default_iface

    try:

        subprocess.call(['sudo', 'ifconfig', iface, 'down'])
        subprocess.call(['sudo','iwconfig', iface, 'mode', 'managed'])
        subprocess.call(['sudo','ifconfig', iface, 'up'])
        subprocess.call(['sudo', 'systemctl', 'restart', 'NetworkManager'])

    except Exception as e:
        print(f'[{Fore.RED}!{Style.RESET_ALL}] Error: {Fore.RED}{e}{Style.RESET_ALL}')
    else:
        output = str(subprocess.check_output(['iwconfig', iface,]))
        if 'Managed' in output:
            print(f'[{Fore.GREEN}+{Style.RESET_ALL}] {Fore.GREEN}{iface}{Style.RESET_ALL} succesfully changed to {Fore.GREEN}managed{Style.RESET_ALL} mode.')
        else:
            print(f"[{Fore.RED}!{Style.RESET_ALL}] Couldn't change to managed mode.")