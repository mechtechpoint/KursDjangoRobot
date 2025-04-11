# led_blinker.py

from .sterowanie_pinem import setpin
from time import sleep
import threading
import subprocess
import os
active_thread = None
PIN_PULSE = 2
PIN_DIR_RIGHT = 4
PIN_DIR_LEFT = 6


def get_jazda_path():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_directory, "jazdaT")

def start_engine(direction):
    global active_thread

    # Zakończ poprzedni proces jeśli istnieje
    if active_thread is not None:
        kill_with_sudo("jazdaT")  # Zakończ wszystkie procesy o nazwie "jazda"
        
    # Uruchom plik jazda.c z odpowiednim kierunkiem jako argument
    active_thread = subprocess.Popen(["sudo", get_jazda_path(), direction])

def kill_with_sudo(process_name):
    #print(f"Attempting to kill processes named: {process_name}")
    cmd = ['sudo', 'pkill', '-9', '-f', process_name]
    subprocess.run(cmd)
    #print(cmd)

def stop_engine():
    global active_thread
    if active_thread is not None:
        kill_with_sudo("jazdaT")  # Zakończ wszystkie procesy o nazwie "jazda"
        active_thread = None
    #setpin(PIN_PULSE, 0)
    print("setpinPIN_PULSE, 0")
    #setpin(PIN_DIR_RIGHT, 0)
    print("PIN_DIR_RIGHT, 0")
    #setpin(PIN_DIR_LEFT, 0)
    print("setpinPIN_DIR_LEFT, 0")

    
def onsilnikidolne():
	#setpin(3, 0)
	print("setpin3, 0")

def offsilnikidolne():
	#setpin(3, 1)
	print("setpin3, 1")
