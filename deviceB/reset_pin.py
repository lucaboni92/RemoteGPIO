import RPi.GPIO as GPIO
from config import *
from pin_map_config import *

def pin_setup_output(pin_list):
	GPIO.setup(pin_list, GPIO.OUT, initial=GPIO.HIGH) #HIGH = relay OFF
	print("pin_setup_output() executed on BCM: ", pin_list)
	
def pin_setup_input(pin_list):
	GPIO.setup(pin_list , GPIO.IN)
	print("pin_setup_input() executed on BCM: ", pin_list)

def main():
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)

	try:
		pin_setup_output(pins_out)
		pin_setup_input(pins_in)

	except KeyboardInterrupt:
		# to intercept CRTL+C interrupt 		
		print ("\nQuitting...")
		client.disconnect()
	except Exception as e:
		# unexpected exception
		print("Unexpected error: ", e)

if __name__ == "__main__":
	main()
