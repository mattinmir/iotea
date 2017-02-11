import json

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, rc):
    print("Connected with result code "+str(rc))
	# Subscribing in on_connect() means that if we lose the connection and
	# reconnect then subscriptions will be renewed.
    client.subscribe("esys/InternetOfThugs/tea")

# The callback for when a PUBLISH message is received from the server.


'''
JSON Data Structure and data types: 

[
	tea_id : int,
	name_of_tea : string,
	device_id : int,
	broad_lux : int,
	ir_lux : int,
	temperature : int
]
	 
'''
def on_message(client, userdata, msg):
	#print(msg.topic+ " " + str(msg.payload) )
	payload = json.loads(str(msg.payload))

	tea_id = payload['tea_id']
	name_of_tea  = payload['name_of_tea']
	device_id  = payload['device_id']
	broad_lux  = payload['broad_lux']
	ir_lux  = payload['ir_lux']
	temperature  = payload['temperature']

	
	
	
