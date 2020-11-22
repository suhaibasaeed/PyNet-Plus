from netmiko import ConnectHandler

def ssh_command(device, show_command):
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
        output = net_connect.send_command("show version")
        # Gracefully disconnect from the device
        net_connect.disconnect()

        # Print the output
        print('-' * 80)
        print(output)
        print('-' * 80)

def ssh_command2(device, show_command):
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
        output = net_connect.send_command("show version")
        
        return output

def ssh_command3(device):
    """
    Connect to the device via Netmiko and execute show ip arp command
    :param device: Netmiko device dictionary
    :return: Output of the command from the device
    """
    # Connect to the device and pull in details via **kwargs
    net_connect = ConnectHandler(**device)
    # If the device is the srx
    if net_connect.device_type == 'juniper_junos':
        # Send the different command to the device
        output = net_connect.send_command("show arp")
        
        return output
                                        
    else:
        output = net_connect.send_command("show ip arp")

        return output
