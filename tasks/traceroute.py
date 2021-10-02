import os

def traceroute(host):
    print('Traceroute will start. Press CTRL + C to cancel.')
    os.system(f'traceroute {host}')

