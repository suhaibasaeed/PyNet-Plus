from getpass import getpass
from netmiko import ConnectHandler
import pytest

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