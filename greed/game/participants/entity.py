# entity: posee icono(texto), tamaño, color, posicion y velocidad. 

import raylib as ray
from raylib import colors
import random

class entity():

    def __init__(self):
        self._posX=random(0 , 1200)
        self._posY=random(0 , 1200)
        self._width=0
        self._height=0
        self._color=colors



    def ICONO(self):

        self._width=random(1,10)

        self._height=random(1,5)

        get_gema=ray.DrawRectangle(self.posX, self.posY, self._width, self._height,random.choice(colors))

        get_roca=ray.DrawCircleLines(self.posX, self.posY, 3,14, colors.GRAY); 
        #me falto la parte de la velocidad que no supe como hacerlo
