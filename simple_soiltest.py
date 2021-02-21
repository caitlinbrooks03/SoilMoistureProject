import time

from board import SCL, SDA
import busio

from adafruit_seesaw.seesaw import Seesaw

i2c_bus = busio.I2C(SCL, SDA)

ss = Seesaw(i2c_bus, addr=0x36)

while True:
	# read moisture level through capacitive touch pad
	touch = ss.moisture_read()

	#read temperature from temperature sensor
	celcius_temp = ss.get_temp()
	fahrenheit_temp = (celcius_temp * (9/5)) + 32
	
	if(touch < 600):
		print("Needs more Water")
	elif (touch > 1500):
		print("Too Wet")
	else:
		print("Temp (F): " + str(fahrenheit_temp) + "\n Moisture: " + str(touch))
	time.sleep(1)
