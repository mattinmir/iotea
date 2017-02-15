import network
from network import WLAN
from umqtt.simple import MQTTClient
import machine
import ujson
import utime
import tsl2561
from machine import I2C, Pin
import read_temp_lux

#i2c = I2C(scl=Pin(5), sda=Pin(4))
#sensor = tsl2561.TSL2561(i2c)


ap_if = network.WLAN(network.AP_IF)
ap_if.active(False)

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('EEERover', 'exhibition')


client = MQTTClient(machine.unique_id(), '192.168.0.10')
client.connect()

id = machine.unique_id()

payload = ujson.dumps({'device_id':str(machine.unique_id()), 'broad_lux':sensor_lux._read()[0], 'ir_lux':sensor_lux._read()[1], 'temperature': sensor_temp.readTemp()})
client.publish('/topic/test', payload )
#payload = ujson.dumps({'tea_id': str(id)})

print (payload)
print(id)