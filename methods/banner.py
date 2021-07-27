import socket
import sys

def bannerWithPort(str, int):
    sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sckt.settimeout(8)
    end = False
    print(f'Connecting to {str} on port {int}...')
    try:
        sckt.connect((str, int))
        print(f"{sckt.recv(1024).decode('utf-8')}\n")
    except:
        e = sys.exc_info()[1]
        print(e)