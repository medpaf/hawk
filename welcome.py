import random
from color import printcolor

def intro1():
    print('\n********************************************************')
    print('*   _      _   _____   __    _                _____    *')
    print('*  | |    | | |  __ \ |  \  | |         _    / ____|   *')
    print('*  | |    | | | |_/ / | \ \ | |  ____  | |_ ( (____    *')
    print('*   \ \  / /  |  __ \ | |\ \| | / __ \ |  _| \____ \   *')
    print('*    \ \/ /   | |_/ / | | \ \ |( ____/ | |_   ____) )  *')
    print('*     \__/    |____/  |_|  \__| \____|  \__| |_____/   *')
    print('*                                                      *')
    printcolor('BLUE','*        Very Basic (kind of) Network Scanner          *')
    printcolor('RED','*             Written by Paulo Medeiros                *')
    print('*                                                      *')
    print('********************************************************\n')

def intro2():
    print

def welcome():
    introList=[intro1]
    random.choice(introList)()