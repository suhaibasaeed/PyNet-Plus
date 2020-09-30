from netmiko import ConnectHandler, file_transfer
from getpass import getpass()

nxos1 = {
    "device_type": "cisco_nxos",
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
}

source_file = "test3.txt"
dest_file = "test3.txt"
direction = "put"
file_system = "bootflash:"

# Create the Netmiko SSH connection
ssh_conn = ConnectHandler(**nxos1)
transfer_dict = file_transfer(
    ssh_conn,
    source_file=source_file,
    dest_file=dest_file,
    file_system=file_system,
    direction=direction,
    overwrite_file=True,
)
print(transfer_dict)
