"""
4b. Using the response data from POST that created the IP add entry in ex4a, capture "id" of newly created IP add object

Using this ID, construct a new URL.
Use this new URL and the HTTP GET method to retrieve only the API information specific to this IP address.

Your IP address URL should be of the following form:

https://netbox.lasthop.io/api/ipam/ip-addresses/{address_id}/

where {address_id} is the ID of the object that you just created.

Pprint the response.json() data from this HTTP GET. Please note the ID of the address object that you just created.

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
    url = "https://netbox.lasthop.io/api/ipam/ip-addresses/236/"
    # Specify the HTTP headers
    http_headers = {}
    http_headers["accept"] = "application/json; version=2.4;"
    # For the Authentication
    http_headers["Authorization"] = f"Token {token}"

    # Use the HTTP-GET operation - pass in URL, HTTP headers & don't check SSL cert
    response = requests.get(url, headers=http_headers, verify=False)
    # Print the status code of the operation
    print("The status code is: {}".format(response.status_code))
    # Get JSON payload from the response and convert into python data structure then print
    response = response.json()
    pprint(response)

