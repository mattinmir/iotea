import read_temp_lux
import umqtt.simple import MQTTClient
import json
current_temp = sensor_temp.readTemp()
current_lux = sensor_lux._read()[0]
current_ir = sensor_lux._read()[1]

teabag = False
heat = True
  
def on_connect(client, userdata, rc):
    print("Connected with result code "+str(rc))
	# Subscribing in on_connect() means that if we lose the connection and
	# reconnect then subscriptions will be renewed.
    client.subscribe("esys/InternetOfThugs/tea")

def on_message(client, userdata, msg):
	
	payload = json.loads(str(msg.payload))

	#time = payload['time'] 
	#device_id  = payload['device_id']
	target_lux  = payload['broad_lux']
	target_ir  = payload['ir_lux']
	target_temp  = payload['temperature']

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message


while current_lux != target_lux:
    current_lux = sensor_lux._read()[0]
teabag =  True
print(teabag);

while current_temp != target_temp
    current_temp = sensor_temp.readTemp()



