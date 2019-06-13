# mac_address_changer
This is a program written in python to change the MAC address for linux machines.

Requirements: 
  1. Python3 should be installed to run this program.
  2. A working network interface.
  
Both options are mandatory for the program to run.

Example : python3 mac_changer.py -i eth0 -m 00:11:22:33:44:12

Usage: mac_changer.py [options]

Options:
  -h, --help            show this help message and exit
  -i INTERFACE, --interface=INTERFACE
                        Interface to change its MAC address
  -m NEW_MAC, --mac=NEW_MAC
                        New MAC address
