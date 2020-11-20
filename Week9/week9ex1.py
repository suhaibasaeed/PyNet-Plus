"""
1b.Create a simple func that accepts the NAPALM device info from my_devices.py and creates a NAPALM connection object.
This function should open the NAPALM connection to the device and should return the NAPALM connection object.

1c. Using devices file function, create a list of NAPALM connection objects to 'cisco3' and 'arista1'.

1d. Iterate through the connection objects, print out the device's connection object itself.
Additionally, pprint the facts for each device & also print out the device's NAPALM platform type (ios, eos, et cetera).
"""

from pprint import pprint
from napalm import get_network_driver # import Class
from my_devices import cisco3, arista1

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
# Exercise 1c
# List of devices to loop through
device_list = [cisco3, arista1]
# List for NAPALM connection objects to go inside
napalm_list = []

# Loop through the device list
for d in device_list:
    # Append each connection object to the empty list by calling the function on each device
    napalm_list.append(connect_device(d))

# Exercise 1d
# Loop through napalm_list
for napalm_device in napalm_list:
    # Print connection object
    print(napalm_device)
    # print the devices facts
    pprint(napalm_device.get_facts())
    # print the device NAPALM platform type
    platform = napalm_device.platform
    print("This devices NAPALM platform is {}".format(platform))
    print('-' * 80)

