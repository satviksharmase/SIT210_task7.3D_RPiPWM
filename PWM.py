import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG = 18
ECHO = 24
buzzer = 3
led = 2

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(led,GPIO.OUT)
GPIO.setup(buzzer,GPIO.OUT)

L1=GPIO.PWM(2,20)
L2=GPIO.PWM(3,20)


try:
    while True:
        GPIO.output(TRIG,False)
        time.sleep(1)
        GPIO.output(TRIG,True)
        time.sleep(0.01)
        GPIO.output(TRIG,False)
        
        while GPIO.input(ECHO)==0:
            pulse_start=time.time()
            
        while GPIO.input(ECHO)==1:
            pulse_end=time.time()
            
        pulse_duration=pulse_end - pulse_start
        
        distance=pulse_duration*11150
        
        distance=round(distance,2)
        
        L1.start(0)
        L2.start(0)
        
        if distance>50:
            L1.stop()
            L2.stop()
            
        elif 40<distance<50:
            L1.ChangeDutyCycle(20)
            L2.ChangeDutyCycle(20)
        
        elif 30<distance<40:
            L1.ChangeDutyCycle(40)
            L2.ChangeDutyCycle(40)
        
        elif 20<distance<30:
            L1.ChangeDutyCycle(60)
            L2.ChangeDutyCycle(60)
            
        elif 10<distance<20:
            L1.ChangeDutyCycle(80)
            L2.ChangeDutyCycle(80)
            
        else:
            L1.ChangeDutyCycle(100)
            L2.ChangeDutyCycle(100)
            
except KeyboardInterrupt:
    GPIO.cleanup()
        
        
    
