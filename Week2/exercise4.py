""" 4. Use Netmiko and the send_config_set() method to configure the following on the Cisco3 router.

ip name-server 1.1.1.1
ip name-server 1.0.0.1
ip domain-lookup

Experiment with fast_cli=True to see how long the script takes to execute (with and without this option enabled).
With fast_cli = 1.62s | Without fast_cli = 6.1a

Verify DNS lookups on the router are now working by executing 'ping google.com'. Verify from this that you receive a ping response back.
"""

from netmiko import Netmiko
from datetime import datetime # To check execution time
from getpass import getpass

cisco3_device = {
    'host': 'cisco3.lasthop.io',
    'username': 'pyclass',
    'password': getpass(),
    'device_type': 'cisco_ios',
    'fast_cli': True,    
}

# Record start time to measure execution speed of command with fast_cli enabled
start_time = datetime.now()

# Establish SSH connection to the network device using **kwargs to pull in details from dictionary
net_connect = Netmiko(**cisco3_device)

# commands to send to the router
cmd = ['ip name-server 1.1.1.1', 'ip name-server 1.0.0.1', 'ip domain-lookup']
# Send command to router with fast_cli enabled
output = net_connect.send_config_set(cmd)
print(output)

# Check if DNS lookups now working on router
print(net_connect.send_command_timing('ping google.com'))

# Disconnect from device
net_connect.disconnect()

# Record end time
end_time = datetime.now()
# Calculate total time taken and print to console
total_time = end_time - start_time
print('-' * 80)
print('Total time taken was: ' + str(total_time))
print('-' * 80)

