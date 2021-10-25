import os
import sys
import subprocess
from colorama import Fore, Back, Style

def save(cmd, filename):
    # Path to save the file
    # path = path to save file
    try:
        os.system(f'python3 run.py {cmd} > {filename}')
    except Exception as e:
        e = sys.exc_info()[1]
        print(f'[{Fore.RED}!{Style.RESET_ALL}] Error: {Fore.RED}{e}{Style.RESET_ALL}')
    else:
        print(f'[{Fore.GREEN}+{Style.RESET_ALL}] Succesfully saved {Fore.GREEN}{filename}{Style.RESET_ALL} output file.') 
    
 