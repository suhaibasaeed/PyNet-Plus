"""
5c. Modify the previous task to capture "show interface terse", but this time only for "fe-0/0/7".
Print the output to standard out. Use normalize=True in the RPC method call to make the output more readable.

You will also need to add pretty_print=True to the etree.tostring() call. Consequently, your code should be similar to the following:
xml_out = dev.rpc.get_interface_information(interface_name="fe-0/0/7", terse=True, normalize=True)
print(etree.tostring(xml_out, pretty_print=True, encoding="unicode"))
"""

from jnpr.junos import Device
from lxml import etree # Etree class
from pprint import pprint
from jnpr_devices import srx2

# Create device object
device_conn = Device(**srx2)
# Establish connection to the device using NETCONF
device_conn.open()

# Invoke rpc call to the device to get the show interface terse output for fe0/0/7 with normalised output
xml_ouput = device_conn.rpc.get_interface_information(interface_name="fe-0/0/7", terse=True, normalize=True)
# Use tostring method to change to unicdoe string and then print
print(etree.tostring(xml_ouput, encoding='unicode', pretty_print=True))
