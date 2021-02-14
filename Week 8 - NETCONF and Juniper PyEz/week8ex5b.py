"""
5b. Using a direct RPC call, gather the output of "show interfaces terse". Print the output to standard out.
"""

from jnpr.junos import Device
from lxml import etree # Etree class
from pprint import pprint
from jnpr_devices import srx2

# Create device object
device_conn = Device(**srx2)
# Establish connection to the device using NETCONF
device_conn.open()

# Invoke rpc call to the device to get the show interfaces terse output in normalised fashion for readability
xml_ouput = device_conn.rpc.get_interface_information(terse=True, normalize=True)
# Use tostring method to change to unicdoe string and then print
print(etree.tostring(xml_ouput, encoding='unicode', pretty_print=True))
