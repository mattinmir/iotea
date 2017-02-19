import paho.mqtt.client as mqtt
import brokerconnection 
import brokerinfo

# Create mqtt object
server = mqtt.Client()
server.on_connect = brokerconnection.on_connect
server.on_message = brokerconnection.on_message

# Connect to broker
server.connect(brokerinfo.ip_address, brokerinfo.port, brokerinfo.keepalive)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
server.loop_forever()
