import random

def intro1():
    print('\n********************************************************')
    print('*   _      _   _____   __    _                _____    *')
    print('*  | |    | | |  __ \ |  \  | |         _    / ____|   *')
    print('*  | |    | | | |_/ / | \ \ | |  ____  | |_ ( (____    *')
    print('*   \ \  / /  |  __ \ | |\ \| | / __ \ |  _| \____ \   *')
    print('*    \ \/ /   | |_/ / | | \ \ |( ____/ | |_   ____) )  *')
    print('*     \__/    |____/  |_|  \__| \____|  \__| |_____/   *')
    print('*                                                      *')
    print('*        Very Basic (kind of) Network Scanner          *')
    print('*             Written by Paulo Medeiros                *')
    print('*                                                      *')
    print('********************************************************\n')

def welcome():
    introList=[intro1]
    random.choice(introList)()