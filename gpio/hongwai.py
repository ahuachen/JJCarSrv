#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|-|S|p|y|.|c|o|.|u|k|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#
# hongwai.py
# Detect movement using a PIR module
#
# Author : ahua
# Date   : 2015/06/20


# Import required Python libraries
import RPi.GPIO as GPIO
import time


# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BOARD)

# Define GPIO to use on Pi
GPIO_PIR=13
GPIO_LED=7

print "PIR Module Test (CTRL-C to exit)"

# Set pin as input
GPIO.setup(GPIO_PIR,GPIO.IN)      # Echo
GPIO.setup(GPIO_LED,GPIO.OUT)     # LED
Current_State  = 0
Previous_State = 0

try:
  print "Waiting for PIR to settle ..."
  # Loop until PIR output is 0
  looptime = 1
  while GPIO.input(GPIO_PIR)==1:
    Current_State  = 0    
    if looptime % 15 == 0:
         print "0"
    else:
         print "0",
    looptime+=1
    time.sleep(1)
  print "  Ready after ", looptime, " second"     
    
  # Loop until users quits with CTRL-C
  while True :
    # Read PIR state
    Current_State = GPIO.input(GPIO_PIR)
    if Current_State==1 and Previous_State==0:
      # PIR is triggered
      print time.ctime(), "  Motion detected!"
      GPIO.output(GPIO_LED, GPIO.HIGH)
      # Record previous state
      Previous_State=1
    elif Current_State==0 and Previous_State==1:
      # PIR has returned to ready state
      print time.ctime(), "  Ready"
      GPIO.output(GPIO_LED, GPIO.LOW)
      Previous_State=0
      
    # Wait for 10 milliseconds
    time.sleep(0.01)      

except KeyboardInterrupt:
  print "  Quit" 
  # Reset GPIO settings
  GPIO.cleanup()
