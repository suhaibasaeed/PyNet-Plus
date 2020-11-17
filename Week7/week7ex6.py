"""
6a. Create an nxapi_plumbing "Device" object for nxos1.
The api_format should be "jsonrpc" and the transport should be "https" (port 8443).
Use getpass() to capture the device's password.
Send the "show interface Ethernet1/1" command to the device, parse the output, and print out the following information:

Interface: Ethernet1/1; State: up; MTU: 1500
"""

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from getpass import getpass
from nxapi_plumbing import Device # import device class
from pprint import pprint

# Disable SSL cert warning we get as we're using self-signed cert
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# Create device object
device = Device(
    api_format="jsonrpc",
    host="nxos1.lasthop.io",
    username="pyclass",
    password=getpass(),
    transport="https",
    port=8443,
    verify=False, # Turn off SSL cert verification
)
# Send show version command to the device and print
output = device.show("show interface Ethernet1/1")
# Get inner most dictionary
result = output['TABLE_interface']['ROW_interface']
# Print interface name & State + MTU from dictionary
print('Interface: Ethernet1/1; State: {}; MTU: {}'.format(result['state'], result['eth_mtu']))

