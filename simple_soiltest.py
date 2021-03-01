
import time

from board import SCL, SDA
import busio

from adafruit_seesaw.seesaw import Seesaw


if __name__ == "__main__":

	i2c_bus = busio.I2C(SCL, SDA)

	ss = Seesaw(i2c_bus, addr=0x36)
	print("Room: Bedroom")
	print("Plant: Pilea Baby Tears\n")

	while True:
		# read moisture level through capacitive touch pad
		touch = ss.moisture_read()
	
		#read temperature from temperature sensor
		celcius_temp = ss.get_temp()
		fahrenheit_temp = (celcius_temp * (9/5)) + 32
		
		if (touch < 600):
			print("Needs More Water")
			print("Current Temp (F): " + str(fahrenheit_temp) + " Moisture: " + str(touch))
		elif (touch > 1500):
			print("Too Much Water")
			print("Current Temp (F): " + str(fahrenheit_temp) + " Moisture: " + str(touch))

		else:
			print("Temp (F): " + str(fahrenheit_temp) + " Moisture: " + str(touch))
		time.sleep(1)



