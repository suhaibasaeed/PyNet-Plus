"""Create a Netmiko connection to the 'nxos2' device using a global_delay_factor of 2.
Execute 'show lldp neighbors detail' and print the returned output to standard output.
Execute 'show lldp neighbors detail' a second time using send_command() with a delay_factor of 8.
Print the output of this command to standard output. Use the Python datetime library to record the execution time of both of these commands.
Print these execution times to standard output.
"""

from netmiko import Netmiko
from datetime import datetime # To check execution time
from getpass import getpass

# Create dictionary that holds device details
nxos_device = {
    'host': 'nxos2.lasthop.io',
    'username': 'pyclass',
    'password': getpass(),
    'device_type': 'cisco_nxos',
    'global_delay_factor': 2,
}
# Record start time to measure execution speed
start_time = datetime.now()

# Establish SSH connection to the network device using **kwargs to pull in details from dictionary
net_connect = Netmiko(**nxos_device)
# Send show lldp neighbours details command to device
output = net_connect.send_command('show lldp neigh detail')
# Print output
print(output)
print('-' * 80)
# Record end time
end_time = datetime.now()
# Calculate & print total time
total_time = end_time - start_time
print('Total time taken was: ' + str(total_time))
print('-' * 80)

# Record start time to measure execution speed & send command to device
start_time = datetime.now()
output = net_connect.send_command('show lldp neigh detail', delay_factor=8)
# Print output
print(output)
# disconnect from the device
net_connect.disconnect()
# Record end time
end_time = datetime.now()
# Calculate total time
total_time = end_time - start_time
print('-' * 80)
print('Total time taken was: ' + str(total_time))
print('-' * 80)
