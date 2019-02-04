import Adafruit_BBIO.GPIO as GPIO
import time

led_pins = ['P9_23', 'P9_24', 'P9_11', 'P9_12', 'P9_13', 'P9_14', 'P9_15', 'P9_16', ]
seg = ['P8_11', 'P8_12', 'P8_13', 'P8_14', 'P8_15', 'P8_16', 'P8_17', 'P8_18', ]
switch = ['P8_7', 'P8_8', 'P8_9', 'P8_10', ]

num_display = {0 : ['P8_11', 'P8_12', 'P8_13', 'P8_14', 'P8_15', 'P8_16', ], 1 : ['P8_11', 'P8_12', ], 2 : ['P8_11', 'P8_12', 'P8_14', 'P8_15', 'P8_17', ], 3 : ['P8_11', 'P8_12', 'P8_13', 'P8_14', 'P8_17', ]}

out_pins = []
out_pins.extend(led_pins)
out_pins.extend(led_pins)
for i in out_pins: GPIO.setup(i, GPIO.OUT)
for i in switch: GPIO.setup(i, GPIO.IN)

def turn_on(x): GPIO.output(x, GPIO.HIGH)
def turn_off(x): GPIO.output(x, GPIO.LOW)

while 
