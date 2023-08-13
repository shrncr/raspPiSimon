import RPi.GPIO as GPIO
from time import sleep
from random import *
import sys
#import pygame

#pygame.init()

leds = [17,16,12,5]

switches = [18,19,20,21]

DEBUG = False

GPIO.setmode(GPIO.BCM)

GPIO.setup(leds, GPIO.OUT)

GPIO.setup(switches, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def all_on():
    for i in leds:
        GPIO.output(leds,True)
def all_off():
    for i in leds:
        GPIO.output(leds,False)
#all_on()
#sleep(1)
#all_off()

def lose():
    for i in range(0,4):
        all_on()
        sleep(.5)
        all_off()
        sleep(.5)
seq = []

seq.append(randint(0,3))
seq.append(randint(0,3))
#print(seq)

print("Welcome to Simon!")
print("Try to play the sequence back by pressing the switches.")
print("press Ctrl+C to exit...")

score = 0
while(True):
    seq.append(randint(0,3))
    if (DEBUG):
        if len(seq)  >=3:
            print()
        print("seq={}".format(seq))
    for s in seq:
        #if score < 15:
          #  PLAY THE SOUND CODE
        GPIO.output(leds[s], True)
        if score >= 13:
            sleep(.6)
        elif score >=10:
            sleep(.7)
        elif score >=10:
            sleep(.8)
        elif score >=10:
            sleep(.9)
        else:
            sleep(1)
        GPIO.output(leds[s], False)
        if score >= 13:
            sleep(.15)
        elif score >=10:
            sleep(.25)
        elif score >=10:
            sleep(.3)
        elif score >=10:
            sleep(.4)
        else:
            sleep(.5)
    switch_count = 0
    while (switch_count < len(seq)):
        pressed = False
        while (not pressed):
            #print("hoot")
            #print(len(switches))
            for i in range(0,len(switches)):
                #print(i)
                if GPIO.input(switches[i]) == True:
                    val = i
                    #print("i pressed")
                    pressed = True
                    if (DEBUG):
                        print(val)
                    GPIO.output(leds[val], True)
            #SOUNDS HERE IF I HAVE TO
                    sleep(1)
                    GPIO.output(leds[val], False)
                    sleep(.25)
                    if (val != seq[switch_count]):
                        lose()
                        if len(seq) == 3:
                            print("You made it to a sequence of 0!")
                        else:
                            print("You made it to a sequence of " + str(len(seq)))
                        GPIO.cleanup()
                        exit(0)
                    switch_count += 1
        score+=1
    #try:
    #except KeyboardInterrupt:
        #GPIO.cleanup()
#all_on()
