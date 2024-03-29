#!/usr/bin/env python

import subprocess
import optparse
import re

#Gets the command line arguments and checks if interface and the new_mac address is displayed or not if it doesn't it displays the appropriate message.
#It also builds the help menu using the optparse package.
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not options.new_mac:
        parser.error("[-] Please specify an newmac, use --help for more info.")
    return options

#It accepts the interface and new mac address. It changes the mac address for the desired interface to the desired mac address.
def change_mac(interface, new_mac):
    print("[+] Changing mac address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

#It gets the mac address using ifconfig and displays only the mac address using regex.
def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface]).decode("utf-8")
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read the MAC address")

#it gets the command line arguments from the get_arguments function and passes it to other functions.
options = get_arguments()

current_mac = get_current_mac(options.interface)
print("Current mac address is : "+str(current_mac))

change_mac(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)
#It displays the appropriate message
if (options.new_mac == current_mac):
    print("[+] Mac Address changed successfully.")
    print("[+] Your current MAC address is : "+ current_mac)
else:
    print("[-] Sorry, Unable to change the mac address.")
