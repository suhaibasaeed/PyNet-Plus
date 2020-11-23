"""
3b. Using the same device information retrieved in exercise 3a, create and print a report to standard output.
This report should contain the location, manufacturer, and status for each device.
Your output should look similar to the following:

------------------------------------------------------------
arista1
----------
Location: Fremont Data Center
Vendor: Arista
Status: Active
------------------------------------------------------------


------------------------------------------------------------
arista2
----------
Location: Fremont Data Center
Vendor: Arista
Status: Active
------------------------------------------------------------

...   # remaining devices

"""
import os
import requests # Used to interface with REST APIs
from pprint import pprint
from urllib3.exceptions import InsecureRequestWarning

# Remove SSL cert warning as we're using device with unsigned cert
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

if __name__ == '__main__':

    # Set the token based on the NETBOX_TOKEN environment variable
    token = os.environ["NETBOX_TOKEN"]

    # Specify the URL
    url = "https://netbox.lasthop.io/api/dcim/devices/"
    # Specify the HTTP headers
    http_headers = {}
    http_headers["accept"] = "application/json; version=2.4;"
    # For the Authentication
    http_headers["Authorization"] = f"Token {token}"

    # Use the HTTP-GET operation - pass in URL, HTTP headers & don't check SSL cert
    response = requests.get(url, headers=http_headers, verify=False)
    # Get JSON payload from the response and convert into python data structure
    response = response.json()

    # Get list of dictionaries with device details in them
    devices = response['results']
    # Loop through list of dictionaries and return the relevant key
    for device in devices:
        display_name = device['display_name']
        device_location = device['site']['name']
        device_vendor = device['device_type']['manufacturer']['name']
        device_status = device['status']['label']

        # Print the report for each device
        print('-' * 40)
        print(display_name)
        print('-' * 10)
        print("Location: {}".format(device_location))
        print("Vendor: {}".format(device_vendor))
        print("Status: {}".format(device_status))
        print('-' * 40)
        
