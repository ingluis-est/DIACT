from picamera import PiCamera            #importacion de libreria picamera
from time import sleep                   #importacion de libreria de tiempo (receso o espera)
camera=PiCamera()                        #asociacion de una libreria a una variable
camera.resolution=(640,480)              #determinar resolucion de la imagenes (ancho*alt)
video_path='/home/pi/Videos/video.h264'  #ubicacion de almacenamiento
camera.start_recording(video_path)       #inicio de carga
sleep(10)                                #tiempo de duracion de la grabacion (10 segundos)
camera.stop_recording()                  #detiene la grabacion
