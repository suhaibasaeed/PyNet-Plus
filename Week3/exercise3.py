"""
3. NAPALM using nxos_ssh has the following data structure in one of its unit tests (the below data is in JSON format). 
Read this JSON data in from a file.

From this data structure extract all of the IPv4 and IPv6 addresses that are used on this NXOS device.
From this data create two lists: 'ipv4_list' and 'ipv6_list'.
The 'ipv4_list' should be a list of all of the IPv4 addresses including prefixes; the 'ipv6_list' should be a list of all of the IPv6 addresses including prefixes.
"""

import json
from pprint import pprint

# Open file and read into file handling variable f
with open('exercise3.json') as f:
    # load the data in and put into napalm_dict variable
    napalm_dict = json.load(f)

#pprint(napalm_dict)
#print('-' * 80)

napalm_dict = napalm_dict['Ethernet2/1']

for intf_name, ip_data in napalm_dict.items():
    print(intf_name)
    print(ip_data)
