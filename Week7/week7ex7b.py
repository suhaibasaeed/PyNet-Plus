"""
7b. Run the following two show commands on the nxos1 device using a single method and passing in a list of commands:
"show system uptime" and "show system resources".
Print the XML output from these two commands.
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

cmds = ['show system uptime', 'show system resources']
# Send show commands to the device and print
output = device.show_list(cmds)

# Loop through returned list of command output and print to the screen
for entry in output:
    print(etree.tostring(entry).decode())
    input('Press Enter to continue: ')


