"""5. On both the NXOS1 and NXOS2 switches configure five VLANs including VLAN names (just pick 5 VLAN numbers between 100 - 999).
Use Netmiko's send_config_from_file() method to accomplish this.
Also use Netmiko's save_config() method to save the changes to the startup-config.
"""

from netmiko import Netmiko
from getpass import getpass

# Create dictionary that holds device details
nxos_device1 = {
    'host': 'nxos1.lasthop.io',
    'username': 'pyclass',
    'password': getpass(),
    'device_type': 'cisco_nxos',
}
nxos_device2 = {
    'host': 'nxos2.lasthop.io',
    'username': 'pyclass',
    'password': getpass(),
    'device_type': 'cisco_nxos',
}

for device in (nxos_device1, nxos_device2):

    # Establish SSH connection to the network devices using **kwargs to pull in details from dictionary
    net_connection = Netmiko(**device)

    # Send config to device from specified file
    output = net_connection.send_config_from_file('config.txt')
    # Print to console
    print(output)
    # Save to startup config
    print(net_connection.save_config())

    # Gracefully disconnect from device
    net_connection.disconnect()

