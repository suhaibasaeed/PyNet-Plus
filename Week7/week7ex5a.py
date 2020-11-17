"""
5a. Load the show_version.xml file (originally from a Cisco NX-OS device) using the etree.fromstring() method.

Note this XML document, unlike the previous documents, contains the document encoding information.
Because the document encoding is at the top of the file, you need to read the file using "rb" mode ("b" for binary mode)

Print out the the namespace map of this XML object.
You can accomplish this by using the .nsmap attribute of your XML object.

"""

from lxml import etree

# Open and read the file in using binary mode & parse it using fromstring method
with open("show_version.xml", "rb") as f:
    my_xml = etree.fromstring(f.read())
# Use nsmap attribute of MCL objecy to print namespace map
print(my_xml.nsmap)

