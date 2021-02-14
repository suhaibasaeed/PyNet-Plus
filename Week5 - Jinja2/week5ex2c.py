"""
2c. Use Netmiko to push the configurations generated in exercise 2b to the nxos1 device and to the nxos2 device, respectively.
Verify you are able to ping between the devices and also verify that the BGP session reaches the established state.
Note, you might need to use an alternate interface besides Ethernet 1/1 (you can use either Ethernet 1/1, 1/2, 1/3, or 1/4).
For this exercise you should store your Netmiko connection dictionaries in an external file named my_devices.py
Import nxos1, and nxos2 from that external file.
Make sure that you use getpass() to enter the password in for these devices
"""

from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
from netmiko import Netmiko
from my_devices import nxos1, nxos2
import time

# Create jinja2 environment, StrictUndefined object allows us to have error thrown if variable missing
env = Environment(undefined=StrictUndefined)
# Load the jinja2 templates using FileSystemLoader Class, look in current directory
env.loader = FileSystemLoader(".")
# Variables for template
intf_vars = {"interface": "Ethernet1/1",
             "ip_address": ["10.1.100.1","10.1.100.2"],
             "netmask": "/24",
             "local_as": 22,
             "peer_ip": ["10.1.100.2","10.1.100.1"]
             }
# template file
template_file = "template2c.j2"
# Pass in template file via get_template method invoked on env object
template = env.get_template(template_file)
# Render template passing in variables from dictionary via **kwargs and print
output = template.render(**intf_vars)

# Split list of config so we have one command per list entry
new = output.splitlines()
# Remove headers
new.remove('nxos1')
new.remove('nxos2')
# Get rid of null strings in the list
new = list(filter(None, new))
# Strip white space from strings in the list using list comprehension
new = [line.strip() for line in new]

# Create list slices from original list with each devices corresponding config
nxos1_config = new[:5] # Index 0  to Index 4 list slice
nxos2_config = new[5:] # Index 5 to 9 list slice.

x = 0
# Connect to each device one by one
for device in (nxos1, nxos2):
    net_connection = Netmiko(**device)
    if x == 0: # Send config to first device
        output = net_connection.send_config_set(nxos1_config)
        print(output)
    if x == 1: # Send config to 2nd device
        output = net_connection.send_config_set(nxos2_config)
        print(output)
        # Sleep for 20s allowing time for BGP connection to establish
        time.sleep(20)
        # Verify that the BGP neighbourship has formed
        output += net_connection.send_command('show ip bgp neighbors')
        # Check that neighbour is in Established state and print confirmation
        if 'BGP state = Established' in output:
            print('-' * 80)
            print('BGP neighbourship has been established')

    # Gracefully disconnect from SSH session
    net_connection.disconnect()
    # increment loop counter
    x += 1
