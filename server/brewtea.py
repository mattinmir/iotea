'''
This file is the remnant of what was to be a feature of our product, 
where tea recipes would be downloaded to the device, but could not
have both subscription to the broker and publishing to the broker to
run concurrently. So, this file was abandoned, but the logic is still 
sound - it would just require additional hardware.
'''


import sys
import paho.mqtt.client as mqtt
import json
import ubinascii

broad_lux = sys.argv[1]
ir_lux = sys.argv[2]
temperature = sys.argv[3]


def on_connect(client, userdata, rc):
    print("Connected with result code "+str(rc))

client = mqtt.Client()
client.on_connect = on_connect
client.connect('192.168.0.10', 1883, 60)

data = json.dumps(["broad_lux":broad_lux, "ir_lux":ir_lux, "temperature":temperature])
client.publish('esys/InternetOfThugs/brew', data)