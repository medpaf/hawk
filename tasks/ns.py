import socket
import sys
from extras import printcolor

def ns(str):
    try:
        addr = socket.gethostbyname(str)
        name = socket.gethostbyaddr(str)
    except:
        e = sys.exc_info()[1]
        printcolor('RED', f'{e}')
    else:
        print(f'Name: {name}')
        print(f'Address: {addr}\n')

# Function to return an URL IP address
def nsconv(str):
    try:
        return socket.gethostbyname(str)
    except:
        e = sys.exc_info()[1]
        printcolor('RED', f'{e}')
        sys.exit(1)
        
