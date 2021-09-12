import socket
import sys
import ipinfo
from extras import printcolor

token = '8d53c2357c2a13'
handler = ipinfo.getHandler(token)


def ns(str):
    try:
        addr = socket.gethostbyname(str)
        name = socket.gethostbyaddr(str)
        details = handler.getDetails(addr)
    except:
        e = sys.exc_info()[1]
        printcolor('RED', f'{e}')
    else:
        print(f'Name: {name}')
        print(f'Address: {addr}')
        print(f'Country: {details.country_name}')
        print(f'City: {details.city}')
        print(f'Postal: {details.postal}')
        print(f'Organization: {details.org}')
        print(f'Location: {details.loc}')
        print(f'Timezone: {details.timezone}\n')

# Function to return an URL IP address
def nsconv(str):
    try:
        return socket.gethostbyname(str)
    except:
        e = sys.exc_info()[1]
        printcolor('RED', f'{e}')
        sys.exit(1)
        
