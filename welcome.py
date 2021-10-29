import random
from colorama import Fore, Back, Style
from extras import printcolor

def intro1():
    printcolor('RED','\n                                                     ')   
    printcolor('RED','        `/-`                                           ')
    printcolor('RED','         :/:.`                                         ')
    printcolor('RED','         `///:.`..-::::////::::-..`                    ')
    printcolor('RED','          .://////////////////////::-``          ..    ')
    printcolor('RED','           `-/////////////////////////:.`        ::`   ')
    printcolor('RED','       `.`   `-:////////////////////////:.`     `//`   ')
    printcolor('RED','      `:/-`    `.-:///////////////////////-    `://.   ')
    printcolor('RED','     .:///.       ``.-::////////////////:-`   `:///.   ')
    printcolor('RED','    .//////-`       ```.-////////////:-.`    .:////`   ')
    printcolor('RED','   `:///////-```..---:://:--//////:-.`     `-/////-    ')
    print(f'   {Fore.RED}-/////////////::--..``.:///:-.`       `-://///:`{Style.RESET_ALL} {Fore.BLUE}HAWK{Style.RESET_ALL}')
    print(f'  {Fore.RED}`///////:-..```     `-:--.``         `-//:.://:`{Style.RESET_ALL}  Written by {Fore.RED}Paulo Medeiros{Style.RESET_ALL}')
    print(f'  {Fore.RED}`//////. ```                     `.-:/:-` -//-{Style.RESET_ALL}    {Fore.BLUE}github.com/medpaf/hawk{Style.RESET_ALL}')
    printcolor('RED','  `/////. `:/:                 ``.-:/:-.` `-///.       ')
    printcolor('RED','  `////-  `..`                -//:-.``   `:////`       ')
    printcolor('RED','   ://-```.----..`           `:/-``    `.:////:        ')
    printcolor('RED','   `//-::////////:-.         -//`    `.://////.        ')
    printcolor('RED','    -///////////////.       `//.  ``-:///////-         ')
    printcolor('RED','    `-//////////////:`     `:/-``-://///////-`         ')
    printcolor('RED','      .://///////////`   `.://-:///////////.`          ')
    printcolor('RED','       `-///////////:   `-///////////////:`            ')
    printcolor('RED','         .-/////////.``-://////////////:.`             ')
    printcolor('RED','           `.://///..-//////////////:-`                ')
    printcolor('RED','              `.-:://///////////:-.`                   ')
    printcolor('RED','                   ``........``                        ')

def intro2():
    printcolor('RED', '\n    _____________  _______   ________  ________  _______   ________      ')
    printcolor('RED', '   |\   ___\__   \|\  ___ \ |\   ___ \|\   ____\|\  ___ \ |\   ____\     ')
    printcolor('RED', '   \ \  \ \__\ \  \ \   __/|\ \  \__\ \ \  \___|\ \   __/|\ \  \___|     ')
    printcolor('RED', '    \ \  \ |__| \  \ \  \_|/_\ \  \  \ \ \_____  \ \  \_|/_\ \  \        ')
    printcolor('RED', '     \ \  \    \ \  \ \  \_|\ \ \  \__\ \|____|\  \ \  \_|\ \ \  \_____  ')
    printcolor('RED', '      \ \__\    \ \__\ \_______\ \_______\____\_\  \ \_______\ \_______\ ')
    printcolor('RED', '       \|__|     \|__|\|_______|\|_______|\_________\|_______|\|_______| ')
    printcolor('RED', '                                         \|_________| \n                  ')                                                         
    print(f'                        Written by {Fore.RED}Paulo Medeiros{Style.RESET_ALL}              ')
    print(f'             Github repository: {Fore.RED}https://github.com/medpaf/medsec{Style.RESET_ALL}          ')
                                                                                                                                          

def welcome():
    introList=[intro1]
    random.choice(introList)()