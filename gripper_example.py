from Robotiq2F85Driver import Robotiq2F85Driver
import time

# Initialize the driver with the gripper's serial number
tty_device = '/dev/ttyUSB3'
gripper = Robotiq2F85Driver.Robotiq2F85Driver(serial_number='FT89FKDO', tty_device=tty_device, debug=False)

# Reset the gripper
print(gripper.read_status())
gripper.reset()

# Move the gripper to fully open position (opening = 85 mm)
# The motion is done at 150 mm/s with a force of up to 235 Newtons.
time.sleep(3)

print("Opening")
gripper.go_to(opening=85, speed=150, force=235, blocking_call=False)
print("Opened")

time.sleep(3)

print("Closing")
gripper.go_to(opening=0, speed=120, force=205, blocking_call=False)
print("Closed")

time.sleep(3)

print("Opening")
gripper.go_to(opening=85, speed=150, force=235, blocking_call=False)
print("Opened")

'''
opening : float
Opening in millimeters. Must be between 0 and 85 mm.
speed : float
Speed in mm/s. Must be between 20 and 150 mm/s.
force : float
Force in N. Must be between 20 and 235 N.
'''
