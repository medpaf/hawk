#Install necessary packages
sudo apt-get install nmap
sudo apt-get install python3-pip
sudo pip3 install python-nmap

#Add main .py file to the system path (later)
cp *.py /usr/bin
cp methods/*.py /usr/bin
mv /usr/bin/vbnets.py /usr/bin/vbnets
chmod 755 /usr/bin/vbnets
