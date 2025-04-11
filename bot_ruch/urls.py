"""
URL configuration for bot_ruch project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from bot_motion.views import *

urlpatterns = [
	path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('go/', go, name='go'),
    path('back/', back, name='back'),
    path('left/', left, name='left'),
    path('right/', right, name='right'),
    path('stop/', stop, name='stop'),
    path('start_sensor/', startsensor, name='start_sensor'),
	path('stop_sensor/', stopsensor, name='stop_sensor'),
	path('turn_on_pin3/', turn_on_pin3, name='turn_on_pin3'),
    path('turn_off_pin3/', turn_off_pin3, name='turn_off_pin3'),
    path('take_photo/', take_photo, name='take_photo'),
]
