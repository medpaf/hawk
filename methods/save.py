import os
import sys
import subprocess
from extras import printcolor

def save(comm, filename):
    # Path to save the file
    #path = 
    try:
        os.system(f'python3 run.py {comm} > {filename}')
    except:
        e = sys.exc_info()[1]
        printcolor('RED', f'{e}')
    else:
        printcolor('GREEN', f'Succesfully saved {filename} output file.') 
    
