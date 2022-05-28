import requests
import sys
from threading import Thread, Lock
from queue import Queue
from colorama import Fore, Back, Style

q = Queue()
list_lock = Lock()
discovered_directories = []

def scan_directories(host):
    global q
    while True:
        try:
            # Get the directory from the queue
            directory = q.get()
            # Scan the directory
            url = f"http://{host}/{directory}"
            requests.get(url)
        except requests.ConnectionError:
            pass
        except KeyboardInterrupt:
            sys.exit('^C')
        except Exception as e:
            print(f'[{Fore.RED}!{Style.RESET_ALL}] Error: {Fore.RED}{e}{Style.RESET_ALL}')
        else:
            if(requests.get(url).status_code != 404):
                print(f'[{Fore.GREEN}+{Style.RESET_ALL}] Discovered directory: {Fore.GREEN}{url}{Style.RESET_ALL}')
                # Add the directory to the global list
                with list_lock:
                    discovered_directories.append(url)

        # Scanning of that directory complete
        q.task_done()

def main(host, threads, directories):
    global q
    print(f'[{Fore.YELLOW}?{Style.RESET_ALL}] Performing directory busting on {Fore.YELLOW}{host}{Style.RESET_ALL}...\nPress CTRL-C to cancel.\nThis might take a while. Looking for directories in {Fore.YELLOW}{host}{Style.RESET_ALL}...')

    # Fill the queue with all the directories
    try:
        for directory in directories:
            q.put(directory)

        for thread in range(threads):
            # Start all threads
            worker = Thread(target=scan_directories, args=(host,))
            # Daemon thread (a thread that will end when the main thread ends)
            worker.daemon = True
            worker.start()
    except KeyboardInterrupt:
        sys.exit('^C\n')
    except Exception as e:
        print(f'[{Fore.RED}!{Style.RESET_ALL}] Error: {Fore.RED}{e}{Style.RESET_ALL}')

def dirbust(host, wordlist):
    threads = 8

    try:
        main(host=host, threads=threads, directories=open(wordlist).read().splitlines())
        q.join()

        if len(discovered_directories) > 0:
            if len(discovered_directories) == 1:
                print(f'\nScan completed. {Fore.GREEN}{len(discovered_directories)}{Style.RESET_ALL} directory was discovered.\n')
            else:
                print(f'\nScan completed. {Fore.GREEN}{len(discovered_directories)}{Style.RESET_ALL} directories were discovered.\n')
        else:
            print(f'Scan completed. No directories were discovered.\n')
    except KeyboardInterrupt:
        sys.exit('^C\n')
    except Exception as e:
        print(f'[{Fore.RED}!{Style.RESET_ALL}] Error: {Fore.RED}{e}{Style.RESET_ALL}')
