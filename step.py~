import Adafruit_BBIO.GPIO as GPIO
import time

GPIO.setup("P9_11", GPIO.OUT)
GPIO.setup("P9_12", GPIO.OUT)
GPIO.setup("P9_13", GPIO.OUT)
GPIO.setup("P9_14", GPIO.OUT)

n = 2

print("Clockwise {} times")

for _ in range(n):
	for i in range(24):
	
		GPIO.output("P9_11", GPIO.HIGH)
		GPIO.output("P9_12", GPIO.LOW)
		GPIO.output("P9_13", GPIO.LOW)
		GPIO.output("P9_14", GPIO.LOW)
		time.sleep(1)

		GPIO.output("P9_11", GPIO.LOW)
		GPIO.output("P9_12", GPIO.HIGH)
		GPIO.output("P9_13", GPIO.LOW)
		GPIO.output("P9_14", GPIO.LOW)
		time.sleep(1)

		GPIO.output("P9_11", GPIO.LOW)
		GPIO.output("P9_12", GPIO.LOW)
		GPIO.output("P9_13", GPIO.HIGH)
		GPIO.output("P9_14", GPIO.LOW)
		time.sleep(1)

		GPIO.output("P9_11", GPIO.LOW)
		GPIO.output("P9_12", GPIO.LOW)
		GPIO.output("P9_13", GPIO.LOW)
		GPIO.output("P9_14", GPIO.HIGH)
		time.sleep(1)

print("AntiClockwise {} times")

for _ in range(n):
	for i in range(24):
		
		GPIO.output("P9_11", GPIO.LOW)
		GPIO.output("P9_12", GPIO.LOW)
		GPIO.output("P9_13", GPIO.LOW)
		GPIO.output("P9_14", GPIO.HIGH)
		time.sleep(1)

		GPIO.output("P9_11", GPIO.LOW)
		GPIO.output("P9_12", GPIO.LOW)
		GPIO.output("P9_13", GPIO.HIGH)
		GPIO.output("P9_14", GPIO.LOW)
		time.sleep(1)

		GPIO.output("P9_11", GPIO.LOW)
		GPIO.output("P9_12", GPIO.HIGH)
		GPIO.output("P9_13", GPIO.LOW)
		GPIO.output("P9_14", GPIO.LOW)
		time.sleep(1)

		GPIO.output("P9_11", GPIO.HIGH)
		GPIO.output("P9_12", GPIO.LOW)
		GPIO.output("P9_13", GPIO.LOW)
		GPIO.output("P9_14", GPIO.LOW)
		time.sleep(1)




