import socket
import sys
import multiprocessing
from extras import printcolor, animate

def bannerWithPort(host, port):
    socket.setdefaulttimeout(2)
    sckt = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    animateProcess = multiprocessing.Process(target = animate, args = ((f'Connecting to {host} on port {port}',)))
    animateProcess.start()

    try:
        sckt.connect((host, port))
        sckt.send('WhoAreYou\r\n'.encode())
        banner = sckt.recv(1024)
        
    except KeyboardInterrupt:
        # stop process
        animateProcess.kill()
        sys.exit('\n')
    except:
        # stop process
        animateProcess.kill()
        e = sys.exc_info()[1]
        printcolor('RED', f'\n{e}\n')
    else:
        # stop process
        animateProcess.kill()
        sckt.close()
        printcolor('GREEN', f'\n{banner.decode()}\n')
