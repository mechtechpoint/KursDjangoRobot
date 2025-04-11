from django.shortcuts import render
from django.http import JsonResponse
import threading
import subprocess
from django.http import HttpResponse
from .led_blinker import start_engine, stop_engine, active_thread, onsilnikidolne, offsilnikidolne
from .sterowanie_pinem import initiate_sensor
from .alertPIN import alert,stop_alert
alert_thread = None
import cv2
import os

def index(request):
    return render(request, 'bot_motion/index.html')

def go(request):
    start_engine("go")
    return HttpResponse(status=204)

def back(request):
    start_engine("back")
    return HttpResponse(status=204)

def left(request):
    start_engine("left")
    return HttpResponse(status=204)

def right(request):
    start_engine("right")
    return HttpResponse(status=204)

def stop(request):
    stop_engine()
    return HttpResponse(status=204)
    
def startsensor(request):
    global alert_thread
    
    # Ścieżka do pliku control.txt
    file_path = '/home/orangepi/programowanie/WRbot/bot_motion/control.txt'
    try:
        with open(file_path, 'w') as file:
            file.write("true")
    except:
        print("lipton startsensor")
    
    initiate_sensor()  # Funkcja z Pythona do uruchamiania procesu C
    
    # Uruchomienie wątku alertu
    alert_thread = threading.Thread(target=alert)
    alert_thread.start()

    return HttpResponse(status=204)

def stopsensor(request):
    global alert_thread

    # Ścieżka do pliku control.txt
    file_path = '/home/orangepi/programowanie/WRbot/bot_motion/control.txt'
    try:
        with open(file_path, 'w') as file:
            file.write("false")
    except:
        print("lipton stop sensor")
    stop_alert()
    if alert_thread is not None:
        alert_thread.join()  # Zakończ wątek alertu
        alert_thread = None  # Zresetuj wątek alertu
    
    return HttpResponse(status=204)
    

def turn_on_pin3(request):
    onsilnikidolne()
    return HttpResponse(status=204)

def turn_off_pin3(request):
    offsilnikidolne()
    return HttpResponse(status=204)
    
def take_photo(request):
    try:
        cap = cv2.VideoCapture(1)  # 1 oznacza kamerę zewnętrzną; 0 to domyślna kamera

        ret, frame = cap.read()
        if not ret:
            print("error: Nie udało się zrobić zdjęcia.")
            return HttpResponse(status=204)

        file_path = '/home/orangepi/programowanie/WRbot/bot_motion/static/bot_motion/photo.jpg'
        cv2.imwrite(file_path, frame)
        cap.release()

        return HttpResponse(status=204)

    except Exception as e:
        print(f"error: {e}")  # Wydrukuj informacje o błędzie do konsoli
        return HttpResponse(status=204)
