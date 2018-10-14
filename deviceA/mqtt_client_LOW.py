import paho.mqtt.client as mqtt
from config import *

def main():

    client = mqtt.Client()

    try:
        client.username_pw_set(username, password=pwd)
        client.connect(broker)

        client.publish("cmnd/deviceB/BCM17", payload="LOW", qos=0)

    except KeyboardInterrupt:
        # to intercept CRTL+C interrupt 		
        print ("\nQuitting...")
    except Exception as e:
        # unexpected exception
        print("Unexpected error: ", e)

if __name__ == "__main__":
	main()
        
