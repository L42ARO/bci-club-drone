from djitellopy import Tello

# Initialize the drone
drone = Tello()

# Connect to the drone
drone.connect()

# Take off
drone.takeoff()

# Fly forward for 100 cm
drone.move_forward(100)

# Turn clockwise 90 degrees
drone.rotate_clockwise(90)

# Land
drone.land()
