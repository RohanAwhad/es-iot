import Adafruit_BBIO.GPIO as GPIO
import time

# 1 2 3 4
red_pin = ['P9_11','P9_23','P8_18','P8_11']
green_pin = ['P9_15','P9_14','P8_14','P8_15']
yellow_pin = ['P9_13','P9_16','P8_16','P8_13']
left_green_pin = ['P9_24','P9_12','P8_12','P8_17']

vcc = ['P8_7','P8_8']
pins = []
pins.extend(red_pin)
pins.extend(green_pin)
pins.extend(yellow_pin)
pins.extend(left_green_pin)
pins.extend(vcc)

#set output on
for i in pins: GPIO.setup(i, GPIO.OUT)

for i in red_pin: GPIO.output(i, GPIO.HIGH)
for i in green_pin: GPIO.output(i, GPIO.LOW)
for i in yellow_pin: GPIO.output(i, GPIO.LOW)
for i in left_green_pin: GPIO.output(i, GPIO.HIGH)

pins = []
pins.append(red_pin)
pins.append(green_pin)
pins.append(yellow_pin)

def turn_on(red, green, yellow):
	GPIO.output(red, GPIO.LOW)
	GPIO.output(green, GPIO.HIGH)
	time.sleep(5)
	GPIO.output(green, GPIO.LOW)
	GPIO.output(yellow, GPIO.HIGH)
	time.sleep(2)
	GPIO.output(yellow, GPIO.LOW)
	GPIO.output(red, GPIO.HIGH)
	
while True:
	for i in range(4):
		turn_on(pins[0][i], pins[1][i], pins[2][i])
