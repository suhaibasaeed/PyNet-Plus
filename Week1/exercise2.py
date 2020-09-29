"""
2. Add a second NX-OS device to your first exercise. Make sure you are using dictionaries to represent the two NX-OS devices.
Additionally, use a for-loop to accomplish the Netmiko connection creation.
Once again print the prompt back from the devices that you connected to.
"""
from netmiko import Netmiko
from getpass import getpass

# Get password from user
password = getpass()

# Create dictionaries that holds device details
nxos_device = {
    'host': 'nxos1.lasthop.io',
    'username': 'pyclass',
    'password': password,
    'device_type': 'cisco_nxos',
}

nxos_device2 = {
    'host': 'nxos2.lasthop.io',
    'username': 'pyclass',
    'password': password,
    'device_type': 'cisco_nxos',
}
# Loop through the 2 dictionaries connecting to each device sequentially
for device in (nxos_device, nxos_device2):
    net_connection = Netmiko(**device)
    
    # Get the devices prompt
    output = net_connection.find_prompt()
    # Print prompt to console
    print(output)

    # Gracefully disconnect from SSH session
    net_connection.disconnect()
