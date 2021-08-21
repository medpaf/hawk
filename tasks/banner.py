import socket
import sys
import multiprocessing
from extras import printcolor, animate

def bannerWithPort(host, port):
    sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sckt.settimeout(8)

    animateProcess = multiprocessing.Process(target = animate, args = ((f'Connecting to {host} on port {port}',)))
    animateProcess.start()

    try:
        sckt.connect((host, port))
    except KeyboardInterrupt:
        # stop process
        animateProcess.kill()  
        sys.exit('\n')
    except:
        # stop process
        animateProcess.kill()  
        e = sys.exc_info()[1]
        printcolor('RED', f'\n{e}')
    else:
        # stop process`
        animateProcess.kill()  
        printcolor('GREEN',f"\n{sckt.recv(1024).decode('utf-8')}\n")
    