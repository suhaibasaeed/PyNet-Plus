"""
1a. Create a Python file named "my_devices.py" that defines the NAPALM connection information
for both the 'cisco3' device and the 'arista1' device. Use getpass() for the password handling.

This Python module will store the device connection info for all of the exercises in this lesson
"""

from getpass import getpass

password = getpass()

cisco3 = dict(
    hostname='cisco3.lasthop.io',
    device_type='ios',
    username='pyclass',
    password=password,
    optional_args={},
)

arista1 = dict(
    hostname="arista1.lasthop.io",
    device_type="eos",
    username="pyclass",
    password=password,
)

nxos1 = dict(
    hostname='nxos1.lasthop.io',
    device_type='nxos',
    username='pyclass',
    password=password,
    optional_args={'port': 8443},
)
