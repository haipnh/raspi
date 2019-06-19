import RPi.GPIO as GPIO
from time import sleep

class Servo:
   # Shared attributes for all instances 
   minDutyCycle = 2
   middleDutyCycle = 7.5
   maxDutyCycle = 12.5
   operatingDutyScale = maxDutyCycle - minDutyCycle
   # Unique attributes
   # pwm
   # currentDegree
   
   def __init__(self, pin, degree=None):
      
      GPIO.setmode(GPIO.BCM)
      GPIO.setup(pin, GPIO.OUT)
      self.pwm = GPIO.PWM(pin, 50)

      self.pwm.start(self.middleDutyCycle) # Go to 0 degree position
      sleep(0.5) # For safety
      self.currentDegree=90
      
      if degree is not None:
         self.currentDegree=degree
         self.setDegree(degree)         
         
   def __del__(self):
      self.setDegree(90)
      self.pwm.stop()
      GPIO.cleanup()

   def setDegree(self, degree):
      if degree >= 0 & degree <= 180:
         # Calculate PWM duty cycle
         if degree == 90:
            dutyCycle = self.middleDutyCycle
         else:
            dutyCycle = (degree/180) * self.operatingDutyScale + self.minDutyCycle
         
         # At 5V, 0.1s is required to rotate 60 degree
         diff = abs(degree - self.currentDegree)
         reponseTime = ((diff // 60) + 1) * 0.2

         # Perform action
         self.pwm.ChangeDutyCycle(dutyCycle)
         self.currentDegree = degree
         sleep(reponseTime)
      
##### Testing Servo class =====
         
try:
   MG90S = Servo(17, 90)
   print("Start MG90S")
   while True:
##      pass
##   while True:
      MG90S.setDegree(0)
      sleep(0.5)
      MG90S.setDegree(90)
      sleep(0.5)
      MG90S.setDegree(180)
      sleep(0.5)
      MG90S.setDegree(90)
      sleep(0.5)
except KeyboardInterrupt:
  del MG90S
  print("Stop MG90S")
      

   
    
