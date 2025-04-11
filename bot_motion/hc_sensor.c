#include <stdio.h>
#include <string.h>
#include <wiringPi.h>

#define TRIG 5  // Zmieniaj według własnej konfiguracji
#define ECHO 7  // Zmieniaj według własnej konfiguracji
#define ENABLE  9  // Pin dla diody
#define CONTROL_FILE "control.txt"

void setup() {
    wiringPiSetup();
    pinMode(TRIG, OUTPUT);
    pinMode(ECHO, INPUT);
    pinMode(ENABLE, OUTPUT);

    // Upewnij się, że początkowy stan wyjścia TRIG to LOW
    digitalWrite(TRIG, LOW);
    digitalWrite(ENABLE, LOW);  // Upewnij się, że dioda jest wyłączona na początku
    delay(30);
}

int getCM() {
    // Wyślij impuls 10us na TRIG
    digitalWrite(TRIG, HIGH);
    delayMicroseconds(10);
    digitalWrite(TRIG, LOW);

    // Czekaj na sygnał HIGH i mierz czas trwania
    while(digitalRead(ECHO) == LOW);

    long startTime = micros();
    while(digitalRead(ECHO) == HIGH);
    long travelTime = micros() - startTime;

    // Konwersja czasu podróży na odległość, używając prędkości dźwięku: 343m/s = 34300cm/s = 0.0343cm/us = 34.3cm/ms
    int distance = travelTime / 58;

    return distance;
}




int main(void) {
    FILE *fp;
    setup();

    while(1) {
        FILE *fp = fopen("/home/orangepi/programowanie/WRbot/bot_motion/control.txt", "r");
        if(fp == NULL) {
            perror("Nie można otworzyć pliku kontrolnego");
            return 1;
        }
        
        char control[6];
        if(fscanf(fp, "%5s", control) == 1) {
            if(strcmp(control, "false") == 0) {
                digitalWrite(ENABLE, LOW); 
                digitalWrite(TRIG, LOW);
                fclose(fp);
                return 0;
            }
        }
        fclose(fp);

        int distance = getCM();
        
        if(distance <= 30) {
            digitalWrite(ENABLE, HIGH);
        } else {
            digitalWrite(ENABLE, LOW);
        }
        
        delay(1000);
    }

    return 0;
}
