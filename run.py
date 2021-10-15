import argparse
import os
import subprocess
import sys
import ipaddress
import textwrap

from tasks.ifconfig import ifconfig
from tasks.ns import ns, nsconv
from tasks.sdenum import sdenum, scanSubdomains, main
from tasks.ping import ping
from tasks.traceroute import traceroute
from tasks.banner import bannerWithPort
from tasks.scan import scanStatus, scan, scanWithPort, scanLocalDevices
from tasks.vulnscan import vulnscan
from tasks.offense.sniff import sniff
from tasks.offense.ipspoof import ipspoof
from tasks.getmac import getmac
from tasks.offense.deauth import deauth
from tasks.save import save
 
ap = argparse.ArgumentParser(description='MedSec Tool', formatter_class=argparse.RawDescriptionHelpFormatter,
epilog=textwrap.dedent('''
Examples:
        -scan -host [HOST(s)] -prange [START PORT] [END PORT]
        -scanlan
        -getmac -host [HOST(s) IP]
        -grab -host [HOST(S)] -p [PORT(s)]
        -ns [HOST]
        -sdenum [DOMAIN]
        -vulnscan -host [HOST(s)]
        -ifconfig [HOST]
        -ping [HOST(s)]
        -traceroute [HOST]
        -ipspoof -source [SOURCE IP] [SOURCE PORT] -target [TARGET IP] [TARGET PORT]
        -sniff
        -deauth -target [TARGET MAC] -gateway [GATEWAY MAC] -iface [INTERFACE] 

   
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
ap.add_argument('-sdenum', type = str, 
        nargs = 1,
        help = 'perform subdomain enumeration.') 
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
        nargs = '+',
        help = 'specify interface')
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
ap.add_argument('-ipspoof', action = 'store_true',
        help = 'perform IP spoofing on a target (root privileges needed)')
ap.add_argument('-sniff', action = 'store_true',
        help = 'perform packet sniffing (root privileges needed)')
ap.add_argument('-deauth', action = 'store_true',
        help = 'perform deauthentication attack (root privileges needed)')
ap.add_argument('-s', type = str,
        nargs = 1,
        help = 'save output as file to the specified path.')

args = vars(ap.parse_args())

# Function to handle scans
def handleScan(scantype):
        if args['host']:
                # Perform SYN scan with IP address(es) only
                if not args['p'] and not len(args['prange']) == 2: 
                        for i in range(0, len(args['host'])):
                                scan(nsconv(args['host'][i]), args['host'][i], 1, 1000, f'{scantype}')

                # Perform SYN scan with IP address(es) and port(s)        
                elif args['p'] and not len(args['prange']) == 2:
                        for i in range(0, len(args['host'])):
                                for j in range(0, len(args['p'])):
                                        scanWithPort(nsconv(args['host'][i]), args['host'][i], args['p'][j], i, j, f'{scantype}')
                
                # Perform SYN scan with IP address(es) and port range
                elif len(args['prange']) == 2 and not args['p']:
                        for i in range(0, len(args['host'])):
                                scan(nsconv(args['host'][i]), args['host'][i], args['prange'][0], args['prange'][1], f'{scantype}')
                else:
                        print('Please type the command correctly. Examples: \n \t -scan -host [HOST(s)] \n \t -scan -host [HOST(s)] -p [PORT(s)] \n \t -scan -host [HOST(s)] -prange [START PORT] [END PORT] \n \t -scan -iprange [START IP] [END IP] -p [PORT(S)] \n \t -scan -iprange [START IP] [END IP] -prange [START PORT] [END PORT]')
        else:
                print('Please specify the host(s) (or IP range) to scan and port(s) (or port range). Examples: \n \t -scan -host [HOST(s)] \n \t -scan -host [HOST(s)] -p [PORT(s)] \n \t -scan -host [HOST(s)] -prange [START PORT] [END PORT] \n \t -scan -iprange [START IP] [END IP] -p [PORT(S)] \n \t -scan -iprange [START IP] [END IP] -prange [START PORT] [END PORT]') 

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
        for i in range(0, len(args['ns'])):
                ns(args['ns'][i])

# Subdomain enumeration
elif args['sdenum']:
        sdenum(args['sdenum'][0])

# Ping to check connectivity
elif args['ping']:
        for i in range(0, len(args['ping'])):
                ping(args['ping'][i], i)

# Traceroue
elif args['traceroute']:
        traceroute(args['traceroute'][0])

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
        if args['host']:
                for i in range(0, len(args['host'])):
                        getmac(args['host'][i], i)                
        else:
              print('Please type the command correctly. Examples: \n \t -getmac -host [HOST(s) IP]')  

# Vuln scan on a host
elif args['vulnscan']:
        if args['host']:
                for i in range(0, len(args['host'])):
                        vulnscan(args['host'][i])
        elif args['iprange']:
                for ip_int in range(int(ipaddress.IPv4Address(args['iprange'][0])), int(ipaddress.IPv4Address(args['iprange'][1]) + 1)):
                        vulnscan(ipaddress.IPv4Address(ip_int))
        else:
                print('Please type the command correctly. Examples: \n \t -vulnscan -host [HOST(s)]')

# Banner grabbing
elif args['grab']:    

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
                else:
                        print('Please type the command correctly. Examples: \n \t -grab -host [HOST(s)] -p [PORT(s)] \n \t -grab -iprange [START IP] [END IP] -prange [START PORT] [END PORT] \n \t -grab -host [HOST(s)] -prange [START PORT] [END PORT] \n \t -grab -iprange [START IP] [END IP] -p [PORT]')
        
        elif args['iprange']:

                # Perform grabbing with IP range and port number(s)
                if args['p'] and not len(args['prange']) == 2: 
                        for ip_int in range(int(ipaddress.IPv4Address(args['iprange'][0])), int(ipaddress.IPv4Address(args['iprange'][1]) + 1)):
                                for j in range(0, len(args['p'])):
                                        bannerWithPort(ipaddress.IPv4Address(ip_int), args['p'][j])

                # Perform grabbing with IP range and port range
                elif len(args['prange']) == 2 and not args['p']: 
                        for ip_int in range(int(ipaddress.IPv4Address(args['iprange'][0])), int(ipaddress.IPv4Address(args['iprange'][1]) + 1)):
                                for j in range(args['prange'][0], args['prange'][1] + 1):
                                        bannerWithPort(ipaddress.IPv4Address(ip_int), j) 
                else:
                        print('Please type the command correctly. Examples: \n \t -grab -host [HOST(s)] -p [PORT(s)] \n \t -grab -iprange [START IP] [END IP] -prange [START PORT] [END PORT] \n \t -grab -host [HOST(s)] -prange [START PORT] [END PORT] \n \t -grab -iprange [START IP] [END IP] -p [PORT]')
        else:
                print('Please type the command correctly. Examples: \n \t -grab -host [HOST(s)] -p [PORT(s)] \n \t -grab -iprange [START IP] [END IP] -prange [START PORT] [END PORT] \n \t -grab -host [HOST(s)] -prange [START PORT] [END PORT] \n \t -grab -iprange [START IP] [END IP] -p [PORT]')
# IP Spoofing
elif args['ipspoof']:

        if args['source']:

                if args['target']:
                        if len(args['source']) == 2 and len(args['target']) == 2:
                                ipspoof(args['source'][0], args['source'][1], nsconv(args['target'][0]), int(args['target'][1])) 
                        else:
                                print('Please type the command correctly. You can only attack one host and one port at a time. Examples: \n \t -ipspoof -spoof -source [SOURCE IP] [SOURCE PORT] -target [TARGET IP] [TARGET PORT]')
                else:
                        print('Please type the command correctly. You can only attack one host and one port at a time. Examples: \n \t -ipspoof -source [SOURCE IP] [SOURCE PORT] -target [TARGET IP] [TARGET PORT]')
        else:
                print('Please type the command correctly. You can only attack one host and one port at a time. Examples: \n \t -ipspoof -source [SOURCE IP] [SOURCE PORT] -target [TARGET IP] [TARGET PORT]')

# Packet sniffing
elif args['sniff']:
        sniff()

# Deauth attack
elif args['deauth']:

        if args['target'] and args['gateway'] and args['iface']:

                if len(args['target']) == 1:
                        deauth(args['target'][0], args['gateway'][0], args['iface'][0]) 
                
                else:
                        print('Please type the command correctly. Examples: \n \t -deauth -target [TARGET(s) MAC(s)] -gateway [GATEWAY MAC] -iface [INTERFACE]')
                
        else:
                print('Please type the command correctly. Examples: \n \t -deauth -target [TARGET(s) MAC(s)] -gateway [GATEWAY MAC] -iface [INTERFACE]')
        


else:
        # if arguments are present
        if len(sys.argv) > 1:
                print("Please, type the command correctly. For additional help, type '-h'.") 
