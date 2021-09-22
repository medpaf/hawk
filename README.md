# MedSec

![Screenshot from 2021-08-21 10-45-59](https://user-images.githubusercontent.com/61552222/131221155-334eea00-10e1-465c-9017-9cccc2991473.png)

This is a network utility tool that I developed to perform some network and security administrator tasks. Currently, this script can perform a good variety of tasks such as:
- Port scans, including SYN, TCP, UDP, ACK, comprehensive scan;
- Host discovery (scan for up devices on a local network);
- Banner grabbing;
- DNS checks with geolocation information;
- ifconfig;
- ping;
- traceroute;
- DDOS (still in beta).

Other features are still being implemented. Future implementations may include WAP (web application firewall) detection, vulnerability reconnaissance, static code analysis, traffic analysis, offensive tasks such as packet sniffing, ARP poisoning, exploits, some automated tasks and others.

## Installation

To install the necessary packages so that the script can run withouth any problems simply run the `setup.sh` script with root privileges. Currently, this installation script is only supported on debian-based distros that has the apt package manager. On most systems, to install medsec simply run the following commands:
```
git clone https://github.com/medpaf/medsec.git
cd medsec
sudo . setup.sh
```
However, if you are using any other Linux distro with a different package manager, please install the packages manually using your distro's package manager. Depending on the specific distro used, some of the required packages to run this script might be already installed on your machine.
The necessary packages are:
- nmap (using your system's package manager)
- traceroute (using your system's package manager)
- python3-pip (using your system's package manager)
- python-nmap (using pip3)
- colorama (using pip3)
- ipinfo (using pip3)
- scapy (using pip3)
- selenium (using pip3)

After the installation, to run the program, simply navigate to the project's directory and run the `medsec.py` file using python. Running the script as root is recommended for better performance and to avoid permission errors. The used command is the following:
```
sudo python3 medsec.py
```
## How to use
### Scanning hosts
```
-scan -host [HOST(S)]
```
### Host discovery
```
-scanlocal
```
### Banner grabbing
```
-grab -host [HOST(s)] -p [PORT(s)]
```
```
-grab -iprange [START IP] [END IP] -prange [START PORT] [END PORT]
```
```
-grab -host [HOST(s)] -prange [START PORT] [END PORT]
```
```
-grab -iprange [START IP] [END IP] -p [PORT]
```
### DNS checks
```
-ns [HOST(s)]
```
### ifconfig
```
-ifconfig
```
### ping
```
-ping [HOST]
```
### traceroute
```
-traceroute [HOST]
```