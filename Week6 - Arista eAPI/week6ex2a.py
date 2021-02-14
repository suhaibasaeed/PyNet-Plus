"""
2a. Define an Arista device in an external YAML file (use arista4.lasthop.io for the device).
In your YAML file, make sure the key names exactly match the names required for use with pyeapi and connect() method.
In other words, you should be able to execute 'connect(**device_dict)' where device_dict was retrieved from YAML file.

Do not store the lab password in this YAML file, instead set the password using getpass() in your Python program.
Using this Arista device information stored in a YAML file, repeat the 'show ip arp' retrieval using pyeapi.
Once again, from ARP table data, print out a mapping of all of the IP addresses and their corresponding MAC addresses.
"""

import pyeapi
from getpass import getpass
import yaml
from pprint import pprint

password = getpass()

# Open yaml file with device details and read it into output variable
with open('arista4.yaml') as f:
    output = yaml.safe_load(f)

# Remove outer dictionary
device_dict = output['arista4']
# Make password in device dictionary equal to getpass()
device_dict['password'] = password

# Create connection object and pull in device details using **kwargs
connection = pyeapi.client.connect(**device_dict)

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
