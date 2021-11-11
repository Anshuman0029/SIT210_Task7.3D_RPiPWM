import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.IN)
GPIO.setup(21, GPIO.OUT)

TRIGGER = 16
ECHO = 20
LED = 21

pwm = GPIO.PWM(21, 100)                  # initializing PWM for the pwmPin with 100 Hz frequency
pwm.start(100)

def distance():
    GPIO.output(TRIGGER, True)
    
    time.sleep(0.00001)
    GPIO.output(TRIGGER, False)

    start_time = time.time()
    stop_time  = time.time()

    while GPIO.input(ECHO) == 0:
        start_time = time.time()
    
    while GPIO.input(ECHO) == 1:
        stop_time = time.time()

    time_elapsed = stop_time - start_time
    
    distance = (time_elapsed * 34300) / 2
    
    return distance

def Set_Dutycycle( percent):
    pwm.ChangeDutyCycle(percent)

try: 
  while True:
       measured_distance = distance()
       print(measured_distance)
       if(measured_distance > 30):
          Set_Dutycycle(25)
          time.sleep(1)
       elif(measured_distance > 20 and measured_distance <30):
          Set_Dutycycle(50)
          time.sleep(1)
       elif(measured_distance > 10 and measured_distance <20):
          Set_Dutycycle(75) 
          time.sleep(1)
       elif(measured_distance < 10):
          Set_Dutycycle(100)
          time.sleep(1)
       else:
          Set_Dutycycle(20)
          time.sleep(1)


except KeyboardInterrupt:
       print("Finish")
