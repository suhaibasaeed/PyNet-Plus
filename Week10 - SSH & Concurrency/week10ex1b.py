"""
1b. Create a Python script that executes "show version" on each of the network devices defined in my_devices.py.
It should execute serially i.e. one SSH connection after the other. Record the total execution time for the script.
Print the "show version" output and the total execution time to standard output.

Create a function that establishes a Netmiko connection & executes a single show command that you pass in as argument.
This function's arguments should be the Netmiko device dictionary and the "show-command" argument.
The function should return the result from the show command.
"""

from datetime import datetime
from netmiko import ConnectHandler
from my_devices import device_list # Import list of devices

def ssh_con(device, show_command):
    """
    Connect to the device via Netmiko and execute show version command
    :param device: Netmiko device dictionary
    :param show_command: Show command to send to the device
    :return: Output of the command from the device
    """
    # Connect to the device and pull in details via **kwargs
    net_connect = ConnectHandler(**device)
    # If the 2nd parameter passed to the function is show version
    if show_command == 'show version':
        # Send the command to the device
        output = net_connect.send_command_timing("show version")
        # Gracefully disconnect from the device
        net_connect.disconnect()

        # Print the output
        print('-' * 80)
        print(output)
        print('-' * 80)

if __name__ == '__main__':
    # Record start time
    start_time = datetime.now()
    
    # Loop through the devices
    for device in device_list:
        # Call ssh_con and pass in device details and the show command we want to send to it
        ssh_con(device, 'show version')
    
    # Record end time and prind
    end_time = datetime.now()
    print('Total time taken for execution is: {}'.format(end_time - start_time))
