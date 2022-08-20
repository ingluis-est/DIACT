from picamera import PiCamera              #importacion de libreria picamera
from time import sleep                     #importacion de libreria de tiempo (receso o espera)
camera=PiCamera()                          #asociacion de una libreria a una variable
def grabar_video(nombre):                  #definicion de la funcion captura de foto
    camera.resolution=(640,480)            #determinar resolucion de la imagenes (ancho*alto)
    video_path='/home/pi/Videos/{0}.h264'.format(nombre)  #ubicacion de almacenamiento
    camera.start_recording(video_path)     #inicio de carga
    sleep(10)                              #tiempo de duracion de la grabacion (10 segundos)
    camera.stop_recording()                #detiene la grabacion
    
grabar_video("grabar") #ejecucion de la funcion

#Readme
# Variables video_path, almacena la ubicacion donde se guardara la imagen.