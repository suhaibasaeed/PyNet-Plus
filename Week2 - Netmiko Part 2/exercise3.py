"""
3. On your AWS lab server, look at the ntc-templates index file (at ~/ntc-templates/templates/index).
Look at some of the commands available for cisco_ios (you can use 'cat ~/ntc-templates/templates/index | grep cisco_ios' to see this).
Also look at some of the abbreviated forms of Cisco IOS commands that are supported in the index file.

Create a script using Netmiko that executes 'show version' and 'show lldp neighbors' against the Cisco4 device with use_textfsm=True.

What is the outermost data structure that is returned from 'show lldp neighbors' (dictionary, list, string, something else)?
The Cisco4 device should only have one LLDP entry (the HPE switch that this router connects to). From this LLDP data, print out the remote device's interface.
In other words, print out the port number on the HPE switch that Cisco4 connects into.
"""

from netmiko import Netmiko
from getpass import getpass

# Create dictionary that holds device details
cisco4_device = {
    'host': 'cisco4.lasthop.io',
    'username': 'pyclass',
    'password': getpass(),
    'device_type': 'cisco_ios',
}

# Establish SSH connection to the network device using **kwargs to pull in details from dictionary
net_connect = Netmiko(**cisco4_device)

# Get structured show version command output from device using TextFSM
output = net_connect.send_command('show version', use_textfsm=True)

# Print to console
print(output)

print('-' * 80)
# Get structured show lldp neigh output from device using TextFSM
output = net_connect.send_command('show lldp neighbors', use_textfsm=True)
# Print to console
print(output)

# Print the remote device's interface from LLDP data by accessing dict key
print('The remote devices interface is: ' + str(output[0]['neighbor_interface']))
