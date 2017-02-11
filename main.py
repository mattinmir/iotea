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


ap_if = network.WLAN(network.AP_IF)
ap_if.active(False)

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('EEERover', 'exhibition')

sensor.gain(16)
sensor.integration_time(402)

client = MQTTClient(machine.unique_id(), '192.168.0.10')
client.connect()

payload = ujson.dumps({'tea_id': 652510, 'name_of_tea': 'pepepepepermint tea','device_id':str(machine.unique_id()), 'broad_lux':sensor._read()[0], 'ir_lux':sensor._read()[1], 'temperature': 69})
print(payload)


client.publish('esys/InternetOfThugs/tea', payload )

# sudo screen /dev/ttyUSB0 115200
# ctrl-E for paste mode
# ctrl-D to run
