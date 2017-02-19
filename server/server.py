import paho.mqtt.client as mqtt
import brokerconnection 
import brokerinfo

client = mqtt.Client()
client.on_connect = brokerconnection.on_connect
client.on_message = brokerconnection.on_message

# Connect to broker
client.connect(brokerinfo.ip_address, brokerinfo.port, brokerinfo.keepalive)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
