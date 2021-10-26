import whois
from colorama import Fore, Back, Style

def whoisinfo(host):
    
    try:
        whois_info = whois.whois(host)
    except Exception as e:
        print(f'[{Fore.RED}!{Style.RESET_ALL}] Error: {e}')
    else:
        print(f'[{Fore.GREEN}+{Style.RESET_ALL}] Domain name')
        whois_checker(host, whois_info.domain_name)

        print(f'[{Fore.GREEN}+{Style.RESET_ALL}] Registar: {Fore.GREEN}{whois_info.registrar}{Style.RESET_ALL}')
        print(f'[{Fore.GREEN}+{Style.RESET_ALL}] WHOIS server: {Fore.GREEN}{whois_info.whois_server}{Style.RESET_ALL}')

        print(f'[{Fore.GREEN}+{Style.RESET_ALL}] Name servers')
        whois_checker(host, whois_info.name_servers)

        print(f'[{Fore.GREEN}+{Style.RESET_ALL}] Creation date')
        whois_checker(host, whois_info.creation_date)

        print(f'[{Fore.GREEN}+{Style.RESET_ALL}] Updated date')
        whois_checker(host, whois_info.updated_date)

        print(f'[{Fore.GREEN}+{Style.RESET_ALL}] Expiration date')
        whois_checker(host, whois_info.expiration_date)

        print(f'[{Fore.GREEN}+{Style.RESET_ALL}] Status')
        whois_checker(host, whois_info.status)

        print(f'[{Fore.GREEN}+{Style.RESET_ALL}] Emails')
        whois_checker(host, whois_info.emails)
        
        print(f'[{Fore.GREEN}+{Style.RESET_ALL}] Organization: {Fore.GREEN}{whois_info.org}{Style.RESET_ALL}')
        print(f'[{Fore.GREEN}+{Style.RESET_ALL}] State: {Fore.GREEN}{whois_info.state}{Style.RESET_ALL}')
        print(f'[{Fore.GREEN}+{Style.RESET_ALL}] Country: {Fore.GREEN}{whois_info.country}{Style.RESET_ALL}')

def whois_checker(host, dictionary):

    try:
        length = len(dictionary)
    except:
        print(f'\t{Fore.GREEN}{dictionary}{Style.RESET_ALL}')
    else: 
        for value in dictionary:
            print(f'\t{Fore.GREEN}{value}{Style.RESET_ALL}')
