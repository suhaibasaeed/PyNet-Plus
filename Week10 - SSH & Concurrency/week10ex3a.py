"""
3a. Create a new function that is a duplicate of your "ssh_command" function. Name this function "ssh_command2".
This function should eliminate all printing to standard output and should instead return the show command output.

Note, in general, it is problematic to print in the child thread as you can get into race conditions between threads.
Using the "ThreadPoolExecutor" in Concurrent Futures execute show ver on each of the devices defined in my_devices.py.

Use the 'wait' method to ensure all of the futures have completed.
Concurrent futures should be executing the ssh_command2 function in the child threads.
Print the total execution time required to accomplish this task.
"""

from datetime import datetime # Keep track of execution time
from netmiko import ConnectHandler
from my_devices import device_list # Import list of devices
from my_functions import ssh_command2 # Import ssh_command function
from concurrent.futures import ThreadPoolExecutor, wait

def main():
    """
    Use threading and Netmiko to connect to each device using concurrent futures. Execute 'show version' on each device.
    Lastly, record the total amount of time required to do this.
    """
    # Record start time
    start_time = datetime.now()

    # Specify how big the thread pool is
    max_threads = 4
    # Create instance of ThreadPoolExecutor object and pass in max_thread no
    pool = ThreadPoolExecutor(max_threads)

    future_list = []

    # Loop through the 4 devices
    for device in device_list:
        # Start 4 child threads and submit them into the thread pool
        future = pool.submit(ssh_command2, device, 'show version') # Pass in ssh_command2, device and command
        # Append each thread to the list
        future_list.append(future)

    # Waits until all the pending threads are done - Same thing as join() in legacy way
    wait(future_list)
    # Retrieve the results from child threads and pass back into the main thread
    for future in future_list:
        print("Result" + future.result())

    # Record end time and print
    end_time = datetime.now()
    print('Total time taken for execution is: {}'.format(end_time - start_time))


if __name__ == '__main__':
   main()

