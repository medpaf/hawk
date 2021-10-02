# MedSec

[![Stars](https://img.shields.io/github/stars/medpaf/medsec.svg)]()
[![Forks](https://img.shields.io/github/forks/medpaf/medsec.svg)]()
[![Size](https://img.shields.io/github/repo-size/medpaf/medsec)]()
[![Mantained](https://img.shields.io/badge/Maintained%3F-yes-green.svg)]()
[![Linux](https://svgshare.com/i/Zhy.svg)](https://svgshare.com/i/Zhy.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Followes](https://img.shields.io/github/followers/medpaf?style=social)]()

This is a network utility tool that I developed to perform some network and security administrator tasks. 
Currently, this script can perform a good variety of tasks such as:
- Port scans, including SYN, TCP, UDP, ACK, comprehensive scan;
- Host discovery (scan for up devices on a local network);
- Banner grabbing;
- DNS checks with geolocation information;
- ifconfig;
- ping;
- traceroute;
- IP spoofing (beta);
- Packet sniffing (beta).

Other features are still being implemented. Future implementations may include WAP (web application firewall) detection, vulnerability reconnaissance, static code analysis, traffic analysis, ARP poisoning, exploits, some automated tasks and others.

![demo2](https://user-images.githubusercontent.com/61552222/134327486-753f4281-fae1-4262-89ef-087c19c8e46a.gif)

## Contents
+ [Installation](#installation)
  - [Linux](#linux)
+ [How to use](#how-to-use)
  - [Scanning ports](#scanning-ports)
  - [Host discovery (scan for devices on a local network)](#host-discovery)
  - [Banner grabbing](#banner-grabbing)
  - [DNS checks (with geolocation information)](#dns-checks)
  - [ifconfig](#ifconfig)
  - [ping](#ping)
  - [traceroute](#traceroute)
  - [IP spoofing (beta)](#ip-spoofing)
  - [Packet sniffing (beta)](#packet-sniffing)
+ [Contribution](#contribution)
+ [License](#license)

## Installation

Note that currently, this script can only run well on Linux. If you try it in on Windows or macOS, it may run, but numerous errors will appear.

### Linux

To install the necessary packages so that the script can run withouth any problems simply run the `setup.sh` script with root privileges. Currently, this installation script is only supported on debian-based distros that has the apt package manager (***Ubuntu***, ***Kali***, ***Parrot***, ***Debian***, ***PopOS***, ***Mint***, etc). On most systems, to install medsec simply run the following commands:
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

After the installation, to run the program, simply navigate to the project's directory and run the `medsec.py` file using python. Running the script as root is recommended for better performance and to avoid permission errors. The used command is the following:
```
sudo python3 medsec.py
```
## How to use
### Scanning ports
Multiple scan types are supported, including SYN (`-scansyn`), TCP (`-scantcp`), UDP (`-scanudp`), ACK (`-scanack`) and comprehensive scan (`-scan`).

`-scan -host [HOST(s)]`

`-scan -host [HOST(s)] -p [PORT(s)]`

`-scan -host [HOST(s)] -prange [START PORT] [END PORT]`

`-scan -iprange [START IP] [END IP] -p [PORT(s)]`

`-scan -iprange [START IP] [END IP] -prange [START PORT] [END PORT]`

![scan](https://user-images.githubusercontent.com/61552222/134312220-9bfbfd14-aaed-411b-8299-0169f7fefbf9.png)
After this scan, it is possible to see that both 22 (SSH) and 80 (HTTP) ports are open.

### Host discovery
To look for current up devices on a given network type the following command:

`-scanlocal`

Then type the network you want to scan.
![host-disc](https://user-images.githubusercontent.com/61552222/134312276-2e18c1cb-2c18-4239-b44e-21fc78b9fe78.png)

### Banner grabbing
To perform banner grabbing, depending on your specific needs, type one of the following commands:

`-grab -host [HOST(s)] -p [PORT(s)]`

`-grab -iprange [START IP] [END IP] -prange [START PORT] [END PORT]`

`-grab -host [HOST(s)] -prange [START PORT] [END PORT]`

`-grab -iprange [START IP] [END IP] -p [PORT(s)]`

![grab](https://user-images.githubusercontent.com/61552222/134312366-3548a436-7462-4e3a-8304-dc2befb74c3a.png)

### DNS checks
This feature is similar to the well known `nslookup` command used on UNIX systems. If you want to do a DNS check, type the following:

`-ns [HOST(s)]`

![dns](https://user-images.githubusercontent.com/61552222/134312444-fe74ff4a-76d1-4bef-9093-e83cdebe50e6.png)

### ifconfig
If you want to display your system's current TCP/IP network configuration, type the following command:

`-ifconfig`

![ifconfig](https://user-images.githubusercontent.com/61552222/134312657-b7262736-0ae0-4a39-bb72-c6dc0bc6869b.png)

### ping
To send ICMP packets to a host to check connectivity, simply type:

`-ping [HOST]`

![ping](https://user-images.githubusercontent.com/61552222/134312705-9e7237c1-dfe4-470b-9b35-f9560884d039.png)

### traceroute
To diagnose route paths and measure transit delays, use the `-traceroute` command:

`-traceroute [HOST]`

![traceroute](https://user-images.githubusercontent.com/61552222/134312735-7f185efd-4264-4fbb-96d8-91a053d0ff6e.png)

### IP spoofing
Note that this command only works on machines with unpached vulnerabilities. To performe IP spoofing on a host's specific port, use the following command:

`-spoof -host [HOST] -p [PORT]`

![anim ddos](https://user-images.githubusercontent.com/61552222/135481491-a24e689c-ba4b-4eb4-933b-2be9c85fcddb.gif)

**Disclaimer**: Please only use this for testing purposes and target your own machines.

### Packet sniffing
To perform packet sniffing, type:

`-sniff`

![anim sniff](https://user-images.githubusercontent.com/61552222/135460586-240e23e0-783a-4fc8-a088-1e15a0b9af3d.gif)

## Contribution

Create a issue or pull request, or send me an email at [pafmed@outlook.com](mailto:pafmed@outlook.com).
## License

This repository is under the [***MIT License***](https://opensource.org/licenses/MIT).


