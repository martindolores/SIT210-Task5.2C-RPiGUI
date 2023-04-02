from tkinter import *
import tkinter.font
import RPi.GPIO as GPIO

##HARDWARE
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.output(12, GPIO.LOW)
GPIO.output(16, GPIO.LOW)
GPIO.output(18, GPIO.LOW)

##GUI DEFINITIONS
win = Tk()
win.title("LED Toggler")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

##VARIABLES
pinList = []
pinList.append(12)
pinList.append(16)
pinList.append(18)

radioVariable = IntVar()
radioVariable.set(0)

##EVENT METHODS
def ledToggle(pin):
   if GPIO.input(pin) == GPIO.LOW:
      GPIO.output(pin, GPIO.HIGH)
   for otherPin in pinList:
      if GPIO.input(otherPin) == GPIO.HIGH and otherPin != pin:
         GPIO.output(otherPin, GPIO.LOW)

def close():
   GPIO.cleanup()
   win.destroy()

##WIDGETS
ledButton = Radiobutton(win, text = "Red", font = myFont, command = lambda:ledToggle(12), variable = radioVariable, value = 12, bg = 'bisque2', height = 1, width = 24)
ledButton2 = Radiobutton(win, text = "Green", font = myFont, command = lambda:ledToggle(18), bg = 'bisque2',variable = radioVariable, value = 18, height = 1, width = 24)
ledButton3 = Radiobutton(win, text = "Blue", font = myFont, command = lambda:ledToggle(16), bg = 'bisque2', variable = radioVariable, value = 16, height = 1, width = 24)
closeButton = Button(win, text = "Close", font = myFont, command = close, bg = 'bisque2', height = 1, width = 24)

ledButton.pack()
ledButton2.pack()
ledButton3.pack()
closeButton.pack()

win.mainloop()

