"""
4a. Using an HTTP POST and the Python-requests library, create a new IP address in NetBox.
This IP address object should be a /32 from the 192.0.2.0/24 documentation block.
Print out the status code and the returned JSON.

The HTTP headers for this request should look as follows:

http_headers = {}
http_headers["Content-Type"] = "application/json; version=2.4;"
http_headers["accept"] = "application/json; version=2.4;"
http_headers["Authorization"] = f"Token {token}"

The URL for the HTTP POST is:

https://netbox.lasthop.io/api/ipam/ip-addresses/

The JSON payload data for this request should be similar to the following:

data = {"address": "192.0.2.100/32"}

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
    url = "https://netbox.lasthop.io/api/ipam/ip-addresses/"
    # Specify the HTTP headers
    http_headers = {}
    http_headers["accept"] = "application/json; version=2.4;"
    http_headers['Content-Type'] = "application/json; version=2.4;"
    # For the Authentication
    http_headers["Authorization"] = f"Token {token}"
    
    # Data regarding the object we're creating
    post_data = {"address": "192.0.2.200/32"}
    
    # Use the HTTP-POST operation - pass in URL, HTTP headers, JSON data from variable & don't check SSL cert
    response = requests.post(url, headers=http_headers, data=dumps(post_data), verify=False)
    # Print the status code of the operation
    print("The response code is: {}".format(response.status_code))
    # Get JSON payload from the response and convert into python data structure then print
    response = response.json()
    pprint(response)
    
