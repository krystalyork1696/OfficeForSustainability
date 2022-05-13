import numpy as np
import sys
import matplotlib.pyplot as plt
import scipy.special
import math
import cv2
import spidev
import os
from gpiozero import DigitalInputDevice
import busio
import digitalio
import board
import time
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import glob
import RPi.GPIO as GPIO

#first program - moisture

d0_input = DigitalInputDevice(4)

while True:
if (not d0_input.value):
    print('Moisture threshold reached!!!')
else:
    print('You need to water your plant')
    time.sleep(2)

##second program - moisture

# create the spi bus
#spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# create the cs (chip select)
#cs = digitalio.DigitalInOut(board.CE0)

# create the mcp object
#mcp = MCP.MCP3008(spi, cs)

# create an analog input channel on pin 0
#chan = AnalogIn(mcp, MCP.P0)

#while True:
#    print('Raw ADC Value: ', chan.value)
#    print('ADC Voltage: ' + str(chan.voltage) + 'V')
#    time.sleep(2)

##third program - Moisture

#delay = 0.2

#spi = spidev.SpiDev()
#spi.open(0,0)

#def readChannel(channel):
 # val = spi.xfer2([1,(8+channel)<<4,0])
  #data = ((val[1]&3) << 8) + val[2]
#  return data

#if __name__ == "__main__":
 # try:
#    while True:
#      val = readChannel(0)
#      if (val != 0):
#        print(val)
#      time.sleep(delay)

##first program - temperature

#base_dir = '/sys/bus/w1/devices/'
#device_folder = glob.glob(base_dir + '28*')[0]
#device_file = device_folder + '/w1_slave'

#def read_temp_raw():
#    f = open(device_file, 'r')
#    lines = f.readlines()
#    f.close()
#    return lines

#def read_temp():
#    lines = read_temp_raw()
#    while lines[0].strip()[-3:] != 'YES':
#        time.sleep(0.2)
#        lines = read_temp_raw()
#    equals_pos = lines[1].find('t=')
#    if equals_pos != -1:
#        temp_string = lines[1][equals_pos+2:]
#        temp_c = float(temp_string) / 1000.0
#        temp_f = temp_c * 9.0 / 5.0 + 32.0
#        return temp_c, temp_f

#while True:
#    print(read_temp())
#    time.sleep(1) #reads temp every second

##first program - camera with LED turning on

#FRAMES = 2000
#TIMEBETWEEN = 3600
#GPIO.setmode(GPIO.BOARD)
#GPIO.setwarnings(False)
#ledPin = 12 #change number to whatever pin
#GPIO.setup(ledPin, GPIO.OUT) 

#frameCount = 0
#while frameCount < FRAMES:
#    GPIO.output(ledPin,GPIO.HIGH)
#    imageNumber = str(frameCount).zfill(7)
#    os.system("raspistill -o image%s.jpg"%(imageNumber))
#    frameCount += 1
#    time.sleep(6)          #is this line needed?
#    GPIO.output(ledPin,GPIO.LOW)
#    time.sleep(TIMEBETWEEN - 6) #Takes roughly 6 seconds to take a picture
