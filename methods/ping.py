import os

def ping(str):
    print('Ping will start. Press CTRL + C to cancel.')
    os.system(f'ping {str}')