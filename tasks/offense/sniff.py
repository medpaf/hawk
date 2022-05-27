import socket
import struct
import binascii
import sys
import os
from colorama import Fore, Back, Style

def sniff():

    # If not sudo, don't allow to continue
    if not 'SUDO_UID' in os.environ.keys():
        print(f'[{Fore.RED}!{Style.RESET_ALL}] Permission error: {Fore.RED}You need root privileges for this feature.{Style.RESET_ALL}')
        sys.exit()

    try:

        raw_socket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, 
        socket.htons(0x0800))
        
    except socket.error as e:
        print(f'[{Fore.RED}!{Style.RESET_ALL}] Error: [{Fore.RED}{e[1]}{Style.RESET_ALL}')
        sys.exit()
    except KeyboardInterrupt:
        print('Operation was cancelled.')
        sys.exit()
    else:
        while True:
            try:
                packet = raw_socket.recvfrom(2048)
                ethernet_header = packet[0][0:14]
                eth_header = struct.unpack("!6s6s2s", ethernet_header)
                print(f'\nDestination MAC: {binascii.hexlify(eth_header[0]).upper().decode("utf-8")}, Source MAC: {binascii.hexlify(eth_header[1]).upper().decode("utf-8")}, Type: {binascii.hexlify(eth_header[2]).decode("utf-8")}')
                ip_header = packet[0][14:34]
                ip_hdr = struct.unpack("!12s4s4s", ip_header)
                print(f'Source IP: {socket.inet_ntoa(ip_hdr[1])}, Destination IP: {socket.inet_ntoa(ip_hdr[2])}')
            except KeyboardInterrupt:
                sys.exit('\n')
            except Exception as e:
                print(f'[{Fore.RED}!{Style.RESET_ALL}] Error: {Fore.RED}{e}{Style.RESET_ALL}')