"""7. Using your TextFSM template and the 'show interface status' data from exercise2, create a Python program that uses TextFSM to parse this data. In this Python program, read the show interface status data from a file and process it using the TextFSM template. From this parsed-output, create a list of dictionaries. The program output should look as follows:
$ python ex7_show_int_status.py 

[{'DUPLEX': 'auto',
  'PORT_NAME': 'Gi0/1/0',
  'PORT_TYPE': '10/100/1000BaseTX',
  'SPEED': 'auto',
  'STATUS': 'notconnect',
  'VLAN': '1'},
 {'DUPLEX': 'auto',
  'PORT_NAME': 'Gi0/1/1',
  'PORT_TYPE': '10/100/1000BaseTX',
  'SPEED': 'auto',
  'STATUS': 'notconnect',
  'VLAN': '1'},
 {'DUPLEX': 'auto',
  'PORT_NAME': 'Gi0/1/2',
  'PORT_TYPE': '10/100/1000BaseTX',
  'SPEED': 'auto',
  'STATUS': 'notconnect',
  'VLAN': '1'},
 {'DUPLEX': 'auto',
  'PORT_NAME': 'Gi0/1/3',
  'PORT_TYPE': '10/100/1000BaseTX',
  'SPEED': 'auto',
  'STATUS': 'notconnect',
  'VLAN': '1'}]
"""
from pprint import pprint
import textfsm

# Put file inside variable
template_file = "ex2_show_int_status.template"
# Open the template file
template = open(template_file)

# Open the txt file with device output and read it in
with open("ex1_show_int_status.txt") as f:
    raw_text_data = f.read()

# Process template using TextFSM class passing in template file handle
re_table = textfsm.TextFSM(template)
# Parse text using ParseText method passing in device input as string
data = re_table.ParseText(raw_text_data)
# Get header row which will be used for dictionary creation
header = re_table.header
# Close the template
template.close

# Initialise empty dictionary and list
new_dict = {}
new_list = []
# Loop through list with inner lists of parse data, set key as corresponding header and value as actual info
for inner_list in data:
    new_dict = {
        header[3]: inner_list[3],    
        header[0]: inner_list[0],
        header[5]: inner_list[5],
        header[4]: inner_list[4],
        header[1]: inner_list[1],
        header[2]: inner_list[2],   
}
    # Append dictionaries to new list
    new_list.append(new_dict)
# Print to console
pprint(new_list)

