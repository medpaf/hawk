import socket
import sys
import multiprocessing
from colorama import Fore, Back, Style

def bannerWithPort(host, port):

    socket.setdefaulttimeout(2)
    sckt = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    try:
        
        print(f'[{Fore.YELLOW}?{Style.RESET_ALL}] Connecting to {Fore.YELLOW}{host}{Style.RESET_ALL} on port {Fore.YELLOW}{port}{Style.RESET_ALL}...')
        sckt.connect((host, port))
        sckt.send('WhoAreYou\r\n'.encode())
        banner = sckt.recv(1024)
        
    except KeyboardInterrupt:
        sys.exit('^C\n')
    except Exception as e:
        e = sys.exc_info()[1]
        print(f'[{Fore.RED}!{Style.RESET_ALL}] Error: {Fore.RED}{e}{Style.RESET_ALL}')
    else:
        sckt.close()
        print(f'[{Fore.GREEN}+{Style.RESET_ALL}] Banner of {Fore.YELLOW}{host}{Style.RESET_ALL} on port {Fore.YELLOW}{port}{Style.RESET_ALL}: \n{Fore.GREEN}{banner.decode()}{Style.RESET_ALL}\n')
