import socket
import sys
from extras import printcolor

def bannerWithPort(host, port):
    sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sckt.settimeout(8)
    try:
        print('Banner grabbing will start. Press CTRL-C to cancel.')
        print(f'Connecting to {host} on port {port}...')
        sckt.connect((host, port))
        print(f"{sckt.recv(1024).decode('utf-8')}\n")
    except KeyboardInterrupt:
        sys.exit('\n')
    except:
        e = sys.exc_info()[1]
        printcolor('RED', f'{e}')