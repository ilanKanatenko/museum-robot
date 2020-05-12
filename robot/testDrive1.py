import RPi.GPIO as GPIO          
from time import sleep




#right wheel
in1 = 24
in2 = 23
en1 = 25

#left wheel
in3 = 27
in4 = 17
en2 = 22

temp1=1

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en1,GPIO.OUT)

GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(en2,GPIO.OUT)

p1=GPIO.PWM(en1,1000)
p2=GPIO.PWM(en2,1000)



def forward(time_to_run,p1_duty,p2_duty):
    
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)
    p1.start(p1_duty)
    p2.start(p2_duty)
    sleep(time_to_run)
    p1.stop()
    p2.stop()





def backward(time_to_run,p1_duty,p2_duty):
    
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in1,GPIO.HIGH)
    
    GPIO.output(in4,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
#    p1.ChangeDutyCycle(69.3)
#    p2.ChangeDutyCycle(70)
    p1.start(p1_duty)
    p2.start(p2_duty)
    sleep(time_to_run)
    p1.stop()
    p2.stop()
    


def degree_to_time(degree):
    
    time=degree
    
    return time
    


def rotate_right(degree):
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in1,GPIO.HIGH)
    p1.start(100)
    time=degree_to_time(degree)
    sleep(time)
    p1.stop()
    
    

def rotate_left(degree):
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    p1.start(100)
    time=degree_to_time(degree)
    sleep(time)
    p1.stop()   




# forward(8,68.2,70)
# backward(8,67,71.5)
rotate_left(0.50)


GPIO.cleanup()


