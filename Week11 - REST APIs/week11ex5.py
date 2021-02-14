"""
5. Building on the script from exercise 4, add a description to the the IP address object that you just created.

Accomplish this using an HTTP PUT.
The HTTP PUT operation will require all of the mandatory fields in the object (in this case, the "address" field).

Print the status code and the response.json() from your PUT operation.
The HTTP PUT operation will use same URL as exercise 4b (i.e. URL of the new IP address object including its ID).

"""
import os
import requests # Used to interface with REST APIs
from pprint import pprint
from json import dumps
from urllib3.exceptions import InsecureRequestWarning

# Remove SSL cert warning as we're using device with unsigned cert
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

if __name__ == '__main__':

    # Set the token based on the NETBOX_TOKEN environment variable
    token = os.environ["NETBOX_TOKEN"]

    # Specify the URL
    url = "https://netbox.lasthop.io/api/ipam/ip-addresses/236/"
    # Specify the HTTP headers
    http_headers = {}
    http_headers["Content-Type"] = "application/json; version=2.4;"
    # For the Authentication
    http_headers["Authorization"] = f"Token {token}"
    
    # Information we are passing to the device - including the address which is a mandatory field in the object
    put_data = {
        'address': '192.0.2.200/32',
        'description': 'This is a test description',
    }

    # Use the HTTP-PUT operation - pass in URL, HTTP headers, JSON data from variable& don't check SSL cert
    response = requests.put(url, headers=http_headers, data=dumps(put_data), verify=False)
    
    # Print the status code of the operation
    print("The status code is: {}".format(response.status_code))
    # Get JSON payload from the response and convert into python data structure then print
    response = response.json()
    pprint(response)

