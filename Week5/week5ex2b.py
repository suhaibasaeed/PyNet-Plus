"""2b. Expand your template so both the following interface and BGP configurations are generated for nxos1 and nxos2.
The interface name, IP address, netmask, local_as, and peer_ip should all be variables in the template.
This is iBGP so the remote_as will be the same as the local_as.
nxos1

interface Ethernet1/1
  ip address 10.1.100.1/24

router bgp 22
  neighbor 10.1.100.2 remote-as 22
    address-family ipv4 unicast


nxos2

interface Ethernet1/1
  ip address 10.1.100.2/24

router bgp 22
  neighbor 10.1.100.1 remote-as 22
    address-family ipv4 unicast
"""

from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

# Create jinja2 environment, StrictUndefined object allows us to have error thrown if variable missing
env = Environment(undefined=StrictUndefined)
# Load the jinja2 templates using FileSystemLoader Class, look in current directory
env.loader = FileSystemLoader(".")
# Variables for template
intf_vars = {"interface": "Ethernet1/1",
             "ip_address": ["10.1.100.1","10.1.100.2"],
             "netmask": "/24",
             "local_as": 22,
             "peer_ip": ["10.1.100.2","10.1.100.1"]
             }
# template file
template_file = "template2b.j2"
# Pass in template file via get_template method invoked on env object
template = env.get_template(template_file)
# Render template passing in variables from dictionary via **kwargs and print
output = template.render(**intf_vars)
print(output)
