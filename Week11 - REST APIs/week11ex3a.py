"""
3a. Retrieve a list of all the devices in NetBox. This will require authentication.
As in the previous task, create your headers manually and pass them into your request.
In order to perform the NetBox authentication, you should do the following:

import os
# Set the token based on the NETBOX_TOKEN environment variable
token = os.environ["NETBOX_TOKEN"]

Then add the following key to your HTTP Headers:

http_headers["Authorization"] = f"Token {token}"

From this returned data structure (the NetBox "/api/dcim/devices/"), print out all of the device "display_names".
Note, the response.json() will contain a "results" key. This "results" key will refer to a list of dictionaries.
These dictionaries will contain information about each one of the devices in NetBox.

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
    # Loop through list of dictionaries and return the display_name key
    for device in devices:
        print(device['display_name'])
