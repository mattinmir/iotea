'''
Used to control brewing of tea to specifications
'''

from umqtt.simple import MQTTClient 
import tsl2561
import si7021
import time 
from machine import I2C, Pin

led = Pin(15 , Pin.OUT)

def make_tea(sensor_lux, sensor_temp, target_lux , target_temp):

    # Read luminosity until tea has reached desired opacity
    current_lux = sensor_lux._read()[0]
    while current_lux > target_lux:
        print (current_lux, " : fixing colour")
        current_lux= sensor_lux._read()[0]

    print("Colour is correct, removing teabag - setting temperature")



    # Read temperature until tea has reached target temperature (within 1%)
    current_temp=sensor_temp.readTemp()
    while not 0.99*target_temp < current_temp and  current_temp< 1.01*target_temp:

        time.sleep(0.5) # Rate limit to conserve power

        if current_temp < 0.99*target_temp:
            print(current_temp," is too cold: heating")
        elif current_temp > 1.01*target_temp:
            print(current_temp," is too hot: cooling")
        current_temp=sensor_temp.readTemp()

    # Set LED high when tea is done to notify user
    print("Tea is ready")
    led.high()

# Creating sensor objects
i2c_lux = I2C(scl=Pin(5), sda=Pin(4))
sensor_lux = tsl2561.TSL2561(i2c_lux)
sensor_temp = si7021.Si7021(64)

# Setting sensitivity of sensor
sensor_lux.gain(16)
sensor_lux.integration_time(402) 


# Enter .tea parameters and make tea
input_lux , input_temp = input("Enter .tea parameters: ").split()
make_tea(sensor_lux, sensor_temp, int(input_lux), int(input_temp))