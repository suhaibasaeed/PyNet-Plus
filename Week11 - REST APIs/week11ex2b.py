"""
2b. Repeat exercise 2a, except properly construct the HTTP request headers as follows:

http_headers = {}
http_headers["accept"] = "application/json; version=2.4;"

You will need to pass these HTTP headers into your HTTP GET request.
Once again print the HTTP status code, the response text, the JSON response, and the HTTP response headers.

"""

import requests # Used to interface with REST APIs
from pprint import pprint
from urllib3.exceptions import InsecureRequestWarning

# Remove SSL cert warning as we're using device with unsigned cert
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

if __name__ == '__main__':

    # Specify the URL
    url = "https://netbox.lasthop.io/api/"
    # Specify the HTTP headers
    http_headers = {}
    http_headers["accept"] = "application/json; version=2.4;"

    # Use the HTTP-GET operation - pass in URL, HTTP headers & don't check SSL cert
    response = requests.get(url, headers=http_headers, verify=False)

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

