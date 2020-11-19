"""
4a. Using the previously created jnpr_devices.py file, open a connection to srx2 and gather the current routing table

4b. Using PyEZ stage a configuration from a file. The file should be "conf" notation.
This configuration should add two static host routes (routed to discard).
These routes should be from the RFC documentation range of 203.0.113.0/24 - Any /32 in that range
Use "merge=True" for this configuration. For example:

routing-options {
    static {
        route 203.0.113.5/32 discard;
        route 203.0.113.200/32 discard;
    }
}

4c. Reusing gather_routes() function from exercise2, retrieve routing table before and after your configuration change.
Print out the differences in the routing table (before and after the change).
To simplify the problem, you can assume that the only change will be *additional* routes added by your script.

4d. Using PyEZ delete the static routes that you just added.
You can use either load() and set operations or load() plus a configuration file to accomplish this.
"""

from jnpr_devices import srx2 # Dictionary with SRX details
from jnpr.junos import Device # Device class
from jnpr.junos.utils.config import Config # Config class
from jnpr.junos.op.routes import RouteTable # RouteTable Class
from pprint import pprint

def gather_routes():
    '''Return the routing table from the device'''
    # Pass in NETCONF connection to RouteTable object
    routing_table = RouteTable(device_conn)
    # Retrieve routing table entries in dictionary like format
    routing_table.get()
    # Return keys and values of data structure
    return routing_table.items()

if __name__ == '__main__':

    # Create instance of device object
    device_conn = Device(**srx2)
    # Establish the NETCONF connection
    device_conn.open()
    # Call the gather_routes function to get the routing tale of the device
    old_routing_table = gather_routes()
    # Print the routing table
    print("Routing table before the change")
    pprint(old_routing_table)
    print('-' * 40)

    # Exercise 4b
    # Increase the timeout
    device_conn.timeout = 60
    # Pass NETCONRF connection into Config Object
    cnfg = Config(device_conn)
    # Lock configuration exclusively to us
    cnfg.lock()
    # Load configuration from external file in curly brace notation
    cnfg.load(path='routing.conf', format='text', merge=True)
    # Commit the configuration
    cnfg.commit()

    # Exercise 4c
    new_routing_table = gather_routes()
    # Print the routing table after the change so we can compare
    print("Routing table after the change")
    pprint(new_routing_table)

    # Print the differences in the routing table
    new_routing_table = dict(new_routing_table)
    print('-' * 40)
    print("The new entries in the routing table are: ")
    # Loop through the routing table items looking for the new entries and print them
    for key, value in new_routing_table.items():
        if key == '203.0.113.5/32' or key == '203.0.113.200/32': # If keys are equal to the new routes added
            print(key)
            print(value)

    # Exercise 4d
    # Delete the 2 static routes we added by loading config from external file but this time replacing NOT merging
    cnfg.load(path='del_routing.conf', format='text', merge=False)

    cnfg.unlock()

