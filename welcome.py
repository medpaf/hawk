import random
import time
import subprocess
from colorama import Fore, Back, Style

def intro1():
    print()
    print(f'{Fore.LIGHTRED_EX}     ``                                 {Style.RESET_ALL}')    
    print(f'{Fore.LIGHTRED_EX}     `/-`                               {Style.RESET_ALL}')
    print(f'{Fore.LIGHTRED_EX}      -/:.` ``..-----..``               {Style.RESET_ALL}{Fore.WHITE} __  __  ______  __     __  __  __    {Style.RESET_ALL}')
    print(f'{Fore.LIGHTRED_EX}      `-///://///////////:-.`        .` {Style.RESET_ALL}{Fore.WHITE}/\ \_\ \/\  __ \/\ \  _ \ \/\ \/ /    {Style.RESET_ALL}')
    print(f'{Fore.LIGHTRED_EX}        .:///////////////////-`      :- {Style.RESET_ALL}{Fore.WHITE}\ \  __ \ \  __ \ \ \/ ".\ \ \  _"-.  {Style.RESET_ALL}')
    print(f'{Fore.LIGHTRED_EX}    `-.   .-://////////////////-`   ./: {Style.RESET_ALL}{Fore.WHITE} \ \_\ \_\ \_\ \_\ \__/".~\_\ \_\ \_\ {Style.RESET_ALL}')
    print(f'{Fore.LIGHTRED_EX}   .//:`     `.:://////////////-`  .//: {Style.RESET_ALL}{Fore.WHITE}  \/_/\/_/\/_/\/_/\/_/   \/_/\/_/\/_/ {Style.RESET_ALL}')
    print(f'{Fore.LIGHTRED_EX}  .////:`      ``-://///////-.`  `-///- {Style.RESET_ALL}')
    print(f'{Fore.LIGHTRED_EX} `///////---::/::-.-:///:-`     .:///:` {Style.RESET_ALL}')
    print(f'{Fore.LIGHTRED_EX} -/////:--..``` `.---.`      `.::-:/:`  {Style.RESET_ALL}{Fore.CYAN}Repo{Style.RESET_ALL}: https://github.com/medpaf/hawk')
    print(f'{Fore.LIGHTRED_EX} :///:.`..                `.:/:.`-/:`   {Style.RESET_ALL}{Fore.CYAN}Email{Style.RESET_ALL}: pafmed@outlook.com') 
    print(f'{Fore.LIGHTRED_EX} :///` .:.            `.-::-.` `-//-    {Style.RESET_ALL}{Fore.CYAN}License{Style.RESET_ALL}: MIT')
    print(f'{Fore.LIGHTRED_EX} .//. `....``         -/-`    .:///.    {Style.RESET_ALL}')
    print(f'{Fore.LIGHTRED_EX} `:/-:///////:`      `/:`   .:////:`    {Style.RESET_ALL}{Fore.CYAN}Configuration file{Style.RESET_ALL}: files/conf.py')
    print(f'{Fore.LIGHTRED_EX}  `////////////`    `:/` `-://////`     {Style.RESET_ALL}')
    print(f'{Fore.LIGHTRED_EX}   `://////////.   `:/--:///////:`      {Style.RESET_ALL}')
    print(f'{Fore.LIGHTRED_EX}    `-/////////` `.////////////.`       {Style.RESET_ALL}{Fore.BLACK}███{Fore.RED}███{Fore.GREEN}███{Fore.YELLOW}███{Fore.LIGHTBLUE_EX}███{Fore.MAGENTA}███{Fore.CYAN}███{Fore.WHITE}███')
    print(f'{Fore.LIGHTRED_EX}      `.://///.`-://////////:.`         {Style.RESET_ALL}{Fore.LIGHTBLACK_EX}███{Fore.LIGHTRED_EX}███{Fore.LIGHTGREEN_EX}███{Fore.LIGHTYELLOW_EX}███{Fore.BLUE}███{Fore.LIGHTMAGENTA_EX}███{Fore.LIGHTCYAN_EX}███{Fore.LIGHTWHITE_EX}███')
    print(f'{Fore.LIGHTRED_EX}         `.-::://///////:-.`            {Style.RESET_ALL}')
    print(f'{Fore.LIGHTRED_EX}             ``.......``                {Style.RESET_ALL}')                                                                                                                           


def welcome():
    introList=[intro1]
    subprocess.call(['clear'])
    random.choice(introList)()
    time.sleep(2.5)
    subprocess.call(['clear'])

