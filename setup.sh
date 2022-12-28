# Show available options

echo "1. Debian-based (Debian, Ubuntu, Kali, ParrotOS, Pop!_OS, Linux Mint, Deepin, Elementary OS, Zorin OS, MX Linux, etc) "
echo "2. RHEL-based (Red Hat Enterprise Linux, Fedora, CentOS, Rocky Linux, AlmaLinux, Oracle Linux, ClearOS, etc)"
echo "3. Arch-based (Arch, Black Arch, Manjaro, etc)"

read -p "Enter your distro [1/2/3]: " choice

if test "$choice" = "1"
then

    # Install necessary packages for Debian-based distros

    sudo apt-get install nmap
    sudo apt-get install python3-pip
    
     
elif test "$choice" = "2"
then

    # Install necessary packages for RHEL-based distros

    sudo dnf install nmap
    sudo dnf install python3-pip

elif test "$choice" = "3"
then

    # Install necessary packages for Arch-based distros

    sudo pacman -S nmap
    sudo pacman -S python3-pip

else
     echo "Invalid choice. Operation cancelled."
     exit 
fi

# Install all necessary pip packages

sudo pip3 install gnureadline
sudo pip3 install colorama

sudo pip3 install ipaddress
sudo pip3 install python-nmap
sudo pip3 install ipinfo
sudo pip3 install scapy
sudo pip3 install shodan
sudo pip3 install python-whois
sudo pip3 install paramiko
sudo pip3 install netfilterqueue


# Add main .py file to the system path (later)
#cp *.py /usr/bin
#cp methods/*.py /usr/bin
#mv /usr/bin/hawk.py /usr/bin/hawk
#chmod 755 /usr/bin/hawk
