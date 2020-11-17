"""
4a. Use the find() method to retrieve the first "zones-security" element.
Print out the tag of this element and of all its children elements. Your output should be similar to the following:

Find tag of the first zones-security element
--------------------
zones-security

Find tag of all child elements of the first zones-security element
--------------------
zones-security-zonename
zones-security-send-reset
zones-security-policy-configurable
zones-security-interfaces-bound
zones-security-interfaces

4b. Use the find() method to find the first "zones-security-zonename".
Print out the zone name for that element (the "text" of that element).

4c. Use the findall() method to find all occurrences of "zones-security".
For each of these security zones, print out the security zone name ("zones-security-zonename", the text of that element)

"""

from lxml import etree

# Exercise 4a
# Open and read in file + parse it using fromstring method
with open("show_security_zones.xml") as f:
    my_xml = etree.fromstring(f.read())

# Use find method and shorthand XPATH notation to find first zones-security element
trust_zone = my_xml.find(".//zones-security")

print('Find tag of the first zones-security element')
print('-' * 30)
print(trust_zone.tag) # Print tag of zones-security element
print()

print("Find tag of all child elements of the first zones-security element")
print('-' * 30)
# Loop through children and print out tag of each child
for child in trust_zone.getchildren():
    print(child.tag)

# Exercise 4b
print('-' * 30)
print('Exercise 4b')
print('-' * 30)
# Find the first occurrence of the below and print out it's name
print(my_xml.find(".//zones-security-zonename").text)

# Exercise 4c
print('-' * 30)
print('Exercise 4c')
print('-' * 30)
# Find all occurrences of zones-security
all_zones_security = my_xml.findall(".//zones-security")
# Loop through each occurrence finding the name and print it out
for zone in all_zones_security:
    print(zone.find(".//zones-security-zonename").text)





