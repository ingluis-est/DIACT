from picamera import PiCamera
from PIL import Image
import zbarlight
from time import sleep

camera = PiCamera()

camera.resolution = (640,480)
sleep(2)
img_path = '/home/pi/Pictures/qr.jpg'
camera.capture(img_path)

image_file = open(img_path,'rb')
image = Image.open(image_file)
image.load()

codigo_en_qr = zbarlight.scan_codes(['qrcode'],image)
print(codigo_en_qr)