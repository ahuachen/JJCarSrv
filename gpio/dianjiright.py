#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

#
# 红板 L298N电机驱动板模块 
#IN1 IN2输入PWM信号驱动电机1的转速和方向
#IN3 IN4输入PWM信号驱动电机2的转速和方向
#
IN1=11
IN2=12
IN3=13
IN4=15

if __name__ == '__main__':
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(IN1, GPIO.OUT)
    GPIO.setup(IN2, GPIO.OUT)
    GPIO.setup(IN3, GPIO.OUT)
    GPIO.setup(IN4, GPIO.OUT)
    GPIO.output(IN1, GPIO.LOW) 
    GPIO.output(IN2, GPIO.HIGH) 
    GPIO.output(IN3, GPIO.HIGH) 
    GPIO.output(IN4, GPIO.LOW) 
    #time.sleep(1)
    #GPIO.cleanup()

