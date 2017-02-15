import network
from network import WLAN
from umqtt.simple import MQTTClient
import machine
import ujson
import utime
import tsl2561
from machine import I2C, Pin
i2c = I2C(scl=Pin(5), sda=Pin(4))
sensor = tsl2561.TSL2561(i2c)

sensor.gain(16)
sensor.integration_time(402)


id = machine.unique_id()

print(sensor._read()[0])

payload = ujson.dumps({'tea_id': 652510, 'name_of_tea': 'pepepepepermint tea','device_id':str(machine.unique_id()), 'broad_lux':sensor._read()[0], 'ir_lux':sensor._read()[1], 'temperature': 69})

print (payload)
print(id)