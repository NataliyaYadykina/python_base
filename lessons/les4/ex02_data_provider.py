# Модуль 1: сбор информации с датчиков - data_provider 
# (get_temperature, get_pressure, get_wind_speed)
# Модуль 2: логирование - logger 
# (temperature_logger, pressure_logger, wind_speed_logger)
# Модуль 3: UI - user_interface 
# (temperature_view, pressure_view, wind_speed_view)
# Модуль 4: HTML-генератор - html_creater (create)
# Модуль 5: главный модуль - main

from random import randint

def get_temperature(sensor):
	return randint(-20, 0) if sensor else randint(0, 20)

def get_pressure(sensor):
	if sensor:
		return randint(720, 750)
	else:
		return randint(750, 770)

def get_wind_speed(sensor):
	if sensor == 1:
		return randint(0, 30)
	else:
		return randint(30, 50)

def data_collection(sensor = 1):
	return (get_temperature(sensor), get_pressure(sensor), get_wind_speed(sensor))