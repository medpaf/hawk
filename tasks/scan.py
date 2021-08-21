import nmap
import sys
import multiprocessing
from extras import printcolor, animate

scanner = nmap.PortScanner()

def scanStatus(str, inputed):

    animateProcess = multiprocessing.Process(target = animate, args = ((f'Checking status of {inputed}',)))
    animateProcess.start()

    try:
        scanner.scan(str, '1', '-v -sT')
    except KeyboardInterrupt:  
        # stop process     
        animateProcess.kill()  
        sys.exit('\n^C\n')
    except:
        # stop process
        animateProcess.kill()  
        e = sys.exc_info()
        printcolor('RED', f'\n{e}')
        sys.exit(1)
    else:
        # stop process
        animateProcess.kill() 
        if scanner[str].state() == 'up':
            printcolor('GREEN', f'\nStatus: {str} is {scanner[str].state()}')
        else: 
            printcolor('RED', f'\nStatus: {str} is {scanner[str].state()}')

def scan(str, inputed, prstart, prend, scantype):
    scanStatus(str, inputed)
    print('Scan will start. Press CTRL-C to cancel.')

    animateProcess = multiprocessing.Process(target = animate, args = ((f'Scanning {str}:{prstart}-{prend}',)))
    animateProcess.start()
    
    try:
        scanner.scan(str, f'{prstart}-{prend}', f'-v {scantype}')
    except KeyboardInterrupt:
        # stop process
        animateProcess.kill()  
        sys.exit('\n^C\n')
    except:
        # stop process
        animateProcess.kill()  
        e = sys.exc_info()[1]
        printcolor('RED', f'\n{e}')
    else:
        # stop process
        animateProcess.kill() 
        if len(scanner[str].all_protocols()) == 0:
            print('\nNo port(s) found.')
        else:
            for protocol in scanner[str].all_protocols():
                if scanner[str][protocol].keys():
                    print(f'\nProtocol: {protocol.upper()}')
                    print('\n PORT     \t\tSTATE     \t\tSERVICE')
                    for port in scanner[str][protocol].keys():
                        print(f" {port}      \t\t{scanner[str][protocol][port]['state']}       \t\t{scanner[str][protocol][port]['name']}")
            
def scanWithPort(str, inputed, int, i, j, scantype):

    animateProcess = multiprocessing.Process(target = animate, args = ((f'Scanning {str}',)))
    animateProcess.start()

    if j == 0:
        scanStatus(str, inputed)
        print('Scan will start. Press CTRL-C to cancel.')
    try:
        scanner.scan(str, f'{int}', f'-v {scantype}')
    except KeyboardInterrupt:
        # stop process
        animateProcess.kill()  
        sys.exit('^C\n')
    except:
        # stop process
        animateProcess.kill() 
        e = sys.exc_info()[1]
        print(f'{e}')
    else:
        # stop process
        animateProcess.kill() 
        for protocol in scanner[str].all_protocols():
            if scanner[str][protocol].keys():
                if j == 0:
                    print(f'Protocol: {protocol.upper()}')
                    print('\n PORT     \t\tSTATE     \t\tSERVICE')
                for port in scanner[str][protocol].keys():
                    print(f" {port}      \t\t{scanner[str][protocol][port]['state']}       \t\t{scanner[str][protocol][port]['name']}")
            

