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
client.publish('esys/InternetOfThugs/tea', str.encode(x) )


# sudo screen /dev/ttyUSB0 115200
# ctrl-E for paste mode
# ctrl-D to run

