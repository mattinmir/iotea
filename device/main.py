'''
import network
from umqtt.simple import MQTTClient
import machine  
import ubinascii
import tsl2561
import ustruct

from machine import I2C, Pin

i2c = I2C(scl=Pin(5), sda=Pin(4))
sensor = tsl2561.TSL2561(i2c)

sensor.gain(1)
sensor.integration_time(402)

ap_if = network.WLAN(network.AP_IF)
ap_if.active(False)

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('EEERover', 'exhibition')

reading = sensor._read()

broad = reading[0]
ir = reading[1]

#print(ustruct.pack('b', ir))


client = MQTTClient(machine.unique_id(), '192.168.0.10')
client.connect()

client.publish('esys/InternetOfThugs/broad',  b'hihihihihihihihihihihihihihihihihihi'  )
#client.publish('esys/InternetOfThugs/ir', str.encode(ir))


# sudo screen /dev/ttyUSB0 115200
# ctrl-E for paste mode
# ctrl-D to run
'''

import network
from umqtt.simple import MQTTClient
import machine  
import ubinascii


ap_if = network.WLAN(network.AP_IF)
ap_if.active(False)

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('EEERover', 'exhibition')


client = MQTTClient(machine.unique_id(), '192.168.0.10')
client.connect()
x="pepepepepepepepepepepepeppepepepepepepepepepepepepepe"
client.publish('/topic/test', str.encode(x) )


# sudo screen /dev/ttyUSB0 115200
# ctrl-E for paste mode
# ctrl-D to run


