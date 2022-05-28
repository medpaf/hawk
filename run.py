import argparse
import os
import sys
import ipaddress
import textwrap
from colorama import Fore, Back, Style

from files.conf import *

from tasks.ifconfig import ifconfig
from tasks.ns import ns, nsconv
from tasks.whoisinfo import whoisinfo
from tasks.sdenum import sdenum
from tasks.dirbust import dirbust
from tasks.ping import ping
from tasks.traceroute import traceroute
from tasks.banner import bannerWithPort
from tasks.scan import scanStatus, scan, scanWithPort, scanLocalDevices
from tasks.vulnscan import vulnscan
from tasks.offense.sniff import sniff
from tasks.offense.ipspoof import ipspoof
from tasks.offense.macspoof import macspoof
from tasks.offense.synflood import synflood
from tasks.getmac import getmac
from tasks.offense.deauth import deauth
from tasks.offense.bruteforce import bruteforce
from tasks.ifacemode import turn_monitor, turn_managed
from tasks.save import save
from autoscan import *
 
ap = argparse.ArgumentParser(description='Hawk', formatter_class=argparse.RawDescriptionHelpFormatter,
epilog=textwrap.dedent('''

Examples:
        -ifconfig
        -ping <HOST(s) IP/URL>
        -traceroute <HOST IP/URL>
        -scan -host <HOST(s) IP/URL> -prange <START PORT> <END PORT>
        -scanlan
        -getmac -host <HOST(s) IP>
        -grab -host <HOST(S) IP/URL> -p <PORT(s)>
        -ns <HOST(s) IP/URL>
        -whois <HOST(s) IP/URL>

        -sdenum <DOMAIN>
        -sdenum <DOMAIN> -wordlist <WORDLIST PATH>
        
        -dirbust <HOST IP/URL> -wordlist <WORDLIST PATH> 
        -vulnscan -host <HOST(s) IP/URL>
        -sniff
        -macspoof -source <SOURCE MAC> -iface <INTERFACE>
        -ipspoof -source <SOURCE IP> <SOURCE PORT> -target <TARGET IP/URL> <TARGET PORT>
        -synflood -source <SOURCE PORT> -target <TARGET IP/URL> <TARGET PORT>
        -deauth -target <TARGET MAC> -gateway <GATEWAY MAC> -iface <INTERFACE> 

        -bruteforce <SERVICE> -target <TARGET IP/URL> -user <USERNAME>
        -bruteforce <SERVICE> -target <TARGET IP/URL> -user <USERNAME> -wordlist <WORDLIST PATH>

        -autoscan <HOST(s) IP/URL>
        -mode <MODE> -iface <INTERFACE>

'''))

ap.add_argument('-ifconfig', action = 'store_true', 
        help = 'display current TCP/IP network configuration')
ap.add_argument('-ping', type = str,
        nargs = '+',
        help = 'send ICMP packets to a host to check connectivity.')
ap.add_argument('-traceroute',
        nargs = 1,
        help = 'diagnose route paths and measure transit delays.')
ap.add_argument('-ns', type = str,
        nargs = '+',
        help = 'obtain domain name or IP address mapping.')
ap.add_argument('-whois', type = str,
        nargs = '+',
        help = 'obtain WHOIS protocol information.')
ap.add_argument('-sdenum', type = str, 
        nargs = 1,
        help = 'perform subdomain enumeration.') 
ap.add_argument('-dirbust', type = str, 
        nargs = 1,
        help = 'perform directory busting on a host.') 
ap.add_argument('-scantcp', action = 'store_true',
        help = 'perform TCP scan for open ports')
ap.add_argument('-scanack', action = 'store_true',
        help = 'perform ACK scan for open ports')
ap.add_argument('-scansyn', action = 'store_true',
        help = 'perform SYN scan for open ports (root privileges needed)')
ap.add_argument('-scanudp', action = 'store_true',
        help = 'perform UDP scan for open ports (root privileges needed)')
ap.add_argument('-scan', action = 'store_true',
        help = 'perform comprehensive scan for open ports (root privileges needed)')
ap.add_argument('-scanlan', action = 'store_true',
        help = 'perform scan to detect local devices')
ap.add_argument('-vulnscan', action = 'store_true',
        help = 'perform vulnerabilty scan on a host')
ap.add_argument('-grab', action = 'store_true',
        help = 'perform banner grabbing')
ap.add_argument('-getmac', action = 'store_true',
        help = 'Get MAC address of a host IP address in the same LAN (root privileges needed)')
ap.add_argument('-macspoof', action = 'store_true',
        help = 'perform MAC spoofing on a target (root privileges needed)')
ap.add_argument('-ipspoof', action = 'store_true',
        help = 'perform IP spoofing on a target (root privileges needed)')
