from picamera import PiCamera            #importacion de libreria picamera
from time import sleep                   #importacion de libreria de tiempo (receso o espera)
camera=PiCamera()                        #asociacion de una libreria a una variable
camera.resolution=(640,480)              #determinar resolucion de la imagenes (ancho*alto)
sleep(2)                                 #tiempo para que la camara tome la foto (2 segundos)
img_path='/home/pi/Pictures/captura.jpg' #ubicacion de almacenamiento
camera.capture(img_path)                 #realiza la captura de la imagen