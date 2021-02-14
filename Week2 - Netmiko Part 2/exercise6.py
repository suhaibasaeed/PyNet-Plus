"""Using SSH and netmiko connect to the Cisco4 router. In your device definition, specify both an 'secret' and a 'session_log'.
Your device definition should look as follows:
device = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": "",
    "secret": "",
    "device_type": "cisco_ios",
    "session_log": "my_output.txt",
}
Execute the following sequence of events using Netmiko:
a. Print the current prompt using find_prompt()

b. Execute the config_mode() method and print the new prompt using find_prompt()

c. Execute the exit_config_mode() method and print the new prompt using find_prompt()

d. Use the write_channel() method to send the 'disable' command down the SSH channel.
Note, write_channel is a low level method so it requires that you add a newline to the end of your 'disable' command.

e. time.sleep for two seconds and then use the read_channel() method to read the data that is currently available on the SSH channel.
Print this to the screen.

f. Execute the enable() method and print your now current prompt using find_prompt().
The enable() method will use the 'secret' defined in your device definition. This 'secret' is the same as the standard lab password.

g. After you are done executing your script, look at the 'my_output.txt' file to see what is included in the session_log.
"""

from netmiko import Netmiko
import time
from getpass import getpass

password = getpass()

device = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
    "secret": password,
    "device_type": "cisco_ios",
    "session_log": "my_output.txt",
}

# Establish SSH connection to the network device using **kwargs to pull in details from dictionary
net_connect = Netmiko(**device)

# Part a - find and print the prompt to the screen
print(net_connect.find_prompt())

# Part B - Enter config mode and find the prompt
print(net_connect.config_mode())
print(net_connect.find_prompt())

# Part C - exit config mode and print the prompt
print(net_connect.exit_config_mode())
print(net_connect.find_prompt())

# Part D - send disable down the SSH channel
print(net_connect.write_channel('disable\n'))

# Part E - Sleep for 2s and read back from SSH channel
time.sleep(2)
print(net_connect.read_channel())

# Part F - Go into enable mode and print prompt
print(net_connect.enable())
print(net_connect.find_prompt())

net_connect.disconnect()







