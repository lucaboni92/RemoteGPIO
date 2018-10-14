 # +-----+------+---+---Pi 3+--+---+------+-----+
 # | BCM | Mode | V | Physical | V | Mode | BCM |
 # +-----+------+---+----++----+---+------+-----+
 # |  17 |  OUT | 1 | 11 || 29 | 0 | IN   | 5   |
 # |  27 |  OUT | 1 | 13 || 31 | 0 | IN   | 6   |
 # |  22 |  OUT | 1 | 15 || 33 | 0 | IN   | 13  |
 # |  10 |  OUT | 1 | 19 || 35 | 0 | IN   | 19  |
 # +-----+------+---+----++----+---+------+-----+
 # | BCM | Mode | V | Physical | V | Mode | BCM |
 # +-----+------+---+---Pi 3+--+---+------+-----+

pins_out = [17,27,22,10] # BCM pins
pins_in = [5,6,13,19] #BCM pins

def translate_pin(pin):
	if pin  == 5:
		return 17
	elif pin == 6:
		return 27
	elif pin == 13:
		return 22
	elif pin == 19:
		return 10
	else:
		return "unknown"