ap.add_argument('-synflood', action = 'store_true',
        help = 'perform SYN flooding on a target (root privileges needed)')
ap.add_argument('-sniff', action = 'store_true',
        help = 'perform packet sniffing (root privileges needed)')
ap.add_argument('-deauth', action = 'store_true',
        help = 'perform deauthentication attack (root privileges needed)')
ap.add_argument('-bruteforce',
        nargs=1,
        help = 'Attempt brute-force attack on a service to guess password')
ap.add_argument('-autoscan',
        nargs = '+',
        help = 'Automated reconnaissance.')
ap.add_argument('-mode', '-m', type = str,
        nargs = 1,
        help = 'turn on specified mode (root privileges needed)')
ap.add_argument('-s', type = str,
        nargs = 1,
        help = 'save output as file to the specified path.')

ap.add_argument('-host', type = str,
        nargs = '+',
        help = 'specify one or more hosts')
ap.add_argument('-iprange', type = str,
        nargs = 2,
        help = 'specify IP range of hosts')
ap.add_argument('-p', type = int,
        nargs = '+',
        help = 'specify one or more ports')
ap.add_argument('-prange', type = int,
        default = [1-1000], 
        nargs = 2,
        help = 'specify port range')
ap.add_argument('-source', '-src', type = str,
        nargs = '+',
        help = 'specify one source')
ap.add_argument('-target', '-trg', type = str,
        nargs = '+',
        help = 'specify one or more targets')
ap.add_argument('-gateway', '-gtw', type = str,
        nargs = '+',
        help = 'specify the gateway MAC address')
ap.add_argument('-iface', '-i', type = str,
        nargs = 1,
        help = 'specify interface')
ap.add_argument('-user', '-usr', type = str,
        nargs = 1,
        help = 'specify username')
ap.add_argument('-wordlist', '-wl', type = str,
        nargs = 1,
        help = 'specify wordlist file')


args = vars(ap.parse_args())

# Function to handle scans
def handleScan(scantype):
        if args['host']:
                # Perform scan with IP address(es) only
                if not args['p'] and not len(args['prange']) == 2: 
                        for i in range(0, len(args['host'])):
                                scan(nsconv(args['host'][i]), args['host'][i], 1, 1000, f'{scantype}')

                # Perform scan with IP address(es) and port(s)        
                elif args['p'] and not len(args['prange']) == 2:
                        for i in range(0, len(args['host'])):
                                for j in range(0, len(args['p'])):
                                        scanWithPort(nsconv(args['host'][i]), args['host'][i], args['p'][j], i, j, f'{scantype}')
                
                # Perform scan with IP address(es) and port range
                elif len(args['prange']) == 2 and not args['p']:
                        for i in range(0, len(args['host'])):
                                scan(nsconv(args['host'][i]), args['host'][i], args['prange'][0], args['prange'][1], f'{scantype}')
                else:
                        print(f'[{Fore.RED}!{Style.RESET_ALL}] Please type the command correctly. Examples: \n \t -scan -host <HOST(s) IP/URL> \n \t -scan -host <HOST(s) IP/URL> -p <PORT(s)> \n \t -scan -host <HOST(s) IP/URL> -prange <START PORT> <END PORT> \n \t -scan -iprange <START IP> <END IP> -p <PORT(S)> \n \t -scan -iprange <START IP> <END IP> -prange <START PORT> <END PORT>')
        else:
                print(f'[{Fore.RED}!{Style.RESET_ALL}] Please type the command correctly. Examples: \n \t -scan -host <HOST(s) IP/UR> \n \t -scan -host <HOST(s) IP/URL> -p <PORT(s)> \n \t -scan -host <HOST(s) IP/URL> -prange <START PORT> <END PORT> \n \t -scan -iprange <START IP> <END IP> -p <PORT(S)> \n \t -scan -iprange <START IP> <END IP> -prange <START PORT> <END PORT>') 

# Save output file
if args['s']:
        argsList = sys.argv[1:]
        filenameIndex = argsList.index('-s') + 1
        argsList.pop(filenameIndex)
        argsList.remove('-s')
        comm = ' '.join(argsList)
        save(f'{comm}', args['s'][0]) 

# Check host IP configuration
elif args['ifconfig']:
        ifconfig()

# DNS check (check IP address of a website)
elif args['ns']:
        
        try:
                for i in range(0, len(args['ns'])):
                        ns(args['ns'][i], IPINFO_API_KEY)
        except Exception as e:
                print(f'[{Fore.RED}!{Style.RESET_ALL}] Please type the command correctly. Examples: \n \t -ns <HOST(s) IP/URL>')

# WHOIS
elif args['whois']:

        try:
                for i in range(0, len(args['whois'])):
                        whoisinfo(args['whois'][i])
        except Exception as e:
                print(f'[{Fore.RED}!{Style.RESET_ALL}] Please type the command correctly. Examples: \n \t -whois <HOST(s) IP/URL>')

