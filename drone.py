import cv2
from djitellopy import Tello
import time

# Initialize the drone
drone = Tello()

# Connect to the drone
drone.connect()


drone.streamon()
frame_read = drone.get_frame_read()

cv2.imwrite("image.png", frame_read.frame)

# Take off
drone.takeoff()


# Fly forward for 100 cm
drone.move_forward(100)

# Turn clockwise 90 degrees
drone.rotate_clockwise(90)

# Land
drone.land()
