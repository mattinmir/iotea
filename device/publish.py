'''
Used to publish reading of brewed tea to server
'''

import network
from umqtt.simple import MQTTClient
import machine
import ubinascii
import ujson
import utime
import tsl2561
import si7021
from machine import I2C, Pin


# Set sensor Settings
i2c_lux = I2C(scl=Pin(5), sda=Pin(4))
sensor_lux = tsl2561.TSL2561(i2c_lux)
sensor_lux.gain(16)
sensor_lux.integration_time(402)
sensor_temp = si7021.Si7021(64)

# Connect to broker 
ap_if = network.WLAN(network.AP_IF)
ap_if.active(False)
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('EEERover', 'exhibition')
client = MQTTClient(machine.unique_id(), '192.168.0.10')
client.connect()

# Publish reading
payload = ujson.dumps({'device_id':str(machine.unique_id()), 'broad_lux':sensor_lux._read()[0], 'ir_lux':sensor_lux._read()[1], 'temperature': sensor_temp.readTemp()})
client.publish('/topic/test', payload )



