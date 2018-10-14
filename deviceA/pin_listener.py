import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
from time import sleep
from config import *
from pin_map_config import *

pin_state = {
	5 : 0,
	6 : 0,
	13 : 0,
	19 : 0
	}

def pin_setup_input(pin_list):
	GPIO.setup(pin_list , GPIO.IN)
	print("pin_setup_input() executed on BCM: ", pin_list)
	
def pin_state_setup(pin_state):
	for pin in pins_in:
		pin_state[pin] = GPIO.input(pin)
		print "pin_state_setup(",pin,") executed"

def main():
	client = mqtt.Client()
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	
	try:
		client.username_pw_set(username, password=pwd)
		client.connect(broker)
		pin_setup_input(pins_in)
		pin_state_setup(pin_state)
		
		while(1):
			for pin in pins_in:
				print "BCM", pin, " -> ", GPIO.input(pin)
				if pin_state[pin] != GPIO.input(pin):
					pin_state[pin] = GPIO.input(pin)
					if(pin_state[pin] == 1):
						out_pin = translate_pin(pin)
						mqtt_cmd = "cmnd/deviceB/BCM" + str(out_pin)
						client.publish(mqtt_cmd, payload="HIGH", qos=0)
					elif(pin_state[pin] == 0):
						out_pin = translate_pin(pin)
						mqtt_cmd = "cmnd/deviceB/BCM" + str(out_pin)
						client.publish(mqtt_cmd, payload="LOW", qos=0)
			sleep(refresh_time)
			print ""

	except KeyboardInterrupt:
		# to intercept CRTL+C interrupt 		
		print ("\nQuitting...")
		client.disconnect()
	except Exception as e:
		# unexpected exception
		print("Unexpected error: ", e)

if __name__ == "__main__":
	main()
