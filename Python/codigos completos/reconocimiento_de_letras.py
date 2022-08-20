from picamera import PiCamera
from picamera.array import PiRGBArray
import pytesseract as ocr
from time import sleep

camera = PiCamera()

camera.resolution = (640,480)
raw_capture = PiRGBArray(camera)
sleep(2)
camera.capture(raw_capture,format = 'rgb')

letra_en_foto = ocr.image_to_string(raw_capture.array)
print(letra_en_fondo)
