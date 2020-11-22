"""
2. Create a new file named my_functions.py. Move your function from exercise1 to this file.
Name this function "ssh_command". Reuse functions from this file for the rest of the exercises.

Complete the same task as Exercise 1b except this time use "legacy" threads to create a solution.
Launch a separate thread for each device's SSH connection. Print time required to complete the task for all devices
Move all of the device specific output printing to the called function (i.e. to the child thread).
"""

from datetime import datetime # Keep track of execution time
from my_devices import device_list # Import list of devices
from my_functions import ssh_command # Import ssh_command function
import threading

def main():
    """
    Use threading and Netmiko to connect to each of the devices in legacy way. Execute 'show version' on each device
    Lastly, record the total amount of time required to do this.
    """
    # Record start time
    start_time = datetime.now()
    
    for device in device_list:  # Loop through 9 devices in device_list
        # call Thread class to create Thread-2 in process which is passed in ssh_command function and device
        my_thread = threading.Thread(target=ssh_command, args=(device, 'show version'))  # i.e. Thread-2 executes         show ver command
        # Start executing the thread
        my_thread.start()
        # Get main thread - Thread-1 in our example
    main_thread = threading.currentThread()
    # Go through all outstanding threads
    for some_thread in threading.enumerate():
        # Skip main thread as it will never be complete as it's the thread that is executing all this
        if some_thread != main_thread:
            print(some_thread)
            # Join makes program wait here until the thread is complete - Basically until all threads are done
            some_thread.join()
            
    # Record end time and prind
    end_time = datetime.now()
    print('Total time taken for execution is: {}'.format(end_time - start_time))


if __name__ == '__main__':
   main()
   