# Subdomain enumeration
elif args['sdenum']:

        try:
                if args['wordlist']:
                        sdenum(args['sdenum'][0], args['wordlist'])
                else:
                        sdenum(args['sdenum'][0], SUBDOMAINS_WORDLIST)
        except Exception as e:
                print(f'[{Fore.RED}!{Style.RESET_ALL}] Please type the command correctly. Examples: \n \t -sdenum <DOMAIN> \n \t -sdenum <DOMAIN> -wordlist <WORDLIST PATH>')

# Directory busting
elif args['dirbust']:

        try:
                if args['wordlist']:
                        dirbust(args['dirbust'][0], args['wordlist'])
                else:
                        dirbust(args['dirbust'][0], DIRECTORIES_WORDLIST)
        except Exception as e:
                 print(f'[{Fore.RED}!{Style.RESET_ALL}] Please type the command correctly. Examples: \n \t -dirbust <HOST IP/URL> \n \t -dirbust <HOST IP/URL> -wordlist <WORDLIST PATH>\n {e}')

# Ping to check connectivity
elif args['ping']:

        try:
                for i in range(0, len(args['ping'])):
                        ping(args['ping'][i], i)
        except Exception as e:
                print(f'[{Fore.RED}!{Style.RESET_ALL}] Please type the command correctly. Examples: \n \t -ping <HOST(s) IP/URL>')

# Traceroue
elif args['traceroute']:

        try:
                traceroute(args['traceroute'][0])
        except Exception as e:
                print(f'[{Fore.RED}!{Style.RESET_ALL}] Please type the command correctly. Examples: \n \t -traceroute <HOST IP/URL>')

# TCP scan
elif args['scantcp']:
        handleScan('-sT')  

# ACK scan
elif args['scanack']:
        handleScan('-sA')

# UDP scan
elif args['scanudp']:
        handleScan('-sU')

# SYN scan
elif args['scansyn']:
        handleScan('-sS')
                                
# Comprehensive scan
elif args['scan']:
        handleScan('-sS -sV -sC -A -O')

# Scan for local devices
elif args['scanlan']:
        scanLocalDevices()

# Get MAC address of a host IP address
elif args['getmac']:

        try:
                for i in range(0, len(args['host'])):
                        getmac(args['host'][i], i)                
        except Exception as e:
              print(f'[{Fore.RED}!{Style.RESET_ALL}] Please type the command correctly. Examples: \n \t -getmac -host <HOST(s) IP>')  

# Vuln scan on a host
elif args['vulnscan']:

        try:
                if args['host']:
                        for i in range(0, len(args['host'])):
                                vulnscan(args['host'][i], SHODAN_API_KEY)
                                if len(args['host']) > 1:
                                        print('\n')
                elif args['iprange']:
                        for ip_int in range(int(ipaddress.IPv4Address(args['iprange'][0])), int(ipaddress.IPv4Address(args['iprange'][1]) + 1)):
                                vulnscan(ipaddress.IPv4Address(ip_int), SHODAN_API_KEY)
        except Exception as e:
                print(f'[{Fore.RED}!{Style.RESET_ALL}] Please type the command correctly. Examples: \n \t -vulnscan -host <HOST(s) IP/URL>')

# Banner grabbing
elif args['grab']: 

        try:   
                if args['host']: 

                        # Perform grabbing with IP address(es) and port number(s)
                        if args['p'] and not len(args['prange']) == 2: 
                                for i in range(0, len(args['host'])):
                                        for j in range(0, len(args['p'])):
                                                bannerWithPort(nsconv(args['host'][i]), args['p'][j])               

                        # Perform grabbing with IP address(es) and port range 
                        elif len(args['prange']) == 2 and not args['p']: 
                                for i in range(0, len(args['host'])):
                                        for j in range(args['prange'][0], args['prange'][1] + 1):
                                                bannerWithPort(nsconv(args['host'][i]), j)
                elif args['iprange']:

                        # Perform grabbing with IP range and port number(s)
                        if args['p'] and not len(args['prange']) == 2: 
                                for ip_int in range(int(ipaddress.IPv4Address(args['iprange'][0])), int(ipaddress.IPv4Address(args['iprange'][1]) + 1)):
                                        for j in range(0, len(args['p'])):
                                                bannerWithPort(ipaddress.IPv4Address(ip_int), args['p'][j])

                        # Perform grabbing with IP range and port rangeIP
                        elif len(args['prange']) == 2 and not args['p']: 
                                for ip_int in range(int(ipaddress.IPv4Address(args['iprange'][0])), int(ipaddress.IPv4Address(args['iprange'][1]) + 1)):
                                        for j in range(args['prange'][0], args['prange'][1] + 1):
                                                bannerWithPort(ipaddress.IPv4Address(ip_int), j) 
        except Exception as e:

                print(f'[{Fore.RED}!{Style.RESET_ALL}] Please type the command correctly. Examples: \n \t -grab -host <HOST(s) IP/URL> -p <PORT(s)> \n \t -grab -iprange <START IP> <END IP> -prange <START PORT> <END PORT> \n \t -grab -host <HOST(s) IP/URL> -prange <START PORT> <END PORT> \n \t -grab -iprange <START IP> <END IP> -p <PORT>')

