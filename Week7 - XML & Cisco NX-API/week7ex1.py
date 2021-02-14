"""
1. Reading and accessing an XML file:
1a. Using the show_security_zones.xml file, read the file contents and parse the file using etree.fromstring().
Print out the newly created XML variable and also print out the variable's type. Your output should look similar to the following:

1b. Using your XML variable from exercise 1a, print out the entire XML tree in a readable format
(ensure that the output string is a unicode string).

1c. Print out the root element tag name (this tag should have a value of "zones-information").
Print the number of child elements of the root element (you can retrieve this using the len() function).

1d. Using both direct indices and the getchildren() method, obtain the first child element and print its tag name.

1e. Create a variable named "trust_zone". Assign this variable to be the first "zones-security" element in the XML tree.
Access this newly created variable and print out the text of the "zones-security-zonename" child.

1f. Iterate through all of the child elements of the "trust_zone" variable.
Print out the tag name for each child element.
"""

from lxml import etree

# Open and read in file + parse it using fromstring method
with open("show_security_zones.xml") as f:
    my_xml = etree.fromstring(f.read())

# Exercise 1a - Print XML variable and the type
print('-' * 20)
print("Exercise 1a")
print('-' * 20)
print(my_xml)
print(type(my_xml))

# Exercise 1b
# Print the xml in readable format using tostring method outputting unicode string
print('-' * 20)
print("Exercise 1b")
print('-' * 20)
print(etree.tostring(my_xml).decode())


# Exercise 1c
# Print root element tag name and number of child elements of root element
print('-' * 20)
print("Exercise 1c")
print('-' * 20)
print(my_xml.tag)
print(len(my_xml.getchildren()))


# Exercise 1d
# Use direct indices and getchildren method to get 1st child and print it's tag
print('-' * 20)
print('Exercise 1d')
print('-' * 20)
print(my_xml[0])
# First child is first element in the list returned by getchildren method
first_child = my_xml.getchildren()[0]
print(first_child)


# Exercise 1e
# Assign new trust_zone variable to first zones-security element in tree. Print text of zones-security-zonename child
print('-' * 20)
print('Exercise 1e')
print('-' * 20)
# Use find method and shorthand XPATH notation to find first occurrence of zones-security
trust_zone = my_xml.find(".//zones-security")
# Print text of the first child element which is zones-security-zonename
print(trust_zone[0].text)


# Exercise 1f
# Loop through children of trust_zone variable and print out tag for each child
print('-' * 20)
print('Exercise 1f')
print('-' * 20)
for child in trust_zone:
    print(child.tag)

