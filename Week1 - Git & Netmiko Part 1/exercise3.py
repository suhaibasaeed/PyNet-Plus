"""
3. For one of the Cisco IOS devices, use Netmiko and the send_command() method to retrieve 'show version'.
Save this output to a file in the current working directory.
"""

from netmiko import Netmiko
from getpass import getpass

# Create dictionary that holds device details
ios_device = {
    'host': 'cisco3.lasthop.io',
    'username': 'pyclass',
    'password': getpass(),
    'device_type': 'cisco_ios',
}

# Establish SSH connection to the network device using **kwargs to pull in details from dictionary
net_connection = Netmiko(**ios_device)

# Get show version command output from device
output = net_connection.send_command('show version')

# Open file in write mode to store show version output in there
f = open("show_ver.txt", mode= "w")
# write contents of output variable to new file
f.write(output)
# close file and flush contents to it
f.close

# Gracefully disconnect from SSH session
net_connection.disconnect()
