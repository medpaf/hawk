import shodan
import requests
import time
import sys
from colorama import Fore, Back, Style

def vulnscan(host, api_key):
    try:
        print(f'[{Fore.YELLOW}?{Style.RESET_ALL}] Vulnerability scanning on {Fore.YELLOW}{host}{Style.RESET_ALL}...') 
        target = host
        api = shodan.Shodan(api_key)
        dnsResolve = f'https://api.shodan.io/dns/resolve?hostnames={target}&key={api_key}'

        # Resolve target domain to an IP
        resolved = requests.get(dnsResolve)
        hostIP = resolved.json()[target]

        # Do a Shodan search on that IP
        host = api.host(hostIP)
        print(f'[{Fore.GREEN}+{Style.RESET_ALL}] Target: {target}') #\n
        print(f"[{Fore.GREEN}+{Style.RESET_ALL}] IP: {host['ip_str']}")
        print(f"[{Fore.GREEN}+{Style.RESET_ALL}] Organization: {host.get('org', 'n/a')}")
        print(f"[{Fore.GREEN}+{Style.RESET_ALL}] Operating System: {host.get('os', 'n/a')}\n")
        

        # Print all banners
        for item in host['data']:
            print(f"[{Fore.GREEN}+{Style.RESET_ALL}] Port: {Fore.GREEN}{item['port']}{Style.RESET_ALL}")
            print(f"[{Fore.GREEN}+{Style.RESET_ALL}] Banner: {Fore.GREEN}{item['data']}{Style.RESET_ALL}")

        # Print vulnerability information
        if 'vulns' in host and len(host['vulns']) > 0:
            print(f"[{Fore.GREEN}+{Style.RESET_ALL}] {len(host['vulns'])} vulnerability(ies) found on {Fore.YELLOW}{target}{Style.RESET_ALL}")
            for item in host['vulns']:
                CVE = item.replace('!','')
                print(f"\n[{Fore.GREEN}+{Style.RESET_ALL}] Vulnerability: {Fore.GREEN} {item} {Style.RESET_ALL}")
                
                # Wait a second
                time.sleep(1) 
                exploits = api.exploits.search(CVE)
                for item in exploits['matches']:
                    print(item.get('description'))  
            #print('\n')
        else:
            print(f"[{Fore.GREEN}+{Style.RESET_ALL}] No vulnerabilities found on {Fore.YELLOW}{target}{Style.RESET_ALL}.\n{Fore.YELLOW}Disclaimer{Style.RESET_ALL}: This doesn't mean that the host isn't vulnerable.\n")
    except KeyboardInterrupt:
        sys.exit('^C\n')
    except Exception as e:
        print(f'[{Fore.RED}!{Style.RESET_ALL}] Error: {Fore.RED}{e}{Style.RESET_ALL}\n')