# Practica1: Aplicación de filtros RGB en imágenes
# 
# A cada imagen se le va a aplicar el filtro RGB, por tanto
# Se van a generar 3 imágenes adicionales a partir de la imagen original. 
#
# Se tienen que usar 2 hilos por cada imagen original

import threading
import numpy
from PIL import Image

#imagen = Image.new('RGB', [1280, 720], (0, 0, 0))

url = "a-photo-of-a-raccoon-wearing-an-astronaut-helmet.jpg"

def imgR(url):
    imagen = Image.open(url).convert('RGB')
    imagen = numpy.array(imagen)
    value = []
    for x in imagen:
        for y in range(0, int(len(x))):
            R = int(46*numpy.log(x[y][0]+1))    # R = int(x[y][0])
            G = int(x[y][1])                    # G = int(numpy.power(x[y][2],2)/255)
            B = int(x[y][2])                    # B = int(numpy.power(x[y][1],2)/255)

            temp = [R, G, B]
            b = numpy.array(temp)
            x[y] = b
            value.append(temp)
            
    imagen = Image.fromarray(imagen)
    imagen.show()
    print("mostrando imagen con filtro rojo")

def imgG(imagen):
    imagen = Image.open(url).convert('RGB')
    imagen = numpy.array(imagen)
    value = []
    for x in imagen:
        for y in range(int(len(x))):
            R = int(x[y][0])
            G = int(46*numpy.log(x[y][0]+1))
            B = int(x[y][2])
            temp = [R, 
                    G, 
                    B]
            b = numpy.array(temp)
            x[y] = b
            value.append(temp)

            
    imagen = Image.fromarray(imagen)
    imagen.show()
    print("mostrando imagen con filtro verde")

def imgB(imagen):
    imagen = Image.open(url).convert('RGB')
    imagen = numpy.array(imagen)
    value = []
    for x in imagen:
        for y in range(int(len(x))):
            R = int(x[y][0])
            G = int(x[y][1])
            B = int(46*numpy.log(x[y][2]+1))
            temp = [R, 
                    G, 
                    B]
            b = numpy.array(temp)
            x[y] = b
            value.append(temp)
            
    imagen = Image.fromarray(imagen)
    imagen.show()
    print("mostrando imagen con filtro azul")

if __name__ == '__main__':
    hilo1 = threading.Thread(target=imgR, args=[url])    
    hilo2 = threading.Thread(target=imgB, args=[url])
    
    hilo1.start()
    hilo2.start()
    
    hilo1.join()
    hilo2.join()
