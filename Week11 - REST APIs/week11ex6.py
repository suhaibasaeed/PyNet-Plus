"""
6. Use an HTTP DELETE and Python-requests to delete the IP address object that you just created.

Remember to reference the ID of your object.

"""
import os
import requests # Used to interface with REST APIs
from urllib3.exceptions import InsecureRequestWarning

# Remove SSL cert warning as we're using device with unsigned cert
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

if __name__ == '__main__':

    # Set the token based on the NETBOX_TOKEN environment variable
    token = os.environ["NETBOX_TOKEN"]

    # Specify the URL of the object we're deleting
    url = "https://netbox.lasthop.io/api/ipam/ip-addresses/236/"
    # Specify the HTTP headers
    http_headers = {}
    http_headers["Content-Type"] = "application/json; version=2.4;"
    # For the Authentication
    http_headers["Authorization"] = f"Token {token}"

    # Use the HTTP-DELETE operation to delete the object - pass in URL, HTTP headers & don't check SSL cert
    response = requests.delete(url, headers=http_headers, verify=False)

    # If we get a 200-OK message back then print success
    if response.ok:
        print("IP address deleted successfully")
        
