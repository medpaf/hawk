import requests
import sys
from threading import Thread, Lock
from queue import Queue

q = Queue()
list_lock = Lock()
discovered_domains = []

def scanSubdomains(domain):
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
            sys.exit()
        else:
            print(f'Discovered subdomain: {url}')
            # Add the subdomain to the global list
            with list_lock:
                discovered_domains.append(url)

        # Scanning of that subdomain complete
        q.task_done()


def main(domain, threads, subdomains):
    global q

    # Fill the queue with all the subdomains
    try:
        for subdomain in subdomains:
            q.put(subdomain)

        for thread in range(threads):
            # Start all threads
            worker = Thread(target=scanSubdomains, args=(domain,))
            # Daemon thread (a thread that will end when the main thread ends)
            worker.daemon = True
            worker.start()
    except KeyboardInterrupt:
        sys.exit('^C')


def sdenum(domain):
    wordlist = "tasks/files/subdomains.txt"
    threads = 6
    #output_file = args.output_file

    try:
        main(domain=domain, threads=threads, subdomains=open(wordlist).read().splitlines())
        q.join()

        if len(discovered_domains) > 0:
            print(f'\nScan completed. A total of {len(discovered_domains)} subdomains were discovered.')
        else:
            print(f'Scan completed. No subdomains were discovered.')
    except KeyboardInterrupt:
        sys.exit()

    # save the file
    # with open(output_file, "w") as f:
    #    for url in discovered_domains:
    #        print(url, file=f)