#!/bin/bash
export PATH=/usr/local/bin:$PATH
cd /home/orangepi/programowanie/WRbot
source bot_env/bin/activate
cd /home/orangepi/programowanie/WRbot
python manage.py runserver 0.0.0.0:8000
