from .led_blinker import stop_engine
from .sterowanie_pinem import setpin
import subprocess
import os
import time
alert_active = True
def alert():
    global alert_active
    alert_active = True
    while alert_active:
        # Uruchomienie komendy gpio readall i przechwycenie wyjścia
        result = subprocess.check_output("gpio readall", shell=True).decode('utf-8')
        
        # Wyszukiwanie linii zawierającej informacje o wPi 9
        for line in result.split("\n"):
            if " 9 " in line:  # Szukamy linii z wPi o wartości 9
                if "16 | 1 |" in line:  # Sprawdzamy czy wartość V (napięcie) jest ustawiona na 1
                    #print("pin16 on")
                    setpin(3, 1)
                    #print("stop silniki dolne")
                    stop_engine()
                    #print("stop ruch")
                    
                    
                    
        
        time.sleep(1)  # Czekamy sekundę przed kolejnym sprawdzeniem

def stop_alert():
    global alert_active
    alert_active = False
