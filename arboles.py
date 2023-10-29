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

@dataclass(repr=True)
class Node:
    data: int
    hijo_izquierdo: Optional["Node"] = None
    hijo_derecho: Optional["Node"] = None
    rojo: bool = True

    def __str__(self):
        string = f"<data={self.data}, rojo={self.rojo}"
        if self.hijo_izquierdo is not None:
            string += f"|hi:{self.hijo_izquierdo}"
        if self.hijo_derecho is not None:
            string += f"|hd:{self.hijo_derecho}"
        return string+">"


@dataclass(repr=True)
class arbol_rojonegro:    

    raiz: Node = None

    def agregar_elemento(self, elemento):
        self.raiz = self.__insertar_elemento(self.raiz, elemento)
        self.raiz.rojo = False

    def dar_altura(self):
        return self.__dar_altura(self.raiz)

    def __dar_altura(self, nodo)->None:

        if nodo is None:
            return 0
        return 1 + max(self.__dar_altura(nodo.hijo_izquierdo), self.__dar_altura(nodo.hijo_derecho))

    def __es_rojo(self, nodo):
        if nodo is None or not nodo.rojo:
            return False
        return True
    
    def __rotacion_izquierda(self, nodo):
        #TODO
        pass

    def __rotacion_derecha(self, nodo):
        #TODO
        pass
    
    def __invertir_colores(self, nodo):
        #TODO
        pass

    def __balancear(self, nodo)->None:
        
        if self.__es_rojo(nodo.hijo_derecho) and not self.__es_rojo(nodo.hijo_izquierdo):
            nodo = self.__rotacion_izquierda(nodo)
        
        if self.__es_rojo(nodo.hijo_izquierdo) and self.__es_rojo(nodo.hijo_izquierdo.hijo_izquierdo):
            nodo = self.__rotacion_derecha(nodo)
        
        if self.__es_rojo(nodo.hijo_izquierdo) and self.__es_rojo(nodo.hijo_derecho):
            nodo = self.__invertir_colores(nodo)
        
        return nodo
    
    def __insertar_elemento(self, nodo, elemento)->None:
        if nodo is None:
            return Node(elemento)
        elif elemento < nodo.data:
            nodo.hijo_izquierdo = self.__insertar_elemento(nodo.hijo_izquierdo, elemento)
        else:
            nodo.hijo_derecho = self.__insertar_elemento(nodo.hijo_derecho, elemento)
        nodo = self.__balancear(nodo)
        return nodo

    def __str__(self):
        return str(self.raiz)
    

    def __pintar_nodo(self, nodo, x, y, xshift=150, yshift=70, nivel=1):
        if nodo is not None:
                
            xshift/=nivel
            
            penup()
            goto(x,y)
            pendown()

            color('black')
            if nodo.rojo:
                fillcolor('red')
            else:
                fillcolor('Black')
            begin_fill()
            circle(10)
            end_fill()       
            
            penup()
            goto(x,y)
            pendown()

            color('white')
            write(nodo.data, font=('Arial',8,'bold'), align='center')

            if self.__es_rojo(nodo.hijo_izquierdo):
                color('red')
            else:
                color('black')

            goto(x-xshift, y-yshift)
            self.__pintar_nodo(nodo.hijo_izquierdo, x-xshift, y-yshift, nivel=nivel+3)

            penup()
            goto(x,y)
            pendown()

            if self.__es_rojo(nodo.hijo_derecho):
                color('red')
            else:
                color('black')
            
            goto(x+xshift, y-yshift)
            self.__pintar_nodo(nodo.hijo_derecho, x+xshift, y-yshift, nivel=nivel+3)
        
    def pintar_arbol(self):
        hideturtle()
        tracer(0, 0) 
        setup(700, self.dar_altura()*100)
        self.__pintar_nodo(self.raiz, 0, self.dar_altura()*40)
        penup()
        goto(0,0)
        pendown()
        exitonclick()