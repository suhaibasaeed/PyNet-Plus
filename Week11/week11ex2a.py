"""
2a. Using requests library, perform HTTP GET on the base URL of the NetBox server (https://netbox.lasthop.io/api/).
Ensure that you are not verifying the SSL certificate.

Print the HTTP status code, the response text, the JSON response, and the HTTP response headers.
These items can be accessed using the following attributes/methods in the Python-requests Response object:

response.status_code
response.text
response.json()
response.headers
"""

import requests # Used to interface with REST APIs
from pprint import pprint
from urllib3.exceptions import InsecureRequestWarning

# Remote SSL cert warning as we're using device with unsigned cert
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

if __name__ == '__main__':

    # Specify the URL
    url = "https://netbox.lasthop.io/api/"

    # Use the HTTP-GET operation - pass in URL & don't check SSL cert
    response = requests.get(url, verify=False)

    # Print the HTTP status code
    print('The HTTP status code is: {}'.format(response.status_code))
    # Print the response text
    print('The response text is: {}'.format(response.text))

    # Print the JSON response
    print('-' * 80)
    pprint('The JSON response is: {} '.format(response.json()))
    print('-' * 80)

    # Print the HTTP response headers
    pprint('The HTTP response headers are: {}'.format(response.headers))

