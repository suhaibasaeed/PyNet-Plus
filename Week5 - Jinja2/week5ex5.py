"""
5. Start with the full running-config from cisco3.lasthop.io as a base template (for example 'cisco3_config.j2').
Modify this base template such that you use Jinja2 include statements to pull in sub-templates
For the: NTP servers, the AAA configuration, and for the clock settings.

Your base template should have the following items (in the proper locations):

{% include 'aaa.j2' %}

{% include 'clock.j2' %}

{% include 'ntp.j2' %}


The child templates being pulled in should contain the NTP configuration, the AAA configuration & the clock config
NTP servers, timezone, timezone_offset & timezone_dst (DST name) should be variables in the child templates.

The output from this should be the full configuration identical to current running configuration on cisco3.lasthop.io
"""

from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

# Create jinja2 environment, StrictUndefined object allows us to have error thrown if variable missing
env = Environment(undefined=StrictUndefined)
# Load the jinja2 templates using FileSystemLoader Class, look in current directory
env.loader = FileSystemLoader(".")
# Variables for template
config_vars = {"ntp_servers": ['130.126.24.24', '152.2.21.1'],
               "timezone": "PST",
               "timezone_offset": "-8 0",
               "timezone_dst": "PDT",

               }
# template file
template_file = "cisco3_config.j2"
# Pass in template file via get_template method invoked on env object
template = env.get_template(template_file)
# Render template passing in variables from dictionary via **kwargs and print
output = template.render(**config_vars)
print(output)

