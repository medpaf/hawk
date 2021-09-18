import nmap
import sys
import os
import multiprocessing
import socket
from extras import printcolor

scanner = nmap.PortScanner()

def scanStatus(str, inputed):

    try:
        scanner.scan(str, '1', '-v -sT')
    except KeyboardInterrupt:  
        sys.exit('\n^C\n')
    except:
        e = sys.exc_info()
        printcolor('RED', f'\n{e}')
        sys.exit(1)
    else:
        if scanner[str].state() == 'up':
            printcolor('GREEN', f'Status: {str} is {scanner[str].state()}')
        else: 
            printcolor('RED', f'Status: {str} is {scanner[str].state()}')
            sys.exit()

def scan(str, inputed, prstart, prend, scantype):

    scanStatus(str, inputed)
    print('Scan will start. Press CTRL-C to cancel.') 

    try:
        printcolor('YELLOW', f'Scanning {str}:{prstart}-{prend}') 
        scanner.scan(str, f'{prstart}-{prend}', f'-v {scantype}')
    except KeyboardInterrupt: 
        sys.exit('\n^C\n')
    except: 
        e = sys.exc_info()[1]
        printcolor('RED', f'\n{e}')
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
            printcolor('YELLOW', f'Scanning {str}') 
            print('Scan will start. Press CTRL-C to cancel.')
        scanner.scan(str, f'{int}', f'-v {scantype}')
    except KeyboardInterrupt: 
        sys.exit('^C\n')
    except:
        e = sys.exc_info()[1]
        print(f'{e}')
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
        printcolor('YELLOW', f'Scanning for devices on {network} network...') 
        scanner.scan(hosts = network, arguments = '-v -sn')
    except KeyboardInterrupt:
        sys.exit('\n^C\n')
    except: 
        e = sys.exc_info()[1]
        printcolor('RED', f'\n{e}')
    else:
        #print(scanner._scan_result) ###testing
        for host in scanner.all_hosts():
            if scanner[host]['status']['state'] == 'up':
                print(f"{host} \t\t {scanner[host]['vendor']}")
           