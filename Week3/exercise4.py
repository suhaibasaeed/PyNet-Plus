"""
4. You have the following JSON ARP data from an Arista switch:

{
    "dynamicEntries": 2,
    "ipV4Neighbors": [
        {
            "hwAddress": "dc38.e111.97cf",
            "address": "172.17.17.1",
            "interface": "Ethernet45",
            "age": 0
        },
        {
            "hwAddress": "90e2.ba5c.25fd",
            "address": "172.17.16.1",
            "interface": "Ethernet36",
            "age": 0
        }
    ],
    "notLearnedEntries": 0,
    "totalEntries": 2,
    "staticEntries": 0
}

From a file, read this JSON data into your Python program.
Process this ARP data and return a dictionary where the keys are the IP addresses and the values are the MAC addresses.
Print this dictionary to standard output.
"""

import json
from pprint import pprint

# Open file and read into file handling variable f
with open('arista_arp.json') as f:
    # load the data in and put into arista_arp variable
    arista_arp = json.load(f)

# Put ipV4Neighbors info into new dict as it is only thing we need
ipv4_info = arista_arp['ipV4Neighbors']

# Initalise new empty dictionary
new_dict = {}
# Loop through 2 dictionaries, 1 per list element and put IP and MAC in new dictionary
for arp_entry in ipv4_info:
    new_dict.update({arp_entry['address']: arp_entry['hwAddress']})

# Print new dictionary
pprint(new_dict)
