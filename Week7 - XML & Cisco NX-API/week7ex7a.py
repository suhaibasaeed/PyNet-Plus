"""
6a. Create an nxapi_plumbing "Device" object for nxos1.
The api_format should be "xml" and the transport should be "https" (port 8443).
Use getpass() to capture the device's password.
Send the "show interface Ethernet1/1" command to the device, parse the output, and print out the following information:

Interface: Ethernet1/1; State: up; MTU: 1500
"""

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from getpass import getpass
from lxml import etree
from nxapi_plumbing import Device # import device class
# Disable SSL cert warning we get as we're using self-signed cert
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# Create device object
device = Device(
    api_format="xml",
    host="nxos1.lasthop.io",
    username="pyclass",
    password=getpass(),
    transport="https",
    port=8443,
    verify=False, # Turn off SSL cert verification
)
# Send show version command to the device and print
output = device.show("show interface Ethernet1/1")

# Find interface name in returned XML tree
interface = output.find(".//interface").text
# Find interface state in XML tree
state = output.find(".//state").text
# Find MTU in XML tree
eth_mtu = output.find(".//eth_mtu").text

# Print interface name & State + MTU from dictionary
print('Interface: {}; State: {}; MTU: {}'.format(interface, state, eth_mtu))
