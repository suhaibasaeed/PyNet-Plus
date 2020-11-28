# Test function which will see if function above will return Netmiko object with correct output after find_prompt()
def test_find_prompt(netmiko_conn):  # Pass in fixture as parameter
    assert "arista1#" in netmiko_conn.find_prompt()

# Test function which will see if the software version of the Netmiko object returned is 4.20.10M
def test_show_version(netmiko_conn):
    output = netmiko_conn.send_command("show version")  # Send show version command to the device
    assert "4.20.10M" in output