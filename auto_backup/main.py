import pyudev
import os
import time


context = pyudev.Context()
monitor = pyudev.Monitor.from_netlink(context)
monitor.filter_by(subsystem='usb')

for device in iter(monitor.poll, None):
    if device.action == 'add' and device.device_node is not None:
        time.sleep(6)
        print(os.path.isdir("/media/christian-kohl/My Passport/backup_folder"))

