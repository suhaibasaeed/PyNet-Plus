"""
6. Use Netmiko to retrieve 'show run' from the Cisco4 device. Feed this configuration into CiscoConfParse.

Use CiscoConfParse to find all of the interfaces on Cisco4 that have an IP address.
Print out the interface name and IP address for each interface.
Your solution should work if there is more than one IP address configured on Cisco4.
For example, if you configure a loopback interface on Cisco4 with an IP address, then your solution should continue to work.
The output from this program should look similar to the following:
$ python confparse_ex6.py 

Interface Line: interface GigabitEthernet0/0/0
IP Address Line:  ip address 10.220.88.23 255.255.255.0
"""

from getpass import getpass
from netmiko import Netmiko
from ciscoconfparse import CiscoConfParse

ios_device = {
    'host': 'cisco4.lasthop.io',
    'username': 'pyclass',
    'password': getpass(),
    'device_type': 'cisco_ios',
}

# Establish SSH connection to the network device using **kwargs to pull in details from dictionary
net_connection = Netmiko(**ios_device)
# Get running config from device and put into variable
show_run = net_connection.send_command('show run')

# Make running config string into a list so we can feed it into CiscoConfParse object
cisco_obj = CiscoConfParse(show_run.splitlines())

# Look for lines in runningt config where parent starts with 'interface' at beginning of line and child with whitespace then 'ip address'
match = cisco_obj.find_objects_w_child(parentspec=r'^interface', childspec=r'^\s+ip address')

# Loop through list of matches and print out the interface name
for line in match:
   print("Interface line: {}".format(line.text))
   # Search the children of each match for one that starts with whitespace then 'ip address'
   child_ip = line.re_search_children(r'^\s+ip address')
   # Loop through list of children where this is found and print to console
   for child in child_ip:
      print("IP address line: {}".format(child.text))
