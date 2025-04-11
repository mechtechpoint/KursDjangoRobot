#!/bin/bash

# Pierwszy argument to numer pinu
PIN=$1
# Drugi argument to stan (0 lub 1)
STAN=$2

# Ustaw pin jako wyjście
gpio mode $PIN out

# Ustaw żądany stan dla pinu
gpio write $PIN $STAN
