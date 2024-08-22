# Script untuk autentikasi dan buka pintu raspberry pi

# Script ini ditempatkan di tiap raspberry pi untuk autentikasi input dari user
# Autentikasi dilakukan dengan ambil data dari server lokal

import RPi.GPIO as GPIO
import time
import requests
import os

from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv('BASE_URL')
VEFIRY_URL = BASE_URL + os.getenv('VERIFY_URL')

while True:

	qrcode = input('QRCode:')

	data = {
		"code": qrcode
	}

	response = None

	try:
		response = requests.post(VEFIRY_URL, json=data)
	except Exception as e:
		print('Cannot connect with server')
		continue

	if response.status_code == 200:

		print('QR Authenticated')
		Proses buka pintu
		GPIO.setmode(GPIO.BCM)
		RELAIS_1_GPIO = 15;

		GPIO.setup(RELAIS_1_GPIO,GPIO.OUT) 
		GPIO.output (RELAIS_1_GPIO, GPIO.HIGH) # out 
		GP10.output (RELAIS_1_GPIO, GPIO.LOW) # on

		time.sleep(3)

		GPIO.output (RELAIS_1_GPIO, GPIO.HIGH)

		GPIO.cleanup()
		End proses buka pintu

	elif response.status_code == 404:
		print("QR doesn't exist")

	else:
		print("Request failed with status code:", response.status_code)
		
else:
	print('finish')
GPIO.cleanup();