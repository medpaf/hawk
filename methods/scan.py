import nmap
import sys

scanner = nmap.PortScanner()

def scanStatus(str, inputed):
    print(f'Checking status of {inputed}...')
    try:
        scanner.scan(str, '1', '-v -sT')
    except:
        e = sys.exc_info()
        print(e)
        sys.exit(1)
    else:
        print(f'Status: {str} is {scanner[str].state()}')

def scan(str, inputed, prstart, prend, scantype):
    scanStatus(str, inputed)
    print(f'Scanning {str}:{prstart}-{prend}...')
    try:
        scanner.scan(str, f'{prstart}-{prend}', f'-v {scantype}')
    except:
        e = sys.exc_info()[1]
        print(e)
    else:
        if len(scanner[str].all_protocols()) == 0:
            print('No port(s) found.')
        else:
            for protocol in scanner[str].all_protocols():
                if scanner[str][protocol].keys():
                    print(f'Protocol: {protocol.upper()}')
                    print('\n PORT     \t\tSTATE     \t\tSERVICE')
                    for port in scanner[str][protocol].keys():
                        print(f" {port}      \t\t{scanner[str][protocol][port]['state']}       \t\t{scanner[str][protocol][port]['name']}")
            
def scanWithPort(str, inputed, int, i, j, scantype):
    if j == 0:
        scanStatus(str, inputed)
        print(f'Scanning {str}...')
    try:
        scanner.scan(str, f'{int}', f'-v {scantype}')
    except:
        e = sys.exc_info()[1]
        print(e)
    else:
        for protocol in scanner[str].all_protocols():
            if scanner[str][protocol].keys():
                if j == 0:
                    print(f'Protocol: {protocol.upper()}')
                    print('\n PORT     \t\tSTATE     \t\tSERVICE')
                for port in scanner[str][protocol].keys():
                    print(f" {port}      \t\t{scanner[str][protocol][port]['state']}       \t\t{scanner[str][protocol][port]['name']}")

