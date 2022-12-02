import RPi.GPIO as GPIO
import time;

while True:

	qrcode = input('QRCode:')

	if qrcode == 'reliance27':

		GPIO.setmode(GPIO.BCM)
		RELAIS_1_GPIO = 15;

		GPIO.setup(RELAIS_1_GPIO,GPIO.OUT) 
		GPIO.output (RELAIS_1_GPIO, GPIO.HIGH) # out 
		GP10.output (RELAIS_1_GPIO, GPIO.LOW) # on

		time.sleep(3)

		GPIO.output (RELAIS_1_GPIO, GPIO.HIGH)

		GPIO.cleanup()
	else:
		print('QR doesnt exists')
else:
	print('finish')
GPIO.cleanup();