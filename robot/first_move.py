import RPi.GPIO as g
import gpiozero
import time

robot = gpiozero.Robot(left=(17,18), right=(27,22))
g.setmode(g.BOARD)
g.setup(17,g.OUT)
g.setup(18,g.OUT)
g.setup(27,g.OUT)
g.setup(22,g.OUT)
pmw = g.PWM(17,100)
for i in range(4):
	
	robot.forward(0.3)
	time.sleep(4)
	#robot.right()
	#time.sleep(0.25)
print("worked")
