from umqtt.simple import MQTTClient 
import tsl2561
import si7021
import time 
from machine import I2C, Pin

led = Pin(15 , Pin.OUT)

def making_other_tea(sensor_lux, sensor_temp, target_lux , target_temp) :
    current_lux= sensor_lux._read()[0]
    while current_lux > target_lux:
        print (current_lux, " : fixing colour")
        current_lux= sensor_lux._read()[0]
    print("colour is correct, removing teabag - setting temperature")
    current_temp=sensor_temp.readTemp()
    while not 0.99*target_temp < current_temp and  current_temp< 1.01*target_temp:
        time.sleep(0.5)
        if current_temp < 0.99*target_temp:
            print(current_temp," is too cold: heating")
        if current_temp > 1.01*target_temp:
            print(current_temp," is too hot: cooling")
        #print(current_temp)
        current_temp=sensor_temp.readTemp()

    print("tea is ready")
    led.high()

i2c_lux = I2C(scl=Pin(5), sda=Pin(4))
sensor_lux = tsl2561.TSL2561(i2c_lux)
sensor_lux.gain(16)
sensor_lux.integration_time(402) 
sensor_temp = si7021.Si7021(64)

current_lux = sensor_lux._read()[0] 
current_temp = sensor_temp.readTemp()

#def making_my_tea()




# if there is an input typed then make this tea
input_lux , input_temp = input("enter tea specs ").split()

making_other_tea(sensor_lux, sensor_temp, int(input_lux), int(input_temp))