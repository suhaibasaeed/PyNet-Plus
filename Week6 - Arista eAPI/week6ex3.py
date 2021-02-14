"""
3. Using your external YAML file and your function located in my_funcs.py, use pyeapi to connect to arista4.lasthop.io
retrieve "show ip route". From routing table, extract all of the static and connected routes from the default VRF.

Print these routes to the screen and indicate whether the route is a connected route or a static route.
In the case of a static route, print the next hop address.
"""

import pyeapi
from my_funcs import function1, function2

# Call function which will read in yaml file and format it properly
device_dict = function1('arista4.yaml')

# Create connection object and pull in device details using **kwargs
connection = pyeapi.client.connect(**device_dict)
# Create client.node object and pass in the connection object created above
device = pyeapi.client.Node(connection)
# Send show ip arp command to device
output = device.run_commands('show ip route')

# Get rid of outer one element list
output = output[0]
# Parse through nested dictionaries and only get values in dictionary keys we need
output = output['vrfs']
new_output = output['default']
new_output = new_output['routes']

# Loop through outer dictionary and print each route in routing table followed by if it's connected/static
for route, value in new_output.items():
    print('-' * 40)
    print('{} - Route Type is: {}'.format(route, value['routeType']))
    # If it's static loop through inner dictionary to find next hop IP address
    if value['routeType'] == 'static':
        for k, v in value.items():
            if k == 'vias': # key that holds next hop info
                nexthop_dict = v[0] # get rid of outer list
                # Return value from nexthopAddr key and print
                print('Next hop address is: {}'.format(nexthop_dict['nexthopAddr']))
                print('-' * 40)

