"""
7c. Using the nxapi_plumbing config_list() method, configure two loopbacks on nxos1 including interface descriptions.
Pick random loopback interface numbers between 100 and 199.
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
# Config commands to send to the device
cmds = ['interface loopback 100', 'description nxapi test lo', 'interface loopback 101', 'description nxapi test lo2']
# Send config commands list to the device
output = device.config_list(cmds)

# Loop through returned list of command output and print to the screen
for entry in output:
    print(etree.tostring(entry).decode())
    input('Press Enter to continue: ')


