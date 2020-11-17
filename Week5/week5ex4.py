"""
4. Expand on exercise3 except use a for-loop to configure five VRFs.
Each VRF should have a unique name and a unique route distinguisher.
Each VRF should have the IPv4 and IPv6 address families controlled by conditional-variable passed into template.

Note, you will want to pass in a list or dictionary of VRFs that you loop over in your Jinja2 template.

"""

from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

# Create jinja2 environment, StrictUndefined object allows us to have error thrown if variable missing
env = Environment(undefined=StrictUndefined)
# Load the jinja2 templates using FileSystemLoader Class, look in current directory
env.loader = FileSystemLoader(".")
# Variables for template
vrf_vars = {"ipv4_enabled": True,
            "ipv6_enabled": True,
            "vrf_name": {"blue": "100:1",
                         "green": "200:2",
                         "red": "300:3",
                         "black": "400:4",
                         "yellow": "500:5",
                         }
            }
# template file
template_file = "template4.j2"
# Pass in template file via get_template method invoked on env object
template = env.get_template(template_file)
# Render template passing in variables from dictionary via **kwargs and print
output = template.render(**vrf_vars)
print(output)

