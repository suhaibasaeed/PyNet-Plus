"""
6. Using a context manager, the ProcessPoolExecutor, and the map() method,  executes "show ip arp" on all of the devices
Note, the Juniper device will require "show arp" instead of "show ip arp" so you need to properly account for this.
"""

from datetime import datetime # Keep track of execution time
from my_devices import device_list # Import list of devices
from my_functions import ssh_command3 # Import ssh_command function
from concurrent.futures import ProcessPoolExecutor

def main():
    """
    Use multiple processes and Netmiko to connect to each device using concurrent futures.
    Execute 'show ip arp' on each device.
    Lastly, record the total amount of time required to do this.
    """
    # Record start time
    start_time = datetime.now()

    # MAx of 4 child processes - 5 inc the parent
    max_threads = 4
    # Use context manager to create instance of ProcessPoolExecutor object and pass in max_thread no
    with ProcessPoolExecutor(max_threads) as pool:

        # Call map method on the ProcessPool passing in ssh_command3 and list of devices into the function one by one
        results_generator = pool.map(ssh_command3, device_list)

        # Loop through results generator and print the result
        for result in results_generator:
            print(result)
            print('-' * 80)

        # Record end time and print
        end_time = datetime.now()
        print('Total time taken for execution is: {}'.format(end_time - start_time))


if __name__ == '__main__':
   main()
