import json
from database import *

db = database('129.31.228.132', 3306, 'root', '', 'TEA')


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, rc):
    print("Connected with result code "+str(rc))
	# Subscribing in on_connect() means that if we lose the connection and
	# reconnect then subscriptions will be renewed.
    client.subscribe("esys/InternetOfThugs/tea")




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
	#print(msg.topic+ " " + str(msg.payload) )
	
	payload = json.loads(str(msg.payload))

	time = payload['time'] 
	device_id  = payload['device_id']
	broad_lux  = payload['broad_lux']
	ir_lux  = payload['ir_lux']
	temperature  = payload['temperature']

	tea_id = db.next_tea_id()

	db.insert(time, tea_id, '', '', device_id, broad_lux, ir_lux, temperature)

	''''
	cnx = pymysql.connect(host='129.31.228.132', port=3306, user='root', passwd='', db='TEA')

	insert_query = ("INSERT INTO `TEA`. `teaTable` (`tea_id`, `name_of_tea`, `device_id`, `broad_lux`, `ir_lux`, `temperature`) VALUES (tea_id, , name_of_tea , '1', '1', '1');")

	cursor = cnx.cursor()
	cursor.execute(insert_query)

	cnx.commit()
	cursor.close()
	cnx.close()
	'''
