
# MedSec

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
![Stars](https://img.shields.io/github/stars/medpaf/medsec.svg)
![Forks](https://img.shields.io/github/forks/medpaf/medsec.svg)
![Size](https://img.shields.io/github/repo-size/medpaf/medsec)
![Mantained](https://img.shields.io/badge/Maintained%3F-yes-green.svg)
[![Linux](https://svgshare.com/i/Zhy.svg)](https://svgshare.com/i/Zhy.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

![135713734-93ac0416-0a67-4a7e-aeb2-7ee70dc7d103~3](https://user-images.githubusercontent.com/61552222/136041183-34e52f67-f93f-4cea-9df6-38d3b5cc5163.png)

MedSec is a network and pentest utility that I developed so that I could perform different kinds of task using the same suite, instead of jumping from one tool to another.

Currently, this script can perform a good variety of tasks such as **ifconfig**, **ping**, **traceroute**, **port scans** (including SYN, TCP, UDP, ACK, comprehensive scan, **host discovery** (scan for up devices on a local network), **MAC address detection** (get MAC address of a host IP on a local network), **banner grabbing**, **DNS checks** (with geolocation information), **WHOIS**, **subdomain enumeration**, **vulnerability reconnaissance**, **packet sniffing**, **MAC spoofing**, **IP spoofing**, **SYN flooding**, **deauth attack** and **brute-force attack** (beta).

Other features are still being implemented. Future implementations may include WAF detection, DNS enumeration, traffic analysis, XSS vulnerability scanner, ARP cache poisoning, DNS cache poisoning, MAC flooding, ping of death, network disassociation attack (not deauth attack), OSINT, exploits, some automated tasks and others.

## Contents

+ [Installation](#installation)
  - [Linux](#linux)
+ [Configuration](#configuration)
+ [How to use](#how-to-use)
  + Networking
    - [ifconfig (beta)](#ifconfig)
    - [ping](#ping)
    - [traceroute](#traceroute)
  + Footprinting
    - [Port scans](#port-scans)
    - [Host discovery (scan for devices on a local network)](#host-discovery)
    - [MAC address detection (get MAC address of a host IP on a local network)](#mac-address-detection)
    - [Banner grabbing](#banner-grabbing)
    - [DNS checks (with geolocation information)](#dns-checks)
    - [WHOIS](#whois)
    - [Subdomain enumeration](#subdomain-enumeration)
    - [Vulnerability reconnaissance](#vulnerability-reconnaissance)
  + Offensive
    - [Packet sniffing](#packet-sniffing)
    - [MAC spoofing](#mac-spoofing)
    - [IP spoofing](#ip-spoofing)
    - [SYN flooding](#syn-flooding)
    - [Deauth attack](#deauth-attack)
    - [Brute-force attack (beta)](#brute-force-attack)
+ [Contribution](#contribution)
+ [License](#license)

## Installation

Note that currently, this script can only run well on Linux. If you try it in on Windows or macOS, it may run, but numerous errors will appear. It will have Windows support anytime in the future.

This script was tested on:
- Kali Linux
- Ubuntu
### Linux

To install the necessary packages so that the script can run withouth any problems simply run the `setup.sh` script with root privileges. Currently, this installation script is only supported on Debian, Red Hat and Arch based distros that has the apt, dnf and pacman package manager respectively (***Ubuntu***, ***Kali Linux***, ***Parrot OS***, ***Debian***, ***Pop!_OS***, ***Linux Mint***, ***Deepin***, ***Zorin OS***, ***MX Linux***, ***Elementary OS***, ***Fedora***, ***CentOS***, ***Red Hat Enterprise Linux***, ***Rocky Linux***, ***AlmaLinux***, ***Oracle Linux***, ***ClearOS***, ***Arch***, ***Black Arch***, ***Manjaro*** etc). On most systems, to install MedSec simply run the following commands:
```
git clone https://github.com/medpaf/medsec.git
cd medsec
sudo sh setup.sh
```
Then, simply follow the instructions.

However, if you are using any other Linux distro with a different package manager, please install the packages manually using your distro's package manager. Depending on the specific distro used, some of the required packages to run this script might be already installed on your machine.
If you wish to know the necessary packages, look the `setup.sh` file.

After the installation, to run the program, simply navigate to the project's directory and run the `medsec.py` file using python. Running the script as root is recommended for better performance and to avoid permission errors. The used command is the following:
```
sudo python3 medsec.py
```

## Configuration
To make configurations, simply go to the configuration file at `files/conf.py` and edit it.

## How to use

### ifconfig
If you want to display your system's current TCP/IP network configuration, type the following command:

`-ifconfig`

![ifconfig](https://user-images.githubusercontent.com/61552222/134312657-b7262736-0ae0-4a39-bb72-c6dc0bc6869b.png)

### ping
To send ICMP packets to one or more hosts to check connectivity, simply type:

`-ping [HOST(s)]`

![ping](https://user-images.githubusercontent.com/61552222/137532338-ed2e2764-edec-47a5-ab1a-9c567854012d.png)

### traceroute
To diagnose route paths and measure transit delays, use the `-traceroute` command:

`-traceroute [HOST]`

![trace](https://user-images.githubusercontent.com/61552222/137626030-40511ada-52f9-4d83-b561-3491939f5d22.png)

### Port scans
Scanning ports helps detect potential security breaches by identifying the hosts connected to your network and the services running.

Multiple scan types are supported, including SYN (`-scansyn`), TCP (`-scantcp`), UDP (`-scanudp`), ACK (`-scanack`) and comprehensive scan (`-scan`).

`-scan -host [HOST(s) IP/URL]`

`-scan -host [HOST(s) IP/URL] -p [PORT(s)]`

`-scan -host [HOST(s) IP/URL] -prange [START PORT] [END PORT]`

`-scan -iprange [START IP] [END IP] -p [PORT(s)]`

`-scan -iprange [START IP] [END IP] -prange [START PORT] [END PORT]`

![scan2](https://user-images.githubusercontent.com/61552222/137121775-59692de5-e75d-45ce-86e7-34c0e12ebf6a.png)

After this scan, it is possible to see that both 22 (SSH) and 80 (HTTP) ports are open.

### Host discovery
To look for current up devices on a given network type the following command:

`-scanlan`

Then type the network you want to scan.

![scanlan2](https://user-images.githubusercontent.com/61552222/137121820-304c1270-a182-4f1e-8f5c-d52157087c9c.png)

### MAC address detection
To get a MAC address of one or more live hosts on the LAN, use the command:

`-getmac -host [HOST(s) IP]`

![getmac](https://user-images.githubusercontent.com/61552222/137489461-c7f2646f-2626-42b5-ab95-2a53407718ac.png)

### Banner grabbing
Banner grabbing is a reconnaissance technique that retrieves a software banner information. This banner usually contains important information about a network service, including but not limited to, it’s software name and version. FTP, Web, SSH, and SMTP servers often expose vital information about the software they are running in their banner.

A banner attack usually starts off with a enumeration scan to find open ports. Once you identified a service you want to target, you can send specific packets and inspect the traffic for the specified information.

To perform banner grabbing, depending on your specific needs, type one of the following commands:

`-grab -host [HOST(s) IP/URL] -p [PORT(s)]`

`-grab -iprange [START IP] [END IP] -prange [START PORT] [END PORT]`

`-grab -host [HOST(s) IP/URL] -prange [START PORT] [END PORT]`

`-grab -iprange [START IP] [END IP] -p [PORT(s)]`

![grab](https://user-images.githubusercontent.com/61552222/138929604-823b3d38-3eb3-4972-891d-6ad081e732d6.png)

### DNS checks
This feature is similar to the well known `nslookup` command used on UNIX systems. If you want to do a DNS check, type the following:

`-ns [HOST(s) IP/URL]`

![ns](https://user-images.githubusercontent.com/61552222/137627097-123581b6-857e-404d-9e60-9c422f752cb4.png)

**Disclaimer**: Note that this feature uses IPinfo API. It is recommended to change the API key to yours as the key provided might be being used by other people. To change the API keys go to the configuration file at `files/conf.py`.

### WHOIS
WHOIS is a TCP protocol that aims to consult contact and DNS.
To request the WHOIS of one or more pages, just type:

`-whois [HOST(s) IP/URL]`

![whois](https://user-images.githubusercontent.com/61552222/138929671-de9c6f37-372e-47e8-acf0-0d2ef466f84d.png)

### Subdomain enumeration
Subdomain enumeration is the process of finding valid sub-domains for one or more domain.

Sub-domain enumeration can reveal a lot of domains/sub-domains that are in scope of a security assessment which in turn increases the chances of finding vulnerabilities.

If you wish to look for common subdomains of a domain, simply type:

`-sdenum [DOMAIN]`

This command uses a default wordlist to look for subdomains. However, if you want to use your own wordlist, type:

`-sdenum [DOMAIN] -wordlist [WORDLIST PATH]`

![sdenum2](https://user-images.githubusercontent.com/61552222/137121964-05c3b6df-a0fa-4b9a-9ac3-bdcdb6dd9263.png)

### Vulnerability reconnaissance
To scan one or more hosts for vulnerabilities use the following command:

`-vulnscan -host [HOST(s) IP/URL]`

![vulnscan2](https://user-images.githubusercontent.com/61552222/139101162-b341178e-4e05-4904-a345-656cc75e7c1b.png)
![vulnscan](https://user-images.githubusercontent.com/61552222/139101140-cc77f0b1-604a-4964-bcbb-049a64d18545.png)

**Disclaimer**: Note that this feature uses Shodan API. It is recommended to change the API key to yours as the key provided might be being used by other people. To change the API keys go to the configuration file at `files/conf.py`.

### Packet sniffing
To perform packet sniffing, type:

`-sniff`

![anim sniff](https://user-images.githubusercontent.com/61552222/135460586-240e23e0-783a-4fc8-a088-1e15a0b9af3d.gif)

**Disclaimer**: If you want to sniff all the data that is passing through a network, first turn your wireless card or adapter to **monitor mode**.

### MAC spoofing
MAC spoofing is the generation of frames with a MAC address different from the address of the sending NIC.
To change the MAC address of an interface, issue the command:

`-macspoof -source [SOURCE MAC] -iface [INTERFACE]`

![macspoof](https://user-images.githubusercontent.com/61552222/137764282-dbb2948c-9d6b-4778-b5e6-2a35f01d491b.png)

As you can see in the screenshot below, the MAC address of the interface was succesfully changed.

![macspoof2](https://user-images.githubusercontent.com/61552222/137764297-0528c075-840b-4ef8-bf63-6a3bbd52f558.png)

### IP spoofing
The objective of IP spoofing is to modify the correct source IP address so that the system to which a packet is directed cannot correctly identify the sender.

Note that this command only works on machines with unpached vulnerabilities. To performe IP spoofing on a host's specific port, use the following command:

`-ipspoof -source [SOURCE IP] [SOURCE PORT] -target [TARGET IP/URL] [TARGET PORT]`

If you want to use a random source IP, type the following command:

`-ipspoof -source r [SOURCE PORT] -target [TARGET IP/URL] [TARGET PORT]`

You can also use a random source port:

`-ipspoof -source [SOURCE IP] r -target [TARGET IP/URL] [TARGET PORT]`

![ipspoof](https://user-images.githubusercontent.com/61552222/139094228-3fc3889d-46ec-4c34-83a8-b9e4e78c1ae1.png)

**Disclaimer**: Please only use this for testing purposes and target your own machines.

### SYN flooding

SYN Flood is a DDoS attack method that causes direct overhead in the transport layer (layer 4) and indirect overhead in application layer (layer 7).

To attempt SYN flooding, type:

`-synflood -source [SOURCE PORT] -target [TARGET IP/URL] [TARGET PORT]`

If you want to use a random source port, type the following command:

`-synflood -source r -target [TARGET IP/URL] [TARGET PORT]`

![synflood](https://user-images.githubusercontent.com/61552222/139092701-9e391c42-8050-4a3c-a427-a84be9e950c3.png)

**Disclaimer**: Please only use this for testing purposes and target your own machines.
### Deauth attack

A deauth attack is a type of wireless attack that targets communication between a router and one or more devices connected to that router. Effectively forcing the target machine to disconnect from the access point.

To do this attack, use the following command:

`-deauth -target [TARGET MAC] -gateway [GATEWAY MAC] -iface [INTERFACE]`

If you plan to attack all clients in a gateway, type:

`-deauth -target a -gateway [GATEWAY MAC] -iface [INTERFACE]`

![deauth](https://user-images.githubusercontent.com/61552222/136202202-2d26efce-5b01-441f-b786-8fd2c6b416dd.png)

After the command issued on the screenshot above, all the devices connected to that access point were disconnected and unable to reconnect while this script was running.

**Disclaimer**: To perform this attack, make sure you have a wireless card or adapter that supports **monitor mode** and turn it on before attempting a deauth attack.
Please only use this for testing purposes and target your own machines.

### Brute-force attack

A brute-force attack is an attempt to crack a password or username.

To perform brute-force attack and find common/weak credentials, type:

`-bruteforce [SERVICE] -target [TARGET IP/URL] -user [USERNAME]`

If you wish to use a custom wordlist, use the command:

`-bruteforce [SERVICE] -target [TARGET IP/URL] -user [USERNAME] -wordlist [WORDLIST PATH]`

For the time being, only the SSH service is supported.

**Disclaimer**: Note that the target server may have defensive mechanisms against this type of attack and block the attacker's attempts on guessing the password.
Please only use this for testing purposes and target your own machines.
## Contribution

Create a issue or pull request, or send me an email at [pafmed@outlook.com](mailto:pafmed@outlook.com).
## License

This repository is under the [**MIT License**](https://opensource.org/licenses/MIT).
