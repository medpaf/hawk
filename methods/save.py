import os
import sys

def save(comm, filename):
    try:
        os.system(f'python3 testrun.py {comm} > {filename}')
    except:
        e = sys.exc_info()[1]
        print(e)
    else:
        print(f'Saved {filename} output file.') ### To be continued
