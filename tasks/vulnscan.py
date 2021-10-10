import shodan
import requests
import time
import sys
from colorama import Fore, Back, Style

SHODAN_API_KEY = 'Q4wtGdNmqnaQ267zzUb2rQztDRayEISI'
api = shodan.Shodan(SHODAN_API_KEY)

def vulnscan(target):
    target = target
    dnsResolve = f'https://api.shodan.io/dns/resolve?hostnames={target}&key={SHODAN_API_KEY}'

    try:
        # Resolve target domain to an IP
        resolved = requests.get(dnsResolve)
        hostIP = resolved.json()[target]

        # Do a Shodan search on that IP
        host = api.host(hostIP)
        print(f'\n[{Fore.GREEN}+{Style.RESET_ALL}] Target: {target}')
        print(f"[{Fore.GREEN}+{Style.RESET_ALL}] IP: {host['ip_str']}")
        print(f"[{Fore.GREEN}+{Style.RESET_ALL}] Organization: {host.get('org', 'n/a')}")
        print(f"[{Fore.GREEN}+{Style.RESET_ALL}] Operating System: {host.get('os', 'n/a')}\n")
        

        # Print all banners
        for item in host['data']:
            print(f"[{Fore.GREEN}+{Style.RESET_ALL}] Port: {item['port']}")
            print(f"[{Fore.GREEN}+{Style.RESET_ALL}] Banner: {item['data']}")

        # Print vulnerability information
        if 'vulns' in host and len(host['vulns']) > 0:
            print(f"[{Fore.GREEN}+{Style.RESET_ALL}] {len(host['vulns'])} vulnerability(ies) found on {target}")
            for item in host['vulns']:
                CVE = item.replace('!','')
                print(f"\nVulnerability: {Fore.RED} {item} {Style.RESET_ALL}")
                # Wait a second
                time.sleep(1) 
                exploits = api.exploits.search(CVE)
                for item in exploits['matches']:
                    print(item.get('description'))  
        else:
            print(f"No vulnerabilities found on {target}.\n{Fore.YELLOW}Disclaimer{Style.RESET_ALL}: This doesn't mean that the host isn't vulnerable.")
    except KeyboardInterrupt:
        sys.exit()
    except Exception as e:
        print(f'[{Fore.RED}!{Style.RESET_ALL}] Error: {Fore.RED}{e}{Style.RESET_ALL}')