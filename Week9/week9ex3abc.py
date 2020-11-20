"""
3a. Using your existing functions and the my_devices.py file, create a NAPALM connection to both cisco3 and arista1.

3b. Create two new text files `arista1.lasthop.io-loopbacks` and `cisco3.lasthop.io-loopbacks`.
In each of these files, create two new loopback interfaces with a description.

Your files should be similar to the following:
interface loopback100
  description loopback100
!
interface loopback101
  description loopback101

For both cisco3 and arista1, use the load_merge_candidate() method to stage the candidate configuration.
In other words, use load_merge_candidate() and your loopback configuration file to stage a configuration change.

Use the NAPALM compare_config() method to print out the pending differences
(i.e. the differences between the running configuration and the candidate configuration).

3c. Commit the pending changes to each device, and check the diff once again (after the commit_config).
"""

from pprint import pprint
from my_functions import connect_device, create_backup
from my_devices import cisco3, arista1
from napalm import get_network_driver


# List of files with config in it
config_list = ["arista1.lasthop.io-loopbacks.txt", "cisco3.lasthop.io-loopbacks.txt"]


# Exercise 3a
# Call connect_device function to get connection object for both devices
cisco3_conn = connect_device(cisco3)
arista1_conn = connect_device(arista1)

# Exercise 3b
# Stage the candidate config to the device
cisco3_conn.load_merge_candidate(filename="cisco3.lasthop.io-loopbacks.txt")
# Compare the staged and running config
print(cisco3_conn.compare_config())

# Do the same for the arista device
arista1_conn.load_merge_candidate(filename="arista1.lasthop.io-loopbacks.txt")
# Compare the staged and running config
print(arista1_conn.compare_config())

# Exercise 3c
# Commit the config for both devices
cisco3_conn.commit_config()
arista1_conn.commit_config()

# Compare the staged and running config again
print('-' * 80)
print('Cisco device - config diff AFTER commit')
print(cisco3_conn.compare_config())
print('Arista device - config diff AFTER commit')
print(arista1_conn.compare_config())
