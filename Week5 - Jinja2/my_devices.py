from getpass import getpass

password = getpass()

nxos1 = {
    'host': 'nxos1.lasthop.io',
    'username': 'pyclass',
    'password': password,
    'device_type': 'cisco_nxos',
}

nxos2 = {
    'host': 'nxos2.lasthop.io',
    'username': 'pyclass',
    'password': password,
    'device_type': 'cisco_nxos',
}
