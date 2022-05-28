import requests
import sys
from threading import Thread, Lock
from queue import Queue
from colorama import Fore, Back, Style

q = Queue()
list_lock = Lock()
discovered_domains = []

def scan_subdomains(domain):
    global q
    while True:
        try:
            # Get the subdomain from the queue
            subdomain = q.get()
            # Scan the subdomain
            url = f"http://{subdomain}.{domain}"
            requests.get(url)
        except requests.ConnectionError:
            pass
        except KeyboardInterrupt:
            sys.exit('^C')
        except Exception as e:
            print(f'[{Fore.RED}!{Style.RESET_ALL}] Error: {Fore.RED}{e}{Style.RESET_ALL}')
        else:
            print(f'[{Fore.GREEN}+{Style.RESET_ALL}] Discovered subdomain: {Fore.GREEN}{url}{Style.RESET_ALL}')
            # Add the subdomain to the global list
            with list_lock:
                discovered_domains.append(url)

        # Scanning of that subdomain complete
        q.task_done()

def main(domain, threads, subdomains):
    global q
    print(f'[{Fore.YELLOW}?{Style.RESET_ALL}] Performing subdomain enumeration on {Fore.YELLOW}{domain}{Style.RESET_ALL}...\nPress CTRL-C to cancel.\nThis might take a while. Looking for subdomains in {Fore.YELLOW}{domain}{Style.RESET_ALL}...')

    # Fill the queue with all the subdomains
    try:
        for subdomain in subdomains:
            q.put(subdomain)

        for thread in range(threads):
            # Start all threads
            worker = Thread(target=scan_subdomains, args=(domain,))
            # Daemon thread (a thread that will end when the main thread ends)
            worker.daemon = True
            worker.start()
    except KeyboardInterrupt:
        sys.exit('^C')
    except Exception as e:
        print(f'[{Fore.RED}!{Style.RESET_ALL}] Error: {Fore.RED}{e}{Style.RESET_ALL}')

def sdenum(domain, wordlist):
    threads = 8

    try:
        main(domain=domain, threads=threads, subdomains=open(wordlist).read().splitlines())
        q.join()

        if len(discovered_domains) > 0:
            if len(discovered_domains) == 1:
                print(f'\nScan completed. {Fore.GREEN}{len(discovered_domains)}{Style.RESET_ALL} subdomain was discovered.\n')
            else:
                print(f'\nScan completed. {Fore.GREEN}{len(discovered_domains)}{Style.RESET_ALL} subdomains were discovered.\n')
        else:
            print(f'Scan completed. No subdomains were discovered.\n')
    except KeyboardInterrupt:
        sys.exit('^C')
    except Exception as e:
        print(f'[{Fore.RED}!{Style.RESET_ALL}] Error: {Fore.RED}{e}{Style.RESET_ALL}')