# IP spoofing
elif args['ipspoof']:
                        
        try:
                ipspoof(args['source'][0], args['source'][1], nsconv(args['target'][0]), int(args['target'][1])) 
        except Exception as e:
                print(f'[{Fore.RED}!{Style.RESET_ALL}] Please type the command correctly. You can only attack one host and one port at a time. Examples: \n \t -ipspoof -source <SOURCE IP> <SOURCE PORT> -target <TARGET IP/URL> <TARGET PORT>')
        
# MAC spoofing
elif args['macspoof']: #changed

        try:

                if args['iface'][0].lower() == 'd':
                        macspoof(args['source'][0], args['iface'][0], DEFAULT_WIRELESS_INTERFACE)
                else:
                        macspoof(args['source'][0], args['iface'][0])

        except Exception as e:
                print(f'[{Fore.RED}!{Style.RESET_ALL}] Please type the command correctly. Examples: \n \t -macspoof -source <SOURCE MAC> -iface <INTERFACE>')

# SYN flooding
elif args['synflood']:

        try:
                synflood(args['source'][0], args['target'][0], args['target'][1])
        except Exception as e:
                print(f'[{Fore.RED}!{Style.RESET_ALL}] Please type the command correctly. Examples: \n \t -synflood -source <SOURCE PORT> -target <TARGET IP/URL> <TARGET PORT>')

# Packet sniffing
elif args['sniff']:
        sniff()

# Deauth attack ##changed
elif args['deauth']:

        try:
                if args['iface'][0].lower() == 'd':
                        deauth(args['target'][0], args['gateway'][0], args['iface'][0], DEFAULT_WIRELESS_INTERFACE)
                else:
                        deauth(args['target'][0], args['gateway'][0], args['iface'][0])

        except Exception as e:
                print(f'[{Fore.RED}!{Style.RESET_ALL}] Please type the command correctly. Examples: \n \t -deauth -target <TARGET(s) MAC(s)> -gateway <GATEWAY MAC> -iface <INTERFACE>')

# Brute-force attack
elif args['bruteforce']: ###### testing phase
        
        try:
                if args['wordlist']:
                        bruteforce(args['bruteforce'][0], args['target'][0], args['user'][0], args['wordlist'][0])
                else:
                        bruteforce(args['bruteforce'][0], args['target'][0], args['user'][0], PASSWORDS_WORDLIST)
        except Exception as e:
                print(f'[{Fore.RED}!{Style.RESET_ALL}] Please type the command correctly. Examples: \n \t -bruteforce <SERVICE> -target <TARGET IP/URL> -user <USERNAME> \n \t -bruteforce <SERVICE> -target <TARGET IP/URL> -user <USERNAME> -wordlist <WORDLIST PATH>')

# Automated reconnaissance
elif args['autoscan']:

        try:
                for i in range(0, len(args['autoscan'])):
                        autoscan(args['autoscan'][i])
        except Exception as e:
                print(f'[{Fore.RED}!{Style.RESET_ALL}] Please type the command correctly. Examples: \n \t -autoscan <HOST(s) IP/URL>')
# Turn on monitor/managed mode
elif args['mode']:

        try:
                if args['mode'][0].lower() == 'monitor':

                        if args['iface'][0].lower() == 'd':
                                turn_monitor(args['iface'][0], DEFAULT_WIRELESS_INTERFACE)
                        else:
                                turn_monitor(args['iface'][0])

                elif args['mode'][0].lower() == 'managed':

                        if args['iface'][0].lower() == 'd':
                                turn_managed(args['iface'][0], DEFAULT_WIRELESS_INTERFACE)
                        else:
                                turn_managed(args['iface'][0])
                else:
                        print(f"[{Fore.RED}!{Style.RESET_ALL}] {Fore.RED}Mode can only be 'monitor' or 'managed'.{Style.RESET_ALL}")
        
        except Exception as e:
                print(f'[{Fore.RED}!{Style.RESET_ALL}] {e} \nPlease type the command correctly. Examples: \n \t -mode <MODE> -iface <INTERFACE>')
        
else:
        # if arguments are present
        if len(sys.argv) > 1:
                print(f"[{Fore.RED}!{Style.RESET_ALL}] Please, type the command correctly. For additional help, type '-h'.") 
