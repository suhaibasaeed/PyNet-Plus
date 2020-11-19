"""
2b. Create a Python program that creates a PyEZ Device connection to srx2 (using the previously created Python module).
Using this PyEZ connection and the RouteTable and ArpTable views retrieve the routing table and the arp table for srx2.

This program should have four separate functions:
1. check_connected() - Verify that NETCONF connection is working. Use .connected attribute to check connection status
2. gather_routes() - Return the routing table from the device.
3. gather_arp_table() - Return the ARP table from the device.
4. print_output() - A function that takes Juniper PyEZ Device object, routing table, ARP table then prints out the:
hostname, NETCONF port, username, routing table, ARP table

This program should be structured such that all of the four functions could be reused in other class8 exercises.
"""

from jnpr_devices import srx2 # Dictionary with SRX details
from jnpr.junos import Device # Device class
from jnpr.junos.op.arp import ArpTable # ARPTable Class
from jnpr.junos.op.routes import RouteTable # RouteTable Class
from pprint import pprint


def check_connected():
    '''Verify the NETCONF connection is working'''
    # Use connected attribute to see if connection was successful and print
    if device_conn.connected:
        print("The NETCONF connection has successfully been established")
    else:
        print("NETCONF connection was not successful")

def gather_routes():
    '''Return the routing table from the device'''
    # Pass in NETCONF connection to RouteTable object
    routing_table = RouteTable(device_conn)
    # Retrieve routing table entries in dictionary like format
    routing_table.get()

    return routing_table

def gather_arp_table():
    '''Return the ARP table from the device'''
    # Pass in NETCONF connection to the ARPTable object
    arp_entries = ArpTable(device_conn)
    # Retrieve the ARP entries in dictionary like format
    arp_entries.get()

    return arp_entries

def print_output(device_object, routing_table, arp_table):
    '''Print out hostname, NETCONF Port, Username, Routing table and ARP table.
    
    Parameters:
    device_object: Device object
    routing_table: RoutingTable object (Dictionary like structure)
    arp_table: ARPTable object (Dictionary like structure)

    '''
    # Get device hostname, port and username via respective attributes and then print
    device_hostname = device_object.hostname
    device_port =  device_object.port
    device_username = device_object.user
    print("The hostname is: {} ".format(device_hostname))
    print("The username is: {}".format(device_username))
    print("The port being used is: {}".format(device_port))
    print('-' * 40)
    # Print routing table
    print("Routing table")
    # Loop through outer routing_table strucutre and print key
    for k, v in routing_table.items():
        print(k)
        new_v = dict(v) # Change innter data structure from list to dictionary
        # Loop through inner dictionary and print arp entries
        for key, value in new_v.items():
            print("{} -> {}".format(key, value))
        print('*' * 30)
    # Print ARP table
    print('-' * 40)
    print("ARP Table")
    pprint(arp_table.items())


if __name__ == '__main__':

    # Create instance of device object
    device_conn = Device(**srx2)
    # Establish the NETCONF connection
    device_conn.open()

    # Call check_connection function to see if NETCONF connection works
    check_connected()
    # Call gather_routes function and put returned value in routing_table variable
    routing_table = gather_routes()
    # Call gather_arp_table function and put returned value in arp_table variable
    arp_table = gather_arp_table()
    # Call print_output function passing in the PyEz device_conn object, routing_table and arp_table objects
    print_output(device_conn, routing_table, arp_table)

