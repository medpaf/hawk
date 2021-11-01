import random
import time
import subprocess
from colorama import Fore, Back, Style
from extras import printcolor

def intro1():
    printcolor('RED','\n                      `/-`                                       ')
    printcolor('RED','                       :/:.`                                       ')
    printcolor('RED','                       `///:.`..-::::////::::-..                   ')
    printcolor('RED','                        .://////////////////////::-            ..  ')
    printcolor('RED','                         `-/////////////////////////:.         ::` ')
    printcolor('RED','                     `.`   `-:////////////////////////:.      `//` ')
    printcolor('RED','                    `:/-`    `.-:///////////////////////-    `://. ')
    printcolor('RED','                   .:///.       ``.-::////////////////:-`   `:///. ')
    printcolor('RED','                  .//////-`       ```.-////////////:-.`    .:////` ')
    printcolor('RED','                 `:///////-```.....:://:--//////:-.`     `-/////-  ')
    printcolor('RED','                 -/////////////::--..``.:///:-.`       `-://///:`   ')
    printcolor('RED','                `///////:-..```     `-:--.``         `-//:.://:`   ')
    printcolor('RED','                `//////. ```                     `.-:/:-` -//-     ')
    printcolor('RED','                `/////. `:/:                 ``.-:/:-.` `-///.     ')
    printcolor('RED','                `////-  `..`                -//:-.``   `:////`     ')
    printcolor('RED','                 ://-```.----..`           `:/-``    `.:////:      ')
    printcolor('RED','                 `//-::////////:-.         -//`    `.://////.      ')
    printcolor('RED','                  -///////////////.       `//.  ``-:///////-       ')
    printcolor('RED','                  `-//////////////:`     `:/-``-://///////-`       ')
    printcolor('RED','                    .://///////////`   `.://-:///////////.`        ')
    printcolor('RED','                     `-///////////:   `-///////////////:`          ')
    printcolor('RED','                       .-/////////.``-://////////////:.`           ')
    printcolor('RED','                         `.://///..-//////////////:-`              ')
    printcolor('RED','                           `.-:://///////////:-.`                  ')
    printcolor('RED','                               ``........``                        ')                                                                                                                             

def welcome():
    subprocess.call(['clear'])
    introList=[intro1]
    random.choice(introList)()
    time.sleep(3)
    subprocess.call(['clear'])