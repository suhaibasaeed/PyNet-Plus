"""
2b. Create a Python module named 'my_funcs.py'. In this file create two functions:
function1 should read the YAML file you created in exercise 2a and return the corresponding data structure;

function2 should handle the output printing of the ARP entries
(in other words, create a separate function that handles all printing to standard out of the 'show ip arp' data).

Create new program based on ex2a but YAML file loading and the output printing done using the functions in my_funcs.py
"""

from my_funcs import function1, function2
import pyeapi

if __name__ == '__main__':
    # call function which will read in yaml file and format it properly
    device_dict = function1('arista4.yaml')

    # Create connection object and pull in device details using **kwargs
    connection = pyeapi.client.connect(**device_dict)
    # Create client.node object and pass in the connection object created above
    device = pyeapi.client.Node(connection)
    # Send show ip arp command to device
    output = device.run_commands('show ip arp')
    # Call function 2 to deal with output of show ip arp command and print mappings
    function2(output)

