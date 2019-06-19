from picamera.array import PiRGBArray
from picamera import PiCamera
import numpy as np
import cv2
from time import sleep

class PiCameraCV2:
   
   def __init__(self):
      self.res = (640, 480)
      self.camera = PiCamera()
      self.camera.resolution = self.res
      self.camera.framerate = 24
      self.camera.rotation = 180
      
   def __del__(self):
      self.release()

   def read(self):
      ret = False
      frame = np.empty((self.res[1] * self.res[0] * 3,), dtype=np.uint8)
      try:
         self.camera.capture(frame, "bgr")
         frame = frame.reshape((self.res[1], self.res[0], 3))
         ret = True
      except PiCameraError:
         print("PiCamera error occurs")
      finally:
         return ret, frame

   def release(self):
      self.camera.close()
      
PiCam = PiCameraCV2()
print("Warming up")
sleep(2)
print("Warmed up")
ret, frame = PiCam.read()
PiCam.release()
cv2.imshow("frame", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
print("Done")
