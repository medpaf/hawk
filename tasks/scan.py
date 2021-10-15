import nmap
import sys
import os
import multiprocessing
import socket
from colorama import Fore, Back, Style

scanner = nmap.PortScanner()

def scanStatus(str, inputed):

    try:
        scanner.scan(str, '1', '-v -sT')
    except KeyboardInterrupt:  
        sys.exit('\n^C\n')
    except Exception as e:
        e = sys.exc_info()
        print(f'[{Fore.RED}!{Style.RESET_ALL}] Error: {Fore.RED}{e}{Style.RESET_ALL}')
        sys.exit(1)
    else:
        if scanner[str].state() == 'up':
            print(f'[{Fore.GREEN}+{Style.RESET_ALL}] Status: {str} is {Fore.GREEN}{scanner[str].state()}{Style.RESET_ALL}.')
        else: 
            print(f'[{Fore.YELLOW}?{Style.RESET_ALL}] Status: {str} is {Fore.RED}{scanner[str].state()}{Style.RESET_ALL}.')
            sys.exit()

def scan(str, inputed, prstart, prend, scantype):

    scanStatus(str, inputed)
    print('Scan will start. Press CTRL-C to cancel.') 

    try:
        print(f'[{Fore.YELLOW}?{Style.RESET_ALL}] Scanning {Fore.YELLOW}{str}{Style.RESET_ALL}:{prstart}-{prend}...') 
        scanner.scan(str, f'{prstart}-{prend}', f'-v {scantype}')
    except KeyboardInterrupt: 
        sys.exit('\n^C\n')
    except Exception as e: 
        e = sys.exc_info()[1]
        print(f'[{Fore.RED}!{Style.RESET_ALL}] Error: {Fore.RED}{e}{Style.RESET_ALL}')
    else:
        if len(scanner[str].all_protocols()) == 0:
            print('No port(s) found.')
        else:
            for protocol in scanner[str].all_protocols():
                if scanner[str][protocol].keys():
                    print(f'\nProtocol: {protocol.upper()}')
                    print('\n PORT     \t\tSTATE     \t\tSERVICE')
                    for port in scanner[str][protocol].keys():
                        print(f" {port}      \t\t{scanner[str][protocol][port]['state']}       \t\t{scanner[str][protocol][port]['name']}")
            
def scanWithPort(str, inputed, int, i, j, scantype):

    try:
        if j == 0:
            scanStatus(str, inputed)
            print(f'[{Fore.YELLOW}?{Style.RESET_ALL}] Scanning {Fore.YELLOW}{str}{Style.RESET_ALL}') 
            print('Scan will start. Press CTRL-C to cancel.')
        scanner.scan(str, f'{int}', f'-v {scantype}')
    except KeyboardInterrupt: 
        sys.exit('^C\n')
    except Exception as e:
        e = sys.exc_info()[1]
        print(f'[{Fore.RED}!{Style.RESET_ALL}] Error: {Fore.RED}{e}{Style.RESET_ALL}')
    else:
        for protocol in scanner[str].all_protocols():
            if scanner[str][protocol].keys():
                if j == 0:
                    print(f'Protocol: {protocol.upper()}')
                    print('\n PORT     \t\tSTATE     \t\tSERVICE')
                for port in scanner[str][protocol].keys():
                    print(f" {port}      \t\t{scanner[str][protocol][port]['state']}       \t\t{scanner[str][protocol][port]['name']}")
            
def scanLocalDevices():
    
    network = input('Please type the network you want to scan (Example: 192.168.1.0/24): ')
    print(f'The network address is {network}')

    try:
        print(f'[{Fore.YELLOW}?{Style.RESET_ALL}] Scanning for devices on {Fore.YELLOW}{network}{Style.RESET_ALL} network...') 
        scanner.scan(hosts = network, arguments = '-v -sn')
    except KeyboardInterrupt:
        sys.exit('\n^C\n')
    except Exception as e: 
        e = sys.exc_info()[1]
        print(f'[{Fore.RED}!{Style.RESET_ALL}] Error: {Fore.RED}{e}{Style.RESET_ALL}')
    else:
        for host in scanner.all_hosts():
            if scanner[host]['status']['state'] == 'up':
                print(f"[{Fore.GREEN}+{Style.RESET_ALL}] {host}      \t\t {scanner[host]['vendor']}")
           