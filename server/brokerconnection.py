import json
from database import *
import dbinfo

db = database(dbinfo.ip_address, dbinfo.port, dbinfo.username, dbinfo.password, dbinfo.dbname)


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, rc):
    print("Connected with result code " + str(rc))
	# Subscribing in on_connect() means that if we lose the connection and
	# reconnect then subscriptions will be renewed.
    client.subscribe("/topic/test")




'''
JSON Data Structure and data types: 

[
	device_id : uint,
	broad_lux : uint,
	ir_lux : uint,
	temperature : uint
]
	 
'''
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
	payload = json.loads("["+str(msg.payload)[2:-1]+"]")

	device_id  = payload[0]['device_id']
	broad_lux  = payload[0]['broad_lux']
	ir_lux  = payload[0]['ir_lux']
	temperature  = payload[0]['temperature']

	tea_id = db.next_tea_id()

	db.insert(tea_id, device_id, broad_lux, ir_lux, temperature)
