"""2a. Use Python and Jinja2 to generate the below NX-OS interface configuration.
You should use an external template file and a Jinja2 environment to accomplish this.
The interface, ip_address, and netmask should all be variables in the Jinja2 template.
 
nxos1
interface Ethernet1/1
  ip address 10.1.100.1/24

nxos2
interface Ethernet1/1
  ip address 10.1.100.2/24
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
             "netmask":"/24",
             }
# template file
template_file = "template2a.j2"
# Pass in template file via get_template method invoked on env object
template = env.get_template(template_file)
# Render template passing in variables from dictionary via **kwargs and print
output = template.render(**intf_vars)
print(output)
