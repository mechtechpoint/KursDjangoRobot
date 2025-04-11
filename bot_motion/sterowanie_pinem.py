import subprocess
import os
import time


def setpin(pin, stan):
    result = subprocess.run(['ustaw_pin.sh', str(pin), str(stan)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        raise Exception(f"Error executing script: {result.stderr.decode('utf-8')}")
        

process = None

def initiate_sensor():
    global process
    current_directory = os.path.dirname(os.path.abspath(__file__))
    hc_sensor_path = os.path.join(current_directory, "hc_sensor")
    process = subprocess.Popen(["sudo", hc_sensor_path])
    
    


    
