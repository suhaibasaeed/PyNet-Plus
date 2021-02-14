"""
5a. Connect to the srx2 device. Using an RPC call, gather and pretty-print the "show version" information.
Recall that you can retrieve RPC method name by running "show version | display xml rpc" argument.
Also don't forget to convert the hyphens to underscores.

Your output should match the following:
<software-information>
<host-name>srx2</host-name>
<product-model>srx110h2-va</product-model>
<product-name>srx110h2-va</product-name>
<jsr/>
<package-information>
<name>junos</name>
<comment>JUNOS Software Release [12.1X46-D35.1]</comment>
</package-information>
</software-information>
"""

from jnpr.junos import Device
from lxml import etree # Etree class
from getpass import getpass
from pprint import pprint
from jnpr_devices import srx2

# Create device object
device_conn = Device(**srx2)
# Establish connection to the device using NETCONF
device_conn.open()

# Invoke rpc call to the device to get the show version output
xml_ouput = device_conn.rpc.get_software_information()
# Use tostring method to change to unicdoe string and then print
print(etree.tostring(xml_ouput, encoding='unicode', pretty_print=True))
