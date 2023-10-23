from dataclasses import dataclass, field
from typing import List, Optional
from turtle import *


@dataclass(repr=True)
class arbol_binario:

    elemento: int = None
    hijo_izquierdo: List['arbol_binario']= None
    hijo_derecho: List['arbol_binario']= None

    def agregar_elemento(self, elemento)->None:
        if self.elemento is None:
            self.elemento = elemento
        elif self.elemento > elemento:
            if self.hijo_izquierdo is None:
                self.hijo_izquierdo = arbol_binario(elemento)
            else:
                self.hijo_izquierdo.agregar_elemento(elemento)
        else:
            if self.hijo_derecho is None:
                self.hijo_derecho = arbol_binario(elemento)
            else:
                self.hijo_derecho.agregar_elemento(elemento)

    def dar_altura(self):
        #TODO
        pass
  

    def __str__(self) -> str:
        cadena = f"<e:{self.elemento}"""
        if self.hijo_izquierdo is not None:
            cadena+=f"|hi:{self.hijo_izquierdo}"
        if self.hijo_derecho is not None:
            cadena+=f"|hd:{self.hijo_derecho}"
        return cadena+">"
    
    def __pintar_nodo(self, x, y, xshift=150, yshift=70, nivel=1):
       
            
        xshift/=nivel
        
        penup()
        goto(x,y)
        pendown()

        color('black')

        fillcolor('Black')
        begin_fill()
        circle(10)
        end_fill()       
        
        penup()
        goto(x,y)
        pendown()

        color('white')
        write(self.elemento, font=('Arial',8,'bold'), align='center')
        color('black')

        if self.hijo_izquierdo is not None:
            goto(x-xshift, y-yshift)
            self.hijo_izquierdo.__pintar_nodo(x-xshift, y-yshift, nivel=nivel+3)

        penup()
        goto(x,y)
        pendown()

        if self.hijo_derecho is not None:
            goto(x+xshift, y-yshift)
            self.hijo_derecho.__pintar_nodo( x+xshift, y-yshift, nivel=nivel+3)
        
    def pintar_arbol(self):
        hideturtle()
        tracer(0, 0) 
        print(self.dar_altura())
        setup(700, self.dar_altura()*100)
        self.__pintar_nodo(0, self.dar_altura()*40)
        penup()
        goto(0,0)
        pendown()
        exitonclick()