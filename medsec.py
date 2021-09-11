import os
import sys
import readline 
from welcome import welcome
from extras import printcolor, inputcolor
from run import *

hist_list = []
comm = ''

# Loop function to read commands and act accordingly
def handleCommands():
        global hist_list  
        global comm 
        while True:
                try:
                        comm = input('\nMedSec > ')
                        if comm != 'history':
                                hist_list.append(comm.strip())
                        elif comm.strip() == 'clear':
                                os.system('clear')
                        if comm.strip() == 'history':
                                if len(hist_list) > 0:
                                        print('Last commands:')
                                        for i in range(0, len(hist_list)):
                                                print(hist_list[i]) 
                                else:
                                        print('No commands history.')
                        else:
                                os.system(f'python3 run.py {comm}') 
                except KeyboardInterrupt:
                        sys.exit('\n^C\n')

def main():
    # if no arguments are present, run the welcome() function
    if len(sys.argv) == 1:
        welcome()
    handleCommands()

main()