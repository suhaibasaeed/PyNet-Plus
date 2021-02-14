"""
4. Note, this exercise might be fairly challenging. Construct a new YAML file that contains the four Arista switches.
This YAML file should contain all of the connection info needed to create a pyeapi connection using the connect method.
Using this inventory information and pyeapi, create script that configures the following on the 4 Arista switches:

interface {{ intf_name }}
   ip address {{ intf_ip }}/{{ intf_mask }}

The {{ intf_name }} should be a Loopback interface between 1 and 99 (for example Loopback99).

The {{ intf_ip }} should be address from the 172.31.X.X address space. The {{ intf_mask }} should be /24 or a /30.

Each Arista switch should have a unique loopback number, and a unique interface IP address.

You should use Jinja2 templating to generate the configuration for each Arista switch.

Data for {{ intf_name }} & {{ intf_ip }} should be stored in YAML file and should be associated with each Arista device.
For example, here is what 'arista4' might look like in the YAML file:

arista4:
  transport: https
  host: arista4.lasthop.io
  username: pyclass
  port: 443
  data:
    intf_name: Loopback99
    intf_ip: 172.31.1.13
    intf_mask: 30

Use pyeapi to push this configuration to the four Arista switches.
Use pyeapi and "show ip interface brief" to display the IP address table after the configuration changes have been made.
"""

import pyeapi
from getpass import getpass
import yaml
from pprint import pprint
from jinja2 import Template

# Open yaml file with device details and read it into output variable
with open('arista.yaml') as f:
    output = yaml.safe_load(f)

password = getpass()
# Loop through dictionaries and make password in device dictionary equal to getpass()
for device, value in output.items():
    value['password'] = password

    ### Jinja2 template section
    # Done inside loop so it's done for each of 4 devices
    # Dictionary containing variables
    intf_vars = value['data']
    # Jinja2 template embedded inside program
    intf_template = '''
    interface {{ intf_name }}
      ip address {{ intf_ip }}/{{ intf_mask }}
    '''
    # Template class created and template passed in
    t = Template(intf_template)
    # render method invoked on template object passing in variables dictionary
    configuration = t.render(**intf_vars)

    # Change the Jinja2 generated config from a string to a list
    new_conf = configuration.splitlines()
    # Remove 1st and 3rd element which are empty strings
    new_conf.pop(0)
    new_conf.pop(2)
    # Strip white space from strings in the list using list comprehension
    conf = [line.strip() for line in new_conf]

    ##Use pyapi to connect to devices
    # Done inside loop so each device is connected to one by one
    # Create connection object and pull in device details using **kwargs
    connection = pyeapi.client.connect(**value)
    # Create client.node object and pass in the connection object created above
    device = pyeapi.client.Node(connection)
    # Send config to device from list
    new_output = device.config(conf)
    # Print result to console - We should have 2 dictionaries returned 4 times
    print(new_output)

    # Send show ip int brief to device
    show_cmd_output = device.enable('show ip interface brief')
    # Get rid of outer list
    show_cmd_output = show_cmd_output[0]
    # Get dictionary key we want only i.e. the actual command output
    final_output = show_cmd_output['result']['output']
    print('Verification')
    print('-' * 80)
    print(final_output)
