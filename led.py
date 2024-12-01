#respberry flash led 
# led + connect pin 1(3.3v)  ,- connect pin 11 (GPIO 17)
import RPi.GPIO as GPIO
import time

led_pin = 11

def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(led_pin, GPIO.OUT)
	GPIO.output(led_pin, GPIO.HIGH)

def loop():
	while True:
		print ('... led on')
		GPIO.output(led_pin,GPIO.LOW)
		time.sleep(0.5)
		print ('... led off')
		GPIO.output(led_pin,GPIO.HIGH)
		time.sleep(0.5)
		
def destroy():
	GPIO.output(led.pin,GPIO.HIGH)
	GPIO.cleanup()
	
if __name__ == '__main__':
	setup()
	
	try:
		loop()
	except KeyboardInterrupt:
		destroy()

