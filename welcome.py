import random
from extras import printcolor

def intro1():
    print('\n********************************************************')
    printcolor('RED', '*  ███    ███ ███████ ██████  ███████ ███████  ██████  *')
    printcolor('RED', '*  ████  ████ ██      ██   ██ ██      ██      ██       *')
    printcolor('RED', '*  ██ ████ ██ █████   ██   ██ ███████ █████   ██       *')
    printcolor('RED', '*  ██  ██  ██ ██      ██   ██      ██ ██      ██       *')
    printcolor('RED', '*  ██      ██ ███████ ██████  ███████ ███████  ██████  *')
    print('*                                                      *')
    printcolor('RED','*             Written by Paulo Medeiros                *')
    print('* Github repository: https://github.com/medpaf/medsec  *')
    print('*                                                      *')
    print('********************************************************\n')

def intro2():
    printcolor('RED', '\n    _____________  _______   ________  ________  _______   ________      ')
    printcolor('RED', '   |\   ___\__   \|\  ___ \ |\   ___ \|\   ____\|\  ___ \ |\   ____\     ')
    printcolor('RED', '   \ \  \ \__\ \  \ \   __/|\ \  \__\ \ \  \___|\ \   __/|\ \  \___|     ')
    printcolor('RED', '    \ \  \ |__| \  \ \  \_|/_\ \  \  \ \ \_____  \ \  \_|/_\ \  \        ')
    printcolor('RED', '     \ \  \    \ \  \ \  \_|\ \ \  \__\ \|____|\  \ \  \_|\ \ \  \_____  ')
    printcolor('RED', '      \ \__\    \ \__\ \_______\ \_______\____\_\  \ \_______\ \_______\ ')
    printcolor('RED', '       \|__|     \|__|\|_______|\|_______|\_________\|_______|\|_______| ')
    printcolor('RED', '                                         \|_________| \n                  ')                                                         
    printcolor('RED','                        Written by Paulo Medeiros              ')
    print('             Github repository: https://github.com/medpaf/medsec          ')
                                                                                                                                          

def welcome():
    introList=[intro1, intro2]
    random.choice(introList)()