"""
5. Using a context manager and a 'ProcessPoolExecutor', complete the same task as Exercise 4.
"""

from datetime import datetime # Keep track of execution time
from my_devices import device_list # Import list of devices
from my_functions import ssh_command2 # Import ssh_command function
from concurrent.futures import ProcessPoolExecutor, as_completed

def main():
    """
    Use multiple processes and Netmiko to connect to each device using concurrent futures.
    Execute 'show version' on each device.
    Lastly, record the total amount of time required to do this.
    """
    # Record start time
    start_time = datetime.now()

    # MAx of 4 child processes - 5 inc the parent
    max_threads = 4
    # Use context manager to create instance of ProcessPoolExecutor object and pass in max_thread no
    with ProcessPoolExecutor(max_threads) as pool:

        future_list = []

        # Loop through the 4 devices
        for device in device_list:
            # Start 4 child processes and submit them into the process pool
            future = pool.submit(ssh_command2, device, 'show version') # Pass in ssh_command2, device and command args
            # Append each process to the list
            future_list.append(future)
    
        # Instead of waiting for all pending processes to finish - process them as they come in
        for future in as_completed(future_list): # Pass in list created above into as_completed function
            # Print result
            print("Result" + future.result())
    
        # Record end time and print
        end_time = datetime.now()
        print('Total time taken for execution is: {}'.format(end_time - start_time))


if __name__ == '__main__':
   main()

