from getpass import getpass
import yaml

def function1(filename):
    # Open yaml file with device details and read it into output variable
    with open(filename) as f:
        output = yaml.safe_load(f)

    password = getpass()
    # Remove outer dictionary
    device_dict = output['arista4']
    # Make password in device dictionary equal to getpass()
    device_dict['password'] = password
    
    return device_dict

def function2(output):
    # Get rid of outer list
    output = output[0]
    # We only want dictionary value with arp entries in it
    output = output['ipV4Neighbors']

    # Loop through entries in arp table dictionary and print out mapping of IPs to MACs
    for entry in output:
        ip_addr = entry['address']
        mac_addr = entry['hwAddress']
        print('{} --> {}'.format(ip_addr, mac_addr))

