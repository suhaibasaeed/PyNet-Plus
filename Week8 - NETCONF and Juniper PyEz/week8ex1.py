"""
1a. Create a PyEZ Device object from the jnpr.junos Device class.
This device object should connect to "srx2.lasthop.io".
Use getpass() to enter the device's password. Pretty print all of the device's facts.
Additionally, retrieve and print only the "hostname" fact.
"""

from jnpr.junos import Device # Import device class
from getpass import getpass
from pprint import pprint

password = getpass() # Get password from user

# Create instance of the device object
srx_device = Device(host="srx2.lasthop.io", user="pyclass", password=password)

# Establish NETCONF connection to device via open method
srx_device.open()
# Get facts from the device and print
device_facts = srx_device.facts
pprint(device_facts)
print('-' * 80)
# Get and print hostname only
hostname = device_facts['hostname']
print('The device hostname is {}'.format(hostname))
