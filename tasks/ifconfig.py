import subprocess

def ifconfig():
    subprocess.call(['ip', 'a'])
