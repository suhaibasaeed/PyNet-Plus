"""
1. Using the pyeapi library, connect to arista3.lasthop.io and execute 'show ip arp'.
From this ARP table data, print out a mapping of all of the IP addresses and their corresponding MAC addresses.
"""

import pyeapi
from getpass import getpass
from pprint import pprint

# Create connection object
connection = pyeapi.client.connect(
    transport="https",
    host="arista3.lasthop.io",
    username="pyclass",
    password=getpass(),
    port="443",
)

# Create client.node object and pass in the connection object created above
device = pyeapi.client.Node(connection)

# Send show ip arp command to device and print to console
output = device.run_commands('show ip arp')

# Get rid of outer list
output = output[0]

# We only want dictionary value with arp entries in it
output = output['ipV4Neighbors']
# Loop through entries in arp table dictionary and print out mapping of IPs to MACs
for entry in output:
    ip_addr = entry['address']
    mac_addr = entry['hwAddress']
    print('{} --> {}'.format(ip_addr, mac_addr))
