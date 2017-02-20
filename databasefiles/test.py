'''
  TO TEST SERVER PUBLISHING .tea FILE TO MQTT BROKER
  TODO for automatic publish of .tea file from server database
'''

import sys
import paho.mqtt.client as mqtt
import json
from time import sleep


#Pass dummy specifications through command line
broad_lux = sys.argv[1]
ir_lux = sys.argv[2]
temperature = sys.argv[3]


def on_connect(client, userdata, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("esys/InternetOfThugs/brew")

def on_message(mosq, obj, msg):
    print("Message =" + str(msg))

def on_publish(mosq, obj, mid):
    print("Published " + str(mid))

def on_subscribe(mosq, obj, mid, granted_qos):
    print("Subscribed")

client = mqtt.Client()

client.on_message = on_message
client.on_connect = on_connect
client.on_publish = on_publish
client.on_subscribe = on_subscribe

client.connect('192.168.0.10', 1883, 60)

#Publish json to broker
data = json.dumps([{"broad_lux":broad_lux, "ir_lux":ir_lux, "temperature":temperature}])
client.publish('esys/InternetOfThugs/brew', data)
