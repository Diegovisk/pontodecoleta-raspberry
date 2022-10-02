from paho.mqtt.client import Client
import paho.mqtt.client as paho
import os

def __init__(self,client_id):
    client = Client(client_id=client_id)
    # client = Client(client_id='', userdata=None, protocol= paho.MQTTv5)

def on_connect(client, userdata, flags, rc, properties=None):
    print("CONNACK received with code %s." % rc)

def on_publish(client, userdata, mid, properties=None):
    print("mid: " + str(mid))

def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_message(client, userdata, msg):
    # TO-DO: pegar o payload e inserir no banco 
    print(msg.topic + " " + str(msg.qos) + " "+ str(msg.payload))	

def ask_exit(*args):
    pass

client = paho.Client(client_id="raspberry")

client.on_connect = on_connect        
client.on_message =  on_message
client.on_disconnect = on_disconnect
client.on_subscribe = on_subscribe


# por algum motivoo.............. a pasta de "config" 
# nao sobe com o git..... mas eh uma pasta config/.env 
# e dentro do .env tem 
host = os.getenv("MQTT_HOST")
client.connect(host)
client.loop_forever()
