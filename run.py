import argparse
import os
import sys
import ipaddress
import textwrap
from tasks.ifconfig import ifconfig
from tasks.ns import ns, nsconv
from tasks.ping import ping
from tasks.traceroute import traceroute
from tasks.banner import bannerWithPort
from tasks.scan import scanStatus, scan, scanWithPort 
from tasks.save import save
 
ap = argparse.ArgumentParser(description='MedSec Tool', formatter_class=argparse.RawDescriptionHelpFormatter,
epilog=textwrap.dedent('''
Examples:
        medsec.py -scan -host 127.0.0.1 -prange 1 20
        medsec.py -grab -host 127.0.0.1 -p 22
        medsec.py -ifconfig www.medpaf.github.io
        medsec.py -traceroute www.medpaf.github.io
        medsec.py -ns www.medpaf.github.io
'''))

ap.add_argument('-ifconfig', action = 'store_true', 
        help = 'display current TCP/IP network configuration')
ap.add_argument('-ping',
        nargs = 1,
        help = 'send ICMP packets to a host to check connectivity.')
ap.add_argument('-traceroute',
        nargs = 1,
        help = 'diagnose route paths and measure transit delays.')
ap.add_argument('-ns', type = str,
        nargs = '+',
        help = 'obtain domain name or IP address mapping.')
ap.add_argument('-host', type = str,
        nargs = '+',
        help = 'specify one or more hosts to scan')
ap.add_argument('-iprange', type = str,
        nargs = 2,
        help = 'specify IP range of hosts to scan')
ap.add_argument('-p', type = int,
        nargs = '+',
        help = 'specify one or more ports to scan')
ap.add_argument('-prange', type = int,
        default = [1-1000], 
        nargs = 2,
        help = 'specify port range to scan')
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
ap.add_argument('-grab', action = 'store_true',
        help = 'perform banner grabbing')
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
                        print('Please type the command correctly. Examples: \n \t -scansyn -host [HOST(s)] \n \t -scansyn -host [HOST(s)] -p [PORT(s)] \n \t -scansyn -host [HOST(s)] -prange [PORT RANGE] \n \t -scansyn -iprange [IP RANGE] -p [PORT(S)] \n \t -scansyn -iprange [IP RANGE] -prange [PORT RANGE]')
        else:
                print('Please specify the host(s) (or IP range) to scan and port(s) (or port range). Examples: \n \t -scansyn -host [HOST(s)] \n \t -scansyn -host [HOST(s)] -p [PORT(s)] \n \t -scansyn -host [HOST(s)] -prange [PORT RANGE] \n \t -scansyn -iprange [IP RANGE] -p [PORT(S)] \n \t -scansyn -iprange [IP RANGE] -prange [PORT RANGE]') 

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

# Check IP address of a website
elif args['ns']:
        for i in range(0, len(args['ns'])):
                ns(args['ns'][i])

# Ping to check connectivity
elif args['ping']:
        ping(args['ping'][0])

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
                        print('Please type the command correctly. Examples: \n \t -grab -host [HOST(s)] -p [PORT(s)] \n \t -grab -iprange [IP RANGE] -prange [PORT RANGE] \n \t -grab -host [HOST(s)] -prange [PORT RANGE] \n \t -grab -iprange [IP RANGE] -p [PORT]')
        
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
                        print('Please type the command correctly. Examples: \n \t -grab -host [HOST(s)] -p [PORT(s)] \n \t -grab -iprange [IP RANGE] -prange [PORT RANGE] \n \t -grab -host [HOST(s)] -prange [PORT RANGE] \n \t -grab -iprange [IP RANGE] -p [PORT]')
        else:
                print('Please specify the host (or IP range) and port(s) (or port range). Examples: \n \t -grab -host [HOST(s)] -p [PORT(s)] \n \t -grab -iprange [IP RANGE] -prange [PORT RANGE] \n \t -grab -host [HOST(s)] -prange [PORT RANGE] \n \t -grab -iprange [IP RANGE] -p [PORT]')
