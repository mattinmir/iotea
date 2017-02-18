import json
from database import *

db = database('192.168.0.132', 3306, 'root', '', 'TEA')


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, rc):
    print("Connected with result code "+str(rc))
	# Subscribing in on_connect() means that if we lose the connection and
	# reconnect then subscriptions will be renewed.
    client.subscribe("/topic/test")




'''
JSON Data Structure and data types: 

[
	time : datetime,
	device_id : int,
	broad_lux : int,
	ir_lux : int,
	temperature : int
]
	 
'''
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
	#print("\'["+str(msg.payload)[2:-1]+"]\'" )
	
	payload = json.loads("["+str(msg.payload)[2:-1]+"]")

	#payload = json.loads('[{"ir_lux": 464, "broad_lux": 4370, "temperature": 32.88036, "device_id": "b\'\\\\xf2\\\\xd7\\\\xc6\\\\x00\'"}]')
	#print(payload)
	device_id  = payload[0]['device_id']
	broad_lux  = payload[0]['broad_lux']
	ir_lux  = payload[0]['ir_lux']
	temperature  = payload[0]['temperature']

	tea_id = db.next_tea_id()

	db.insert(tea_id, device_id, broad_lux, ir_lux, temperature)

	''''
	cnx = pymysql.connect(host='129.31.228.132', port=3306, user='root', passwd='', db='TEA')

	insert_query = ("INSERT INTO `TEA`. `teaTable` (`tea_id`, `name_of_tea`, `device_id`, `broad_lux`, `ir_lux`, `temperature`) VALUES (tea_id, , name_of_tea , '1', '1', '1');")

	cursor = cnx.cursor()
	cursor.execute(insert_query)

	cnx.commit()
	cursor.close()
	cnx.close()
	'''
