import requests
import sys
from colorama import Fore, Back, Style

def dirbust(domain, wordlist):

    print(f'[{Fore.YELLOW}?{Style.RESET_ALL}] Performing directory busting on {Fore.YELLOW}{domain}{Style.RESET_ALL}...\nPress CTRL-C to cancel.\nThis might take a while. Looking for directories in {Fore.YELLOW}{domain}{Style.RESET_ALL}...')

    # Request Headers
    headers = {
        'User-Agent':'Macintosh Mac OS X'
    }

    # Working with file
    file = open(wordlist,'r')
    lines = file.readlines()

    # Parsing through each word in the wordlist
    try:
        for line in lines:
            line = line.strip("\n")
            r = requests.get('http://'+domain+'/'+line, headers=headers)
            if(r.status_code != 404):
                print(f'[{Fore.GREEN}+{Style.RESET_ALL}] Discovered directory: {Fore.GREEN}http://{domain}/{line}{Style.RESET_ALL} Status code: {Fore.GREEN}{r.status_code}{Style.RESET_ALL}')
    
    except KeyboardInterrupt:
            sys.exit()

    except Exception as e:
        print(f'[{Fore.RED}!{Style.RESET_ALL}] Error: {Fore.RED}{e}{Style.RESET_ALL}')

