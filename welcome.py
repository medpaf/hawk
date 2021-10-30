import random
from colorama import Fore, Back, Style
from extras import printcolor

def intro1():
    printcolor('RED','\n                        `/-`                                       ')
    printcolor('RED','                         :/:.`                                       ')
    printcolor('RED','                         `///:.`..-::::////::::-..                   ')
    printcolor('RED','                          .://////////////////////::-``          ..  ')
    printcolor('RED','                           `-/////////////////////////:.`        ::` ')
    printcolor('RED','                       `.`   `-:////////////////////////:.`     `//` ')
    printcolor('RED','                      `:/-`    `.-:///////////////////////-    `://. ')
    printcolor('RED','                     .:///.       ``.-::////////////////:-`   `:///. ')
    printcolor('RED','                    .//////-`       ```.-////////////:-.`    .:////` ')
    printcolor('RED','                   `:///////-```..---:://:--//////:-.`     `-/////-  ')
    printcolor('RED','                  -/////////////::--..``.:///:-.`       `-://///:`   ')
    printcolor('RED','                  `///////:-..```     `-:--.``         `-//:.://:`   ')
    printcolor('RED','                  `//////. ```                     `.-:/:-` -//-     ')
    printcolor('RED','                  `/////. `:/:                 ``.-:/:-.` `-///.     ')
    printcolor('RED','                  `////-  `..`                -//:-.``   `:////`     ')
    printcolor('RED','                   ://-```.----..`           `:/-``    `.:////:      ')
    printcolor('RED','                   `//-::////////:-.         -//`    `.://////.      ')
    printcolor('RED','                    -///////////////.       `//.  ``-:///////-       ')
    printcolor('RED','                    `-//////////////:`     `:/-``-://///////-`       ')
    printcolor('RED','                      .://///////////`   `.://-:///////////.`        ')
    printcolor('RED','                       `-///////////:   `-///////////////:`          ')
    printcolor('RED','                         .-/////////.``-://////////////:.`           ')
    printcolor('RED','                           `.://///..-//////////////:-`              ')
    printcolor('RED','                             `.-:://///////////:-.`                  ')
    printcolor('RED','                                 ``........``                        ')                                                                                                                             

def welcome():
    introList=[intro1]
    random.choice(introList)()