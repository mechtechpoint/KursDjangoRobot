#!/bin/bash

# Funkcja do ustawiania stanu pinu
set_pin() {
    local PIN=$1
    local STAN=$2
    gpio mode $PIN out
    gpio write $PIN $STAN
}

# Obsługa przerwania CTRL+C
trap "set_pin 16 0; exit" SIGINT

# Główna pętla programu
while true; do
    # Ustaw pin 2 na 1 (włącz)
    set_pin 16 1
    sleep $1
    # Ustaw pin 2 na 0 (wyłącz)
    set_pin 16 0
    sleep $1
done
