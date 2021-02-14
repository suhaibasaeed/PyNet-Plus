"""
1. Using the below ARP data, create a five element list.
Each list element should be a dictionary with the following keys: "mac_addr", "ip_addr", "interface".
At the end of this process, you should have five dictionaries contained inside a single list.
Protocol  Address      Age  Hardware Addr   Type  Interface
Internet  10.220.88.1   67  0062.ec29.70fe  ARPA  Gi0/0/0
Internet  10.220.88.20  29  c89c.1dea.0eb6  ARPA  Gi0/0/0
Internet  10.220.88.22   -  a093.5141.b780  ARPA  Gi0/0/0
Internet  10.220.88.37 104  0001.00ff.0001  ARPA  Gi0/0/0
Internet  10.220.88.38 161  0002.00ff.0001  ARPA  Gi0/0/0
"""

from pprint import pprint
arp_data = """
Protocol  Address      Age  Hardware Addr   Type  Interface
Internet  10.220.88.1   67  0062.ec29.70fe  ARPA  Gi0/0/0
Internet  10.220.88.20  29  c89c.1dea.0eb6  ARPA  Gi0/0/0
Internet  10.220.88.22   -  a093.5141.b780  ARPA  Gi0/0/0
Internet  10.220.88.37 104  0001.00ff.0001  ARPA  Gi0/0/0
Internet  10.220.88.38 161  0002.00ff.0001  ARPA  Gi0/0/0"""

# Convert string into list, one element per line
arp_data = arp_data.splitlines()
# Remove first 2 elements which are empty string and column headers
arp_data.pop(0)
arp_data.pop(0)

# Counter for list index we're splitting via whitespace 
x = 0
# initialise empty list
final_list = []

# Loop through arp_data list, split each line again and extract mac, ip and interface
for line in arp_data:
    new_list = arp_data[x].split()  # Split each line of output by whitespace
    mac = new_list[3]  # 4th element is mac address
    ip = new_list[1]  # 2nd element is ip
    intf = new_list[5]  # 6th element is intrface
    x += 1 # increment counter
    
    # Create dictionary with new info extracted from arp_data list
    new_dict = {'mac_addr': mac,
                'ip_addr': ip,
                'interface': intf
    }
    # Add the newly created dictionary to the list
    final_list.append(new_dict)
# Print new list to console
pprint(final_list)
