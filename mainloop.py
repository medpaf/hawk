import os
import readline 

hist_list = []
comm = ''

# Loop function to read commands and act accordingly
def handleCommands():
        global hist_list  
        global comm 
        while True:
                comm = input('\nVBNetS > ')
                # Save used commands in an array (later) to access history with arrow keys 
                hist_list.append(comm.strip())
        
                if comm.strip() == 'clear':
                        os.system('clear')
                elif comm.strip() == 'history':
                        print('Last commands:')
                        for i in range(0, len(hist_list)-1):
                                print(hist_list[i]) 
                else:
                        os.system(f'python3 testrun.py {comm}')      




