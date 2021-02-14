"""
4b. Create a new function named 'create_checkpoint'. Add this function into your my_functions.py file.
This function should take one argument, the NAPALM connection object.
This function should use the NAPALM _get_checkpoint_file() method to retrieve a checkpoint from the NX-OS device.
It should then write this checkpoint out to a file.

Recall that the NX-OS platform requires a 'checkpoint' file for configuration replace operations.
Using this new function, retrieve a checkpoint from nxos1 and write it to the local file system.

4d. Next do complete configuration replace operation (using the checkpoint file that you just retrieved and modified).
Once your candidate config is staged perform a compare_config (diff) on the configuration to see your pending changes.

After the compare_config is complete, then use the discard_config() method to eliminate the pending changes.

Next, perform an additional compare_config (diff) to verify that you have no pending configuration changes.
Do not actually perform the commit_config as part of this exercise.
"""

from my_functions import connect_device, create_checkpoint
from my_devices import nxos1
from napalm import get_network_driver

# get NXOS connection object by calling connect_device function passing in nxos1 details
nxos1_conn = connect_device(nxos1)
# Get and save checkpoint file from device by calling create_checkpoint file
create_checkpoint(nxos1_conn)

# Stage config to the device via a replace operation using checkpoint file
nxos1_conn.load_replace_candidate(filename="nxos_checkpointnew.txt")
# See difference between the candidate and running config
print('Diff before')
print(nxos1_conn.compare_config())
print('-' * 40)

# Discard changes
nxos1_conn.discard_config()
# Do diff again
print('Diff after the discard')
print(nxos1_conn.compare_config())

