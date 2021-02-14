"""
2b. Write the data structure you created in part 2a out to a YAML file. Use expanded YAML format.
How could you re-use this YAML file later when creating Netmiko connections to devices?
"""
import yaml

device_list = [{'device_name': 'cisco3',
                'hostname': 'cisco3.lasthop.io',
                'username': 'username',
                'password': 'password',
                },
                {'device_name':  'cisco4',
                'hostname': 'cisco4.lasthop.io',
                'username': 'username',
                'password': 'password',
                },
                {'device_name': 'nxos1',
                'hostname': 'nxos1.lasthop.io',
                'username': 'username',
                'password': 'password',
                },
                {'device_name': 'nxos2',
                'hostname': 'nxos2.lasthop.io',
                'username': 'username',
                'password': 'password',
                }]

# Open file for writing with file handing variable f
with open("exercise2a.yaml", "w") as f:
    # Pass in list and file handling variable
    output = yaml.dump(device_list, f)
