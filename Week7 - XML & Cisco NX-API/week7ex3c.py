"""
3c. Optional - create a second function that uses xmltodict to read and parse a filename that you pass in.
This function should support a "force_list" argument that is passed to xmltodict.parse().
force_list argument of xmltodict takes a dictionary where dictionary key-name is XML element that is required to be list

For example:
force_list={"zones-security": True}

Use this new function to parse the "show_security_zones_single_trust.xml".
Verify the Python data type is now a list for the ['zones-information']['zones-security'] element.
"""

import xmltodict


def parse_file_list(filename, force_list='False'):
    '''Opens XML file, parses it and returns the XML as OrderedDict.

    Values are the name of a file and True or False'''
    # Open and read in XML file
    with open(filename) as f:
        output = f.read()
    # If force_list parameter passed in function argument is True i.e. We want XML element to be list
    if force_list == 'True':
        # Call parse method on xmltodict class & pass in input from file with force_list True on zones-security element
        my_xml = xmltodict.parse(output, force_list={"zones-security": True})
        return my_xml
    else:
        # Call parse method on xmltodict class and pass in input from file
        my_xml = xmltodict.parse(output)
        return my_xml

# Call function twice once with force_list being True then False
ord_dict = parse_file_list("show_security_zones_trust.xml", 'False')
ord_dict = parse_file_list("show_security_zones_trust.xml", 'True')

# Verify list was returned by printing the type
print(type(ord_dict['zones-information']['zones-security']))
