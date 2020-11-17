"""
3a. Open the following two XML files: show_security_zones.xml and show_security_zones_single_trust.xml.
Use a generic function that accepts an argument "filename" to open and read a file.
Inside this function, use xmltodict to parse the contents of the file.
Your function should return the xmltodict data structure.
Using this function, create two variables to store the xmltodict data structure from the two files.

3b. Compare the Python "type" of the elements at ['zones-information']['zones-security'].
What is the difference between the two data types? Why?

"""
import xmltodict
from pprint import pprint

# Exercise 3a
def parse_file(filename):
    '''Opens XML file, parses it and returns the XML as OrderedDict.

    Value is the name of a file'''
    # Open and read in XML file
    with open(filename) as f:
        output = f.read()
    # Call parse method on xmltodict class and pass in input from file
    my_xml = xmltodict.parse(output)
    return my_xml

# call function twice to return both files and put in new variable
ord_dict1 = parse_file("show_security_zones.xml")
ord_dict2 = parse_file("show_security_zones_trust.xml")

# Exercise3b
# Print type of the inner data structures
print(type(ord_dict1['zones-information']['zones-security'])) # List
print(type(ord_dict2['zones-information']['zones-security'])) # Ordered Dict


