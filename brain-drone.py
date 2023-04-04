
from live_commands import *
import threading
import time

your_app_client_id = '' #My creds
your_app_client_secret = '' #my creds

    # Init live advance
l = LiveCommand(your_app_client_id, your_app_client_secret)

trained_profile_name = 'Alvaro' # Please set a trained profile name here

def runDrone():
    print("Running Drone")
    #Place drone code here

def runAPI():
    global l, trained_profile_name
    print("Running API")
    l.start(trained_profile_name)

t = threading.Thread(target=runAPI)
t.start()
time.sleep(2)
runDrone()