import socket
import sys
import multiprocessing
from extras import printcolor

def bannerWithPort(host, port):

    socket.setdefaulttimeout(2)
    sckt = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    try:
        printcolor('YELLOW', f'Connecting to {host} on port {port}...')
        sckt.connect((host, port))
        sckt.send('WhoAreYou\r\n'.encode())
        banner = sckt.recv(1024)
        
    except KeyboardInterrupt:
        sys.exit('\n')
    except:
        e = sys.exc_info()[1]
        printcolor('RED', f'{e}\n')
    else:
        sckt.close()
        printcolor('GREEN', f'{banner.decode()}\n')
