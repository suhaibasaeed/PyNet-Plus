from pprint import pprint
from my_functions import connect_device, create_backup
from my_devices import cisco3, arista1

# List of devices to loop through
device_list = [cisco3, arista1]
# List for NAPALM connection objects to go inside
napalm_list = []

# Loop through the device list
for d in device_list:
    # Append each connection object to the empty list by calling the function on each device
    napalm_list.append(connect_device(d))

# Loop through the list of NAPALM connection objects
for napalm_device in napalm_list:

    print('ARP table for {} device:'.format(napalm_device.platform))
    pprint(napalm_device.get_arp_table()) # USe getter to print devices ARP table
    print('-' * 80)
    print()

    # Exercise 2c
    # Gracefully catch the exception we get from trying the get_ntp_method against the uncompatible Arista device
    try:
        print('NTP peers for {} device:'.format(napalm_device.platform))
        print(napalm_device.get_ntp_peers()) # Use getter to print devices NTP peers
        print('-' * 80)
    except NotImplementedError: # If method doesn't work this error is thrown
        print("This method doesn't work with this platform")


    # Exercise 2d
    create_backup(napalm_device)
