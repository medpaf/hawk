from multiprocessing import Process
from scapy.all import (ARP, Ether, conf, get_if_hwaddr, send, sniff, sndrcv, srp, wrpcap)

import os
import sys
import time

class Arper:

    def __init__(self, target, gateway, iface):
        self.target = target
        self.gateway = gateway
        self.iface = iface

        conf.iface = iface
        conf.verb = 0

        print(f'Interface: {iface}')  
        print(f'Target MAC: {target}')  
        print(f'Gateway MAC: {gateway}') 

    def run(self):
        pass

    def poison(self):
        pass

    def sniff(self, count=200):
        pass

    def restore(self):
        pass

def arpspoof(target, gateway, iface):
    arp = Arper(target, gateway, iface)
    arp.run()

if __name__ == '__main__':
    arpspoof(target, gateway, iface)