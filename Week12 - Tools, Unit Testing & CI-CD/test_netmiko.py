from getpass import getpass
from netmiko import ConnectHandler

# Create Netmiko connection
def netmiko_conn():
    net_connect = ConnectHandler(
        host="arista1.lasthop.io",
        device_type="arista_eos",
        username='pyclass',
        password=getpass(),
    )
    # Return Netmiko connection object
    return net_connect

# Test function which will see if function above will return Netmiko object with correct output after find_prompt()
def test_find_prompt():
    net_connect = netmiko_conn()  # Call function created above
    assert "arista1#" in net_connect.find_prompt()

# Test function which will see if the software version of the Netmiko object returned is 4.20.10M
def test_show_version():
    net_connect = netmiko_conn() # Call function created above
    output = net_connect.send_command("show version")  # Send show version command to the device
    assert "4.20.10M" in output