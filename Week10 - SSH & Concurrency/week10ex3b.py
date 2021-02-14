"""
3b. Instead of waiting for all futures to complete, use "as_completed" to print future results as they come available.

Reuse your "ssh_command2" function to accomplish this.

Once again use the concurrent futures "ThreadPoolExecutor" and print the "show version" results to standard output.
Additionally, print the total execution time to standard output.
"""

from datetime import datetime # Keep track of execution time
from my_devices import device_list # Import list of devices
from my_functions import ssh_command2 # Import ssh_command function
from concurrent.futures import ThreadPoolExecutor, as_completed

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
        future = pool.submit(ssh_command2, device, 'show version') # Pass in ssh_command2, device and command args
        # Append each thread to the list
        future_list.append(future)

    # Instead of waiting for all pending threads to finish - process them as they come in
    for future in as_completed(future_list): # Pass in list created above into as_completed function
        # Print result
        print("Result" + future.result())

    # Record end time and print
    end_time = datetime.now()
    print('Total time taken for execution is: {}'.format(end_time - start_time))


if __name__ == '__main__':
   main()

