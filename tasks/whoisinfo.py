import whois
import sys
from colorama import Fore, Back, Style

def whoisinfo(host):

    try:
        print(f'[{Fore.YELLOW}?{Style.RESET_ALL}] WHOIS info on {Fore.YELLOW}{host}{Style.RESET_ALL}...')    
        whois_info = whois.whois(host)
    except Exception as e:
        print(f'[{Fore.RED}!{Style.RESET_ALL}] Error: {e}')
    else:
        if isinstance(whois_info.domain_name, str):
            print(f'[{Fore.GREEN}+{Style.RESET_ALL}] Domain name: {Fore.GREEN}{whois_info.domain_name}{Style.RESET_ALL}')
        else:
            print(f'[{Fore.GREEN}+{Style.RESET_ALL}] Domain names')
            whois_checker(host, whois_info.domain_name)

        print(f'[{Fore.GREEN}+{Style.RESET_ALL}] Registar: {Fore.GREEN}{whois_info.registrar}{Style.RESET_ALL}')
        print(f'[{Fore.GREEN}+{Style.RESET_ALL}] WHOIS server: {Fore.GREEN}{whois_info.whois_server}{Style.RESET_ALL}')

        print(f'[{Fore.GREEN}+{Style.RESET_ALL}] Name servers')
        whois_checker(host, whois_info.name_servers)

        if isinstance(whois_info.creation_date, list):
            print(f'[{Fore.GREEN}+{Style.RESET_ALL}] Creation dates')
            whois_checker(host, whois_info.creation_date)
        else:
            print(f'[{Fore.GREEN}+{Style.RESET_ALL}] Creation date: {Fore.GREEN}{whois_info.creation_date}{Style.RESET_ALL}')
            
        if isinstance(whois_info.updated_date, list):
            print(f'[{Fore.GREEN}+{Style.RESET_ALL}] Updated dates')
            whois_checker(host, whois_info.updated_date)
        else:
            print(f'[{Fore.GREEN}+{Style.RESET_ALL}] Updated date: {Fore.GREEN}{whois_info.updated_date}{Style.RESET_ALL}')

        if isinstance(whois_info.expiration_date, list):
            print(f'[{Fore.GREEN}+{Style.RESET_ALL}] Expiration dates')
            whois_checker(host, whois_info.expiration_date)
        else:
            print(f'[{Fore.GREEN}+{Style.RESET_ALL}] Expiration date: {Fore.GREEN}{whois_info.expiration_date}{Style.RESET_ALL}')

        print(f'[{Fore.GREEN}+{Style.RESET_ALL}] Status')
        whois_checker(host, whois_info.status)

        if isinstance(whois_info.emails, list):
            print(f'[{Fore.GREEN}+{Style.RESET_ALL}] Emails')
            whois_checker(host, whois_info.emails)
        else:
            print(f'[{Fore.GREEN}+{Style.RESET_ALL}] Email: {Fore.GREEN}{whois_info.emails}{Style.RESET_ALL}')

        if isinstance(whois_info.org, list):
            print(f'[{Fore.GREEN}+{Style.RESET_ALL}] Organizations')
            whois_checker(host, whois_info.org)
        else:
            print(f'[{Fore.GREEN}+{Style.RESET_ALL}] Organization: {Fore.GREEN}{whois_info.org}{Style.RESET_ALL}')

        print(f'[{Fore.GREEN}+{Style.RESET_ALL}] State: {Fore.GREEN}{whois_info.state}{Style.RESET_ALL}')
        print(f'[{Fore.GREEN}+{Style.RESET_ALL}] Country: {Fore.GREEN}{whois_info.country}{Style.RESET_ALL}\n')

def whois_checker(host, dictionary):

    try:
        length = len(dictionary)
    except:
        print(f'\t{Fore.GREEN}{dictionary}{Style.RESET_ALL}')
    else: 
        for value in dictionary:
            print(f'\t{Fore.GREEN}{value}{Style.RESET_ALL}')

        