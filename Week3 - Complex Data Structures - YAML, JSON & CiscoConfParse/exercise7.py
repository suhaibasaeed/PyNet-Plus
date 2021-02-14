"""
7. You have the following BGP configuration from a Cisco IOS-XR router:

From this BGP configuration, retrieve all of BGP peer IP addresses and their corresponding remote-as.
Return a list of tuples. The tuples should be (neighbor_ip, remote_as). Print your data-structure to standard output.

Your output should look similar to the following. Use ciscoconfparse to accomplish this.
BGP Peers: 
[('10.220.88.20', '42'), ('10.220.88.32', '43')]
"""
configuration = """
router bgp 44
 bgp router-id 10.220.88.38
 address-family ipv4 unicast
 !
 neighbor 10.220.88.20
  remote-as 42
  description pynet-rtr1
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out
  !
 !
 neighbor 10.220.88.32
  remote-as 43
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out"""

from ciscoconfparse import CiscoConfParse

# Make running config string into a list so we can feed it into CiscoConfParse object
cisco_obj = CiscoConfParse(configuration.splitlines())
# Looks for lines in config which start with 'router' at beginning of line and white with whitespace then 'neighbor'
match = cisco_obj.find_objects_w_child(parentspec=r'^router', childspec=r'^\s+neighbor')
# We only have one match so get rid of the list by resetting variable to element 0
match = match[0]
# Search the children of each match for one that starts with whitespace then 'neighbor'
neighbor = match.re_search_children(r'^\s+neighbor')
# Initialise empty list where tuples will be added to in the end
my_list = []
# For final formatting
print('BGP Peers: ')

# Loop through list of matches and extract the neighbor IP address only
for line in neighbor:
    bgp_neighbour = line.text.split()[1] # We want text only, split this to get 2nd element only
    # Search children of each match for one that starts with whitespace then 'remote-as'
    as_no = line.re_search_children(r'^\s+remote-as')
    # Loop through list of children and extract neighbor AS no only
    for asn in as_no:
        as_number = asn.text.split()[1] # We want text only, split this to get 2nd element only
        # Create a tuple with the extracted bgp neighbour ip and it's as no
        my_tuple = (bgp_neighbour, as_number)
        # append these to a new list
        my_list.append((my_tuple))
# Print final list
print(my_list)
