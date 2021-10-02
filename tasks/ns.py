import socket
import sys
import requests
import ipinfo

token = '8d53c2357c2a13'
handler = ipinfo.getHandler(token)

def ns(str):
    try:
        addr = socket.gethostbyname(str)
        name = socket.gethostbyaddr(str)
        details = handler.getDetails(addr)
    except Exception as e:
        e = sys.exc_info()[1]
        print(f'{e}')
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
        print(f'{e}')
        sys.exit(1)

# Function to return an IP address URL:
def nsconvurl(str):
    try:
        return socket.gethostbyaddr(str)
    except:
        e = sys.exc_info()[1]
        print(f'{e}')
        sys.exit(1)
