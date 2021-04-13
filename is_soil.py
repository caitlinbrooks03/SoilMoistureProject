import time
from ISStreamer.Streamer import Streamer
from board import SCL, SDA
import busio
from adafruit_seesaw.seesaw import Seesaw

# --------- User Settings ----------- 
SENSOR_LOCATION_NAME = "Pilea Baby Tears"
BUCKET_NAME = "House Plant"
BUCKET_KEY = "6VDT99BXPS77"
ACCESS_KEY = "ist_DB52Yw4zk_grxkquzx1l5bG7ynIkV7oa"
MIN_BETWEEN_READS = 0.1
# ------------------------------------

i2c_bus = busio.I2C(SCL, SDA)

ss = Seesaw(i2c_bus, addr = 0x36)

streamer = Streamer(bucket_name=BUCKET_NAME, bucket_key = BUCKET_KEY, access_key = ACCESS_KEY)

while True:
	#read moisture levels through capactive touch pad
	touch = ss.moisture_read()
	
	#read temperature from the temperature sensor and convert to F
	temp = ss.get_temp()
	temp_f = format(temp * 9.0/ 5.0 + 32, ".2f")

	streamer.log(SENSOR_LOCATION_NAME + " Moisture", touch)
	streamer.log(SENSOR_LOCATION_NAME + " Temperature", temp_f)
	streamer.flush()

	time.sleep(60*MIN_BETWEEN_READS)
