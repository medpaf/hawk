import random
from extras import printcolor

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
    print('\n                  ___         ___         ___                 ___  ')  
    print('      ___        /  /\       /  /\       /  /\    ___        /  /\     ')
    print('     /  /\      /  /::\     /  /::|     /  /::\  /__/\      /  /::\    ')
    print('    /  /:/     /  /:/\:\   /  /:|:|    /  /:/\:\ \  \:\    /__/:/\:\   ')
    print('   /  /:/     /  /::\ \:\ /  /:/|:|__ /  /::\ \:\ \__\:\  _\_ \:\ \:\  ')
    print('  /__/:/  ___/__/:/\:\_\:/__/:/ |:| //__/:/\:\ \:\/  /::\/__/\ \:\ \:\ ')
    print('  |  |:| /  /\  \:\ \:\/:\__\/  |:|/:\  \:\ \:\_\/  /:/\:\  \:\ \:\_\/ ')
    print('  |  |:|/  /:/\  \:\_\::/    |  |:/:/ \  \:\ \:\/  /:/__\/\  \:\_\:\   ')
    print('  |__|:|__/:/  \  \:\/:/     |__|::/   \  \:\_\/__/:/      \  \:\/:/   ')
    print('   \__\::::/    \__\::/      /__/:/     \  \:\ \__\/        \  \::/    ')
    print('       ~~~~         ~~       \__\/       \__\/               \__\/\n     ')
    printcolor('BLUE','                Very Basic (kind of) Network Scanner          ')
    printcolor('RED','                     Written by Paulo Medeiros \n               ')
                                                                                                                                          

def welcome():
    introList=[intro1, intro2]
    random.choice(introList)()