"""
3a. Open a connection to the srx2 device and acquire a configuration lock.
Validate that configuration session is indeed locked by SSH'ing into the device and attempting to enter config mode
Reuse, the 'srx2' device definition from the jnpr_devices.py file that you created in exercise2.

You should receive a prompt similar to the following:
pyclass@srx2> configure
Entering configuration mode
Users currently editing the configuration:
  pyclass (pid 30316) on since 2019-03-08 18:30:51 PST
      exclusive

Add code to attempt to lock the configuration again.
Gracefully handle the "LockError" exception (meaning the configuration is already locked).

"""

from jnpr_devices import srx2 # SRX device dictionary
from jnpr.junos import Device # Device class
from jnpr.junos.utils.config import Config # Config class
from jnpr.junos.exception import LockError # For gracefully handling lock error
from getpass import getpass

# Create device object
device_conn = Device(**srx2)
device_conn.open() # Establish NETCONF connection
device_conn.timeout = 60 # Change device timeout

# Pass in NETCONF connection to Config object
cnfg = Config(device_conn)
print(cnfg.lock()) # Lock device to others so only we can be in config mode
# Put pause in the program otherwise after program ends and connection terminates the lock is automatically released
pause = input("Go check if you can go into config mode on the device: ")

# Gracefully catch the lock error exception which is thrown when we try to lock the config a 2nd time
try:
    cnfg.lock()
    pause = input("Wait: ")
except LockError: # Run this code if this exception thrown
    print("Error: The configuration is already locked for editing")
    pause = input("Wait: ")

