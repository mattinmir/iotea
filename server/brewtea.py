import sys
from umqtt.simple import MQTTClient
import json
import ubinascii

broad_lux = sys.argv[1]
ir_lux = sys.argv[2]
temperature = sys.argv[3]

client = MQTTClient(machine.unique_id(), '192.168.0.10')
client.connect()
data = json.dumps(["broad_lux":broad_lux, "ir_lux":ir_lux, "temperature":temperature])
client.publish('esys/InternetOfThugs/brew', str.encode(data))