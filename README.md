# VBNetS

![Screenshot from 2021-08-03 08-02-32](https://user-images.githubusercontent.com/61552222/127938045-aa8052c3-fa9a-4cd8-82bf-edcee8e68538.png)


This is a network utility tool that I developed to perform some network and security administrator tasks. Currently, this script can perform a good variety of tasks such as:
- Port scans, including SYN, TCP, UDP, ACK and comprehensive scan;
- Banner grabbing;
- DNS checks;
- ifconfig;
- ping;
- traceroute.

Other features are still being implemented. Future implementations may include WAP (web application firewall) detection, vulnerability reconnaissance, network sniffer, some automated tasks and others.

To install the necessary packages so that the script can run withouth any problems simply run the `setup.sh` file. Currently, this file is only supported on debian based distros that as the apt package manager. If you are using any other Linux distro please install the packages manually using your distro's package manager. Depending on the specific distro used, some of the required packages to run this script might be already installed on your machine.
