"""
1. In the lab environment use Netmiko to connect to one of the Cisco NX-OS devices.
You can find the IP addresses and username/passwords of the Cisco devices in the 'Lab Environment' email or alternatively in the ~/.netmiko.yml file.
Simply print the router prompt back from this device to verify you are connecting to the device properly.
"""
from netmiko import Netmiko
from getpass import getpass

# Create dictionary that holds device details
nxos_device = {
    'host': 'nxos1.lasthop.io',
    'username': 'pyclass',
    'password': getpass(),
    'device_type': 'cisco_nxos',
}

# Establish SSH connection to the network device using **kwargs to pull in details from dictionary
net_connection = Netmiko(**nxos_device)
# Get the devices prompt
output = net_connection.find_prompt()
# Print prompt to console
print(output)

# Gracefully disconnect from SSH session
net_connection.disconnect()
