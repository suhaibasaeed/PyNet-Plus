from getpass import getpass
import pytest
from netmiko import ConnectHandler

password = getpass()


# Create Netmiko connection = Define as a fixture
@pytest.fixture(scope="module")
def netmiko_conn(request):  # Argument passed in
    net_connect = ConnectHandler(
        host="arista1.lasthop.io",
        device_type="arista_eos",
        username='pyclass',
        password=password,
    )
    # We want SSH connection gracefully torn down after the test is done
    def fin():
        net_connect.disconnect()

    # Called when the tests are done - pass in fin func which closes SSH connection
    request.addfinalizer(fin)
    # Return Netmiko connection object
    return net_connect

# Test function which will see if function above will return Netmiko object with correct output after find_prompt()
def test_find_prompt(netmiko_conn):  # Pass in ficture as parameter
    assert "arista1#" in netmiko_conn.find_prompt()

# Test function which will see if the software version of the Netmiko object returned is 4.20.10M
def test_show_version(netmiko_conn):
    output = netmiko_conn.send_command("show version")  # Send show version command to the device
    assert "4.20.10M" in output