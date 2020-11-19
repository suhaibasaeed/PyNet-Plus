"""
3b. Use the "load" method to stage a configuration using a basic set command
for example, "set system host-name python4life".

3c. Print the diff of the current configuration with the staged configuration.
Your output should look similar to the following:

3d. Rollback the staged configuration.
Once again, print out the diff of the staged and the current configuration (which at this point should be None).
"""

from jnpr_devices import srx2 # SRX device dictionary
from jnpr.junos import Device # Device class
from jnpr.junos.utils.config import Config # Config class

# Create device object
device_conn = Device(**srx2)
device_conn.open() # Establish NETCONF connection
device_conn.timeout = 60 # Change device timeout

# Pass in NETCONF connection to Config object
cnfg = Config(device_conn)
cnfg.lock() # Lock device to others so only we can be in config mode

# Use load method to send and stage config on the device via set command - merge NOT replace
cnfg.load("set system host-name test1", format='set', merge=True)

# Exercise 3c
# Print the difference between the candidate and running config to see if the config was applied or not
print(cnfg.diff())

# Exercise 3d
# Undo the change to the candidate config we just did
cnfg.rollback(0)
# Print the difference between the candidate and running config to see if the rollback was successful or not
print(cnfg.diff())

