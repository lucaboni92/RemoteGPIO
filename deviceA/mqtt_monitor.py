import paho.mqtt.client as mqtt
from config import *

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    #client.subscribe("$SYS/#")
    client.subscribe("#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def main():

    client = mqtt.Client()

    try:        
        client.on_connect = on_connect
        client.on_message = on_message

        client.username_pw_set(username, password=pwd)
        client.connect(broker)

        client.loop_forever()

    except KeyboardInterrupt:
        # to intercept CRTL+C interrupt 		
        print ("\nQuitting...")
        client.disconnect()
    except Exception as e:
        # unexpected exception
        print("Unexpected error: ", e)

if __name__ == "__main__":
	main()
