if [ -x "$(command -v apt-get)" ]; then
	detection=1
	printf "apt package manager detected.\n"
elif [ -x "$(command -v dnf)" ]; then
	detection=2
	printf "dnf package manager detected.\n"
elif [ -x "$(command -v pacman)" ]; then
	detection=3
	printf "pacman package manager detected.\n"
else
	detection=0
	printf "Package manager not found. Install manually: $packages\n">&2; fi

printf "\n1. apt\n2. dnf\n3. pacman\n"
read -p "Enter choice (Enter for default): " choice

if [[ ("$detection" == "1" && "$choice" == "") || "$choice" == "1" ]]; then
	
    # Install necessary packages with apt
    sudo apt-get install nmap
    sudo apt-get install python3-pip    
     
elif [[ ("$detection" == "2" && "$choice" == "") || "$choice" == "2" ]]; then
	
    # Install necessary packages with dnf

	sudo dnf install nmap
    sudo dnf install python3-pip

elif [[ ("$detection" == "3" && "$choice" == "") || "$choice" == "3" ]]; then
	
    # Install necessary packages with pacman

    sudo pacman -S nmap
    sudo pacman -S python3-pip

else echo "Unable to install dependencies!"; exit; fi

# Install all necessary pip packages

sudo pip3 install readline
sudo pip3 install binascii
sudo pip3 install struct
sudo pip3 install textwrap
sudo pip3 install multiprocessing
sudo pip3 install threading
sudo pip3 install queue
sudo pip3 install subprocess
sudo pip3 install time

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
