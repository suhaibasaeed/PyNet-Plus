"""
2a. Create a new file named "my_functions.py" that will store a set of reusable functions.

Move the "open_napalm_connection" function from exercise1 into this Python file.
Import the network devices once again from my_devices.py and create a list of connection objects
(once again with connections to both cisco3 and arista1).
"""

from napalm import get_network_driver

def connect_device(device_name):
    # Get devices type field and pop it from the dict
    device_type = device_name.pop("device_type")
    # Find the the NAPALM class we want to use and return it
    driver = get_network_driver(device_type)
    # Create instance of driver class and pass in dict with device details via **kwargs
    device = driver(**device_name)

    # Establish connection to device - Netmiko used here under the hood
    device.open()
    # Return NAPALM connection object
    return device

def create_backup(napalm_conn):
    """ Retrieves the running config from a device and writes it to a file

    :param napalm_conn: NAPALM device connection
    :return:
    """
    # Retrieve running config from device via get_config
    config = napalm_conn.get_config(retrieve='running')
    # Extract the running config only from the returned dictionary
    running_config = config['running']
    # Used for naming the config files we're writing to
    device_name = napalm_conn.hostname

    # Write config to file
    with open(f"{device_name}.txt", 'w') as f:
        f.write(running_config)
    
    # Print confirmation of this
    print("{} config has successfully been backed up".format(device_name))

def create_checkpoint(napalm_conn):
    """ Retrieve a checkpoint from the NX-OS device and write it to a file

    :param napalm_conn: NAPALM device connection
    :return:
    """
    # Get checkpoint file from NXOS device representing device's current config
    checkpoint = napalm_conn._get_checkpoint_file()

    # Write checkpoint to file
    with open("nxos_checkpoint.txt", 'w') as f:
        f.write(checkpoint)
    # Print confirmation of this
    print('Checkpoint file has successfully been created')
