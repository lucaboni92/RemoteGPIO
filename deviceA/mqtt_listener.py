import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
from config import *
from pin_map_config import *

#device_name = deviceA
#device_ip = "192.168.1.50"


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))

	# Subscribing in on_connect() means that if we lose the connection and
	# reconnect then subscriptions will be renewed.
	#client.subscribe("$SYS/#")
	
	# OUTPUT BCM PINS: 17,27,22,10
	client.subscribe("cmnd/deviceA/BCM17")
	client.subscribe("cmnd/deviceA/BCM27")
	client.subscribe("cmnd/deviceA/BCM22")
	client.subscribe("cmnd/deviceA/BCM10")
	
	# INPUT BCM PINS: 5,6,13,19
	# client.subscribe("cmnd/deviceA/BCM5")
	# client.subscribe("cmnd/deviceA/BCM6")
	# client.subscribe("cmnd/deviceA/BCM13")
	# client.subscribe("cmnd/deviceA/BCM19")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
	print(msg.topic+" "+str(msg.payload))
	cmd_array = msg.topic.split("/")
	mqtt_cmd_type = cmd_array[0]
	mqtt_device = cmd_array[1]
	mqtt_pin = cmd_array[2]
	if mqtt_cmd_type == "cmnd":
		pin = pin_translate(mqtt_pin)
		if pin != "unknown":
			if str(msg.payload) == "HIGH" or str(msg.payload) == "1":
				GPIO.output(pin, GPIO.LOW) #HIGH = relay OFF - LOW = relay ON
				print("GPIO.output("+pin+", GPIO.LOW)")
			elif str(msg.payload) == "LOW" or str(msg.payload) == "0":
				GPIO.output(pin, GPIO.HIGH)
				print("GPIO.output("+pin+", GPIO.HIGH)")
			else:
				print ("payload error")
	
def pin_setup_output(pin_list):
	GPIO.setup(pin_list, GPIO.OUT, initial=GPIO.HIGH)
	print("pin_setup_output() executed on BCM: ", pin_list)
	
def pin_translate(mqtt_pin):
	if mqtt_pin == "BCM17":
		return 17
	elif mqtt_pin == "BCM27":
		return 27
	elif mqtt_pin == "BCM22":
		return 22
	elif mqtt_pin == "BCM10":
		return 10
	else:
		return "unknown"

def main():
	GPIO.setmode(GPIO.BCM)
	client = mqtt.Client()
	GPIO.setwarnings(False)

	try:
		pin_setup_output(pins_out)
		
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
