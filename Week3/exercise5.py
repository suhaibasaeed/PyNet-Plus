"""
5. In your lab environment, there is a file located at ~/.netmiko.yml.
This file contains all of the devices used in the lab.
Create a Python program that processes this YAML file and then uses Netmiko to connect to the Cisco3 router.
Print out the router prompt from this device.

Note, the device dictionaries in the .netmiko.yml file use key-value pairs designed to work directly with Netmiko.
The .netmiko.yml also contains group definitions for: cisco, arista, juniper, and nxos groups. These group definitions are lists of devices.
Once again, don't check the .netmiko.yml into GitHub.
"""
import yaml
from netmiko import Netmiko

# Open file and read with file handling variable f
with open('netmiko.yaml') as f:
    # Load file into output variable
    output = yaml.load(f)

# Put cisco3 device dictionary in new variable
cisco3_dict = output['cisco3']

# Establish SSH connection to the network device using **kwargs to pull in details from dictionary
net_connection = Netmiko(**cisco3_dict)
# Get the devices prompt
output = net_connection.find_prompt()
# Print prompt to console
print(output)

# Gracefully disconnect from SSH session
net_connection.disconnect()
