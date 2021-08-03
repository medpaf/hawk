import os
import sys
import readline 
from welcome import intro1, welcome
from extras import printcolor, inputcolor
from run import *

hist_list = []
comm = ''

# Loop function to read commands and act accordingly
def handleCommands():
        global hist_list  
        global comm 
        while True:
                comm = inputcolor('RED', 'VBNetS > ')
                hist_list.append(comm.strip())
                if comm.strip() == 'clear':
                        os.system('clear')
                elif comm.strip() == 'history':
                        print('Last commands:')
                        for i in range(0, len(hist_list)-1):
                                print(hist_list[i]) 
                else:
                        os.system(f'python3 run.py {comm}')      

def main():
    # if there are no arguments run the welcome() function
    if len(sys.argv) == 1:
        welcome()
    handleCommands()

main()