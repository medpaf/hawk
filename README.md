# MedSec

![Screenshot from 2021-08-21 10-45-59](https://user-images.githubusercontent.com/61552222/130434037-3867ec45-93cb-45e1-b93a-935055a7da65.png)


This is a network utility tool that I developed to perform some network and security administrator tasks. Currently, this script can perform a good variety of tasks such as:
- Port scans, including SYN, TCP, UDP, ACK and comprehensive scan;
- Banner grabbing;
- DNS checks;
- ifconfig;
- ping;
- traceroute.

Other features are still being implemented. Future implementations may include WAP (web application firewall) detection, vulnerability reconnaissance, offensive tasks such as packet sniffing, ARP poisoning, DOS attacks, some automated tasks and others.

To install the necessary packages so that the script can run withouth any problems simply run the `setup.sh` file. Currently, this file is only supported on debian based distros that as the apt package manager. If you are using any other Linux distro please install the packages manually using your distro's package manager. Depending on the specific distro used, some of the required packages to run this script might be already installed on your machine.
