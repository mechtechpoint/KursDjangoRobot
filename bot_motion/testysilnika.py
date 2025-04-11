from sterowanie_pinem import setpin
from time import sleep
import threading

PIN_PULSE = 2
PIN_DIR_RIGHT = 4
PIN_DIR_LEFT = 6

TIMEPULSE = 0.01  # wartość początkowa

def motor_pulse():
    while True:
        global TIMEPULSE
        setpin(PIN_PULSE, 1)
        sleep(TIMEPULSE)
        setpin(PIN_PULSE, 0)
        sleep(TIMEPULSE)

        # jeśli wartość TIMEPULSE wynosi 0, to kończymy wątek
        if TIMEPULSE == 0:
            break

def main():
    global TIMEPULSE
    threading.Thread(target=motor_pulse).start()
    
    while True:
        
        print("Aktualny czas pulsacji:", TIMEPULSE)
        choice = input("Wpisz 't', aby zmienić czas pulsacji lub 's', aby zatrzymać silnik: ")

        if choice == 't':
            try:
                new_time = float(input("Podaj nowy czas pulsacji (w sekundach): "))
                TIMEPULSE = new_time
            except ValueError:
                print("Niepoprawna wartość. Spróbuj ponownie.")
        elif choice == 's':
            TIMEPULSE = 0
            print("Silnik zatrzymany. Program kończy działanie.")
            break
        else:
            print("Niepoprawna opcja. Spróbuj ponownie.")


main()
