import socket
import sys

def ns(str):
    try:
        addr = socket.gethostbyname(str)
    except:
        e = sys.exc_info()[1]
        print(e)
    else:
        print(f'Name: {str}')
        print(f'Address: {addr}\n')

def nsconv(str):
    try:
        return socket.gethostbyname(str)
    except:
        e = sys.exc_info()[1]
        print(e)
        sys.exit(1)
        
