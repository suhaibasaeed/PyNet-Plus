"""
5b. Similar to earlier exercises, use the find() method to access text of the "proc_board_id" element (serial number).
As this XML object contains namespace data, you will need to use the {*} namespace wildcard in the find() method.
Your find call should look as follows:

find(".//{*}proc_board_id")

The {*} is a namespace wildcard and says to match ALL namespaces.
"""

from lxml import etree

# Call parse method on etree and pass in XML file
my_xml = etree.parse('show_version.xml')
# Use find method to access text of the proc_board_id element
serial_no = my_xml.find(".//{*}proc_board_id").text
# Print to console
print('The serial number of the device is: {}'.format(serial_no))

