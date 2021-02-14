"""
1. Use the extended 'ping' command and Netmiko on the 'cisco4' router.
This should prompt you for additional information as follows:

cisco4#ping
Protocol [ip]: 
Target IP address: 8.8.8.8
Repeat count [5]: 
Datagram size [100]: 
Timeout in seconds [2]: 
Extended commands [n]: 
Sweep range of sizes [n]: 
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 8.8.8.8, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/4 ms

a. Use send_command_timing() to handle the additional prompting from this 'ping' command. Specify a target IP address of '8.8.8.8'
"""

from netmiko import ConnectHandler
from getpass import getpass

# While loop variable
i = 0

cisco4_device = {
    'host': 'cisco4.lasthop.io',
    'username': 'pyclass',
    'password': getpass(),
    'device_type': 'cisco_ios',
}

# Connect to device 
net_connect = ConnectHandler(**cisco4_device)
# Find prompt of device
print(net_connect.find_prompt())
# Send extended ping command to device
output = net_connect.send_command_timing('ping')

# Deal with additional prompting & give IP address of ping
output += net_connect.send_command_timing('\n')
output += net_connect.send_command_timing('8.8.8.8')

# Press enter 5 times to use ping default settings 
while i <= 4:
    output += net_connect.send_command_timing('\n')
    i += 1

# print result to console
print(output)

# Gracefully disconnect from device
net_connect.disconnect()
