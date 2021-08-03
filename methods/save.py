import os
import sys
import subprocess
from extras import printcolor

def save(comm, filename):
    print(f'#testing: inside save function... command = {comm}') ###
    print(f'#testing: python3 run.py {comm}') ###
    try:
        os.system(f'python3 run.py {comm} > {filename}')
    except:
        e = sys.exc_info()[1]
        printcolor('RED', f'{e}')
    else:
        printcolor('GREEN', f'Saved {filename} output file.') 
    
