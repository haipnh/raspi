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

# ===== HOW TO USE ===== 

# Create PiCameraCV2 object      
PiCam = PiCameraCV2()

# Warming up PiCamera
print("Warming up")
sleep(2)
print("Warmed up")

# Capture the frame
ret, frame = PiCam.read()

# If capture successfully
if ret:
   cv2.imshow("PiCameraCV2", frame)

# Release PiCamera
PiCam.release()

# Press any key to close display window
cv2.waitKey(0)
cv2.destroyAllWindows()
print("Done")
