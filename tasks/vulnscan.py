import shodan
import requests
from extras import printcolor
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
        print(f'\nTarget: {target}')
        print(f"IP: {host['ip_str']}")
        print(f"Organization: {host.get('org', 'n/a')}")
        print(f"Operating System: {host.get('os', 'n/a')}")
        

        # Print all banners
        for item in host['data']:
            print(f"Port: {item['port']}")
            print(f"Banner: {item['data']}")

        # Print vulnerability information
        if 'vulns' in host and len(host['vulns']) > 0:
            printcolor('RED', f"{len(host['vulns'])} vulnerability(ies) found on {target}")
            for item in host['vulns']:
                CVE = item.replace('!','')
                print(f"\nVulnerability: {Fore.RED} {item} {Style.RESET_ALL}")
                # Wait a second
                time.sleep(1) 
                exploits = api.exploits.search(CVE)
                for item in exploits['matches']:
                    print(item.get('description'))  
        else:
            printcolor('GREEN', f"No vulnerabilities found on {target}.")
            print("Disclaimer: This doesn't mean that the host isn't vulnerable.")
    except KeyboardInterrupt:
        sys.exit()
    except Exception as e:
        printcolor('RED', f'Error: {e}')