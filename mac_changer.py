#!/usr/bin/env python

import subprocess
import argparse
import re

def set_arguments():
	parser = argparse.ArgumentParser(description='change MAC address')
	parser.add_argument('-i', '--interface', dest='interface', help='Interface to change MAC Address')
	parser.add_argument('-m', '--mac', dest='new_mac', help='New MAC Address')
	args = parser.parse_args()
	if not args.interface:
		parser.error('[-] Please specify an interface, use --help for more info.')
	elif not args.new_mac:
		parser.error('[-] Please set a new MAC address, use --help for more info.')
	return args

def change_mac(interface, mac_address):
	print(f'[+] Changing MAC Address for {interface} to {mac_address}')
	subprocess.call(['ifconfig', interface, 'down'])
	subprocess.call(['ifconfig', interface, 'hw', 'ether', mac_address])
	subprocess.call(['ifconfig', interface, 'up'])

def get_current_mac(interface):
	##terminal command to check the ifconfig interface
	ifconfig_result = subprocess.check_output(['ifconfig', interface])
	
	##regex module to isolate interface MAC address
	mac_address_search_result = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', ifconfig_result.decode('utf-8'))
	if mac_address_search_result:
		return mac_address_search_result.group(0)
	else:
		print('[-] Could not read MAC Address')


args = set_arguments()

current_mac = get_current_mac(args.interface)
print(f'current MAC = {current_mac}')

change_mac(args.interface, args.new_mac)

#changed mac address b/c of func^
current_mac = get_current_mac(args.interface)
if current_mac == args.new_mac:
	print(f'[+] MAC Address successfully changed to {current_mac}')
else:
	print('[-] Unable to change MAC Address')






