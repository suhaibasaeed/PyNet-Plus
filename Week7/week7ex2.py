"""
2a. Using xmltodict, load the show_security_zones.xml file as a Python dictionary.
Print out this new variable and its type. Newly created object is an OrderedDict; not a traditional dictionary.

2b. Print the names and an index number of each security zone in the XML data from Exercise 2a.
Your output should look similar to the following (tip, enumerate will probably help):
Security Zone #1: trust
Security Zone #2: untrust
Security Zone #3: junos-host
"""

import xmltodict
from pprint import pprint

# Exercise 2a
# Open and read in XML file
with open("show_security_zones.xml") as f:
    output = f.read()
# Call parse method on xmltodict class and pass in input from file
my_xml = xmltodict.parse(output)
# Print variable name and type
pprint(my_xml)
print(type(my_xml))
print('-' * 30)

# Exercise 2b

x = 1 # Initialise x to 1 which will count our security zone numbers through loop
for k, v in my_xml.items(): # Loop through outer ordered dict
    for key, value in v.items(): # Loop through inner ordered dict
        for ord_dict in value: # Loop through list to get to inner most ordered dict
            security_zone = ord_dict['zones-security-zonename'] # Extract value from ordered dict with zone name
            print("Security Zone #{}: {}".format(x, security_zone)) # Print Security zone number and name
            x += 1

