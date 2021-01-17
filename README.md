# PyNet-Plus
Advanced Python for Network Engineers course exercises

## Week 1 - Git + Netmiko Part 1

Netmiko

**1. In the lab environment use Netmiko to connect to one of the Cisco NX-OS devices. You can find the IP addresses and username/passwords of the Cisco devices in the 'Lab Environment' email or alternatively in the ~/.netmiko.yml file. Simply print the router prompt back from this device to verify you are connecting to the device properly.**

**2. Add a second NX-OS device to your first exercise. Make sure you are using dictionaries to represent the two NX-OS devices. Additionally, use a for-loop to accomplish the Netmiko connection creation. Once again print the prompt back from the devices that you connected to.**

**3. For one of the Cisco IOS devices, use Netmiko and the send_command() method to retrieve 'show version'. Save this output to a file in the current working directory.**  

## Week 2 - Netmiko Part 2
1. Use the extended 'ping' command and Netmiko on the 'cisco4' router. This should prompt you for additional information as follows:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cisco4#ping  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Protocol [ip]:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Target IP address: 8.8.8.8  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Repeat count [5]:   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Datagram size [100]:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Timeout in seconds [2]:   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Extended commands [n]:   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sweep range of sizes [n]:   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Type escape sequence to abort.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sending 5, 100-byte ICMP Echos to 8.8.8.8, timeout is 2 seconds:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;!!!!!  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/4 ms  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;a. Use send_command_timing() to handle the additional prompting from this 'ping' command. Specify a target IP address of '8.8.8.8'

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;b. Use send_command() and the expect_string argument to handle the additional prompting. Once again specify a target IP address of '8.8.8.8'.


**2. Create a Netmiko connection to the 'nxos2' device using a global_delay_factor of 2. Execute 'show lldp neighbors detail' and print the returned output to standard output. Execute 'show lldp neighbors detail' a second time using send_command() with a delay_factor of 8. Print the output of this command to standard output. Use the Python datetime library to record the execution time of both of these commands. Print these execution times to standard output.**


**3. On your AWS lab server, look at the ntc-templates index file (at ~/ntc-templates/templates/index). Look at some of the commands available for cisco_ios (you can use 'cat ~/ntc-templates/templates/index | grep cisco_ios' to see this). Also look at some of the abbreviated forms of Cisco IOS commands that are supported in the index file.**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Create a script using Netmiko that executes 'show version' and 'show lldp neighbors' against the Cisco4 device with use_textfsm=True.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;What is the outermost data structure that is returned from 'show lldp neighbors' (dictionary, list, string, something else)? The Cisco4 device should only have one LLDP entry (the HPE switch that this router connects to). From this LLDP data, print out the remote device's interface. In other words, print out the port number on the HPE switch that Cisco4 connects into.


**4. Use Netmiko and the send_config_set() method to configure the following on the Cisco3 router.**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip name-server 1.1.1.1  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip name-server 1.0.0.1  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip domain-lookup  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Experiment with fast_cli=True to see how long the script takes to execute (with and without this option enabled).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Verify DNS lookups on the router are now working by executing 'ping google.com'. Verify from this that you receive a ping response back.


**5. On both the NXOS1 and NXOS2 switches configure five VLANs including VLAN names (just pick 5 VLAN numbers between 100 - 999). Use Netmiko's send_config_from_file() method to accomplish this. Also use Netmiko's save_config() method to save the changes to the startup-config.**  


**6. Using SSH and netmiko connect to the Cisco4 router. In your device definition, specify both an 'secret' and a 'session_log'. Your device definition should look as follows:**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;password = getpass()  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;device = {  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    "host": "cisco4.lasthop.io",  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    "username": "pyclass",  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    "password": password,  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    "secret": password,  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    "device_type": "cisco_ios",  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    "session_log": "my_output.txt",  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Execute the following sequence of events using Netmiko:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;a. Print the current prompt using find_prompt()

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;b. Execute the config_mode() method and print the new prompt using find_prompt()

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;c. Execute the exit_config_mode() method and print the new prompt using find_prompt()

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;d. Use the write_channel() method to send the 'disable' command down the SSH channel. Note, write_channel is a low level method so it requires that you add a newline to the end of your 'disable' command.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;e. time.sleep for two seconds and then use the read_channel() method to read the data that is currently available on the SSH channel. Print this to the screen.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;f. Execute the enable() method and print your now current prompt using find_prompt(). The enable() method will use the 'secret' defined in your device definition. This 'secret' is the same as the standard lab password.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;g. After you are done executing your script, look at the 'my_output.txt' file to see what is included in the session_log.  

## Week 3 - Complex Data Structures - YAML, JSON & CiscoConfParse

## Week 4 - Libraries & TextFSM

## Week 5 - Jinja2

## Week 6 - Arista eAPI

## Week 7 - XML & Cisco NX-API

## Week 8 - NETCONF & Juniper PyEz

## Week 9 - NAPALM

## Week 10 - SSH & Concurrency

## Week 11 - REST APIs

## Week 12 - Tools, Testing & CI-CD
