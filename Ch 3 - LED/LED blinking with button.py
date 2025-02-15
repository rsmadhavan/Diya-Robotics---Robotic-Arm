#Importing function Pin from package machine for manipulating Pins on board
from machine import Pin

#Declaring object button for button
#Button is connected to Pin 10
button=(Pin(10,Pin.IN))

#Declaring object p2 for LED
#Onboard LED is connected to Pin 2
p2=Pin(2,Pin.OUT)

#To run loop infinitely
while True:
    #If button is pressed....
    while(button.value() == 1):
        #...Turn on LED
        p2.on()
    #Turn off LED
    p2.off()
