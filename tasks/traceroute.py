import socket
import sys
from colorama import Fore, Back, Style

def tracert(host, maxhops=30, timeout=0.2):
    proto_icmp = socket.getprotobyname('icmp')
    proto_udp = socket.getprotobyname('udp')
    host_addr = socket.gethostbyname(host)
    port = 33434

    for ttl in range(1, maxhops):
        rx = socket.socket(socket.AF_INET, socket.SOCK_RAW, proto_icmp)
        rx .settimeout(timeout)
        rx.bind(('', port))

        tx = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, proto_udp)
        tx.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)
        tx.sendto(''.encode(), (host_addr, port))

        try:
            data, curr_addr = rx.recvfrom(512)
            curr_addr = curr_addr[0]
        except socket.error:
            curr_addr = None
        finally:
            rx.close()
            tx.close()

        yield curr_addr

        if curr_addr == host:
            break

def traceroute(host):
    try:
        host_addr = socket.gethostbyname(host)
        print(f'[{Fore.YELLOW}?{Style.RESET_ALL}] Starting traceroute to {Fore.YELLOW}{host}{Style.RESET_ALL} ({Fore.YELLOW}{host_addr}{Style.RESET_ALL})...')

        for i, v in enumerate(tracert(host_addr)):
            if v == None:
                print(f'[{Fore.GREEN}{i+1}{Style.RESET_ALL}]\t{v}')
            else:
                try:
                    host = socket.gethostbyaddr(v)
                    print(f'[{Fore.GREEN}{i+1}{Style.RESET_ALL}]\t{Fore.GREEN}{v}{Style.RESET_ALL} ({Fore.GREEN}{host[0]}{Style.RESET_ALL})')
                except Exception:
                    print(f'[{Fore.GREEN}{i+1}{Style.RESET_ALL}]\t{Fore.GREEN}{v}{Style.RESET_ALL}')
    except Exception as e:
        print(f'[{Fore.RED}!{Style.RESET_ALL}] Error: {Fore.RED}{e}{Style.RESET_ALL}')
    except KeyboardInterrupt:
        sys.exit('^C\n')

