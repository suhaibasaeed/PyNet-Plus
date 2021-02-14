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

b. Use send_command() and the expect_string argument to handle the additional prompting. Once again specify a target IP address of '8.8.8.8'.
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
# Send extended ping command to device & look for [ in additional prompt
output = net_connect.send_command('ping', expect_string=r'\[')

# Deal with additional prompting & give IP address of ping
output += net_connect.send_command('\n', expect_string=r'IP')
output += net_connect.send_command('8.8.8.8', expect_string=r'\[')

# Press enter 4 times to use ping default settings 
while i <= 3:
    output += net_connect.send_command('\n', expect_string=r'\[')
    i += 1

output += net_connect.send_command('\n', expect_string=r'Success')

# print result to console
print(output)

# Gracefully disconnect from device
net_connect.disconnect()
