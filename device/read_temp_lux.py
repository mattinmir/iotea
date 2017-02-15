import tsl2561
import si7021
import time 
from machine import I2C, Pin

i2c_lux = I2C(scl=Pin(5), sda=Pin(4))
sensor_lux = tsl2561.TSL2561(i2c_lux)
sensor_lux.gain(16)
sensor_lux.integration_time(402)

sensor_temp = si7021.Si7021(64)

while (1):
	print(sensor_lux._read()[0] , sensor_lux._read()[1])
  	print(sensor_temp.readTemp())
  
# working for reading values from temp and lux sensors 

