#include <stdio.h>
#include <wiringPi.h>
#include <signal.h>
#include <stdlib.h>
#include <string.h>

#define PIN_PULSE 2
#define PIN_DIR_RIGHT 6
#define PIN_DIR_LEFT 4
#define DELAY_TIME 0.0001

int DELAY_TIME_M = DELAY_TIME * 1000000;

void cleanup_and_exit(int signal) {
    digitalWrite(PIN_PULSE, LOW);
    digitalWrite(PIN_DIR_RIGHT, LOW);
    digitalWrite(PIN_DIR_LEFT, LOW);
    exit(0);
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("Brak argumentu kierunku.\n");
        return 1;
    }

    wiringPiSetup();
    pinMode(PIN_PULSE, OUTPUT);
    pinMode(PIN_DIR_RIGHT, OUTPUT);
    pinMode(PIN_DIR_LEFT, OUTPUT);

    signal(SIGINT, cleanup_and_exit);

    if (strcmp(argv[1], "go") == 0) {
        digitalWrite(PIN_DIR_RIGHT, LOW);
        digitalWrite(PIN_DIR_LEFT, HIGH);
    } else if (strcmp(argv[1], "back") == 0) {
        digitalWrite(PIN_DIR_RIGHT, HIGH);
        digitalWrite(PIN_DIR_LEFT, LOW);
    } else if (strcmp(argv[1], "left") == 0) {
        digitalWrite(PIN_DIR_RIGHT, LOW);
        digitalWrite(PIN_DIR_LEFT, LOW);
    } else if (strcmp(argv[1], "right") == 0) {
        digitalWrite(PIN_DIR_RIGHT, HIGH);
        digitalWrite(PIN_DIR_LEFT, HIGH);
    }

    while (1) {
        digitalWrite(PIN_PULSE, HIGH);
        delayMicroseconds(DELAY_TIME_M);
        digitalWrite(PIN_PULSE, LOW);
        delayMicroseconds(DELAY_TIME_M);
    }

    return 0;
}
