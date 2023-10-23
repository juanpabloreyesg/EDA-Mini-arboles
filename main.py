from arboles import arbol_binario

if __name__=='__main__':
    mi_arbol = arbol_binario()

    mi_arbol.agregar_elemento('E')
    
    mi_arbol.agregar_elemento('B')
    mi_arbol.agregar_elemento('C')
    mi_arbol.agregar_elemento('D')
    mi_arbol.agregar_elemento('A')
    mi_arbol.agregar_elemento('E')
    mi_arbol.agregar_elemento('F')
    mi_arbol.agregar_elemento('G')


    mi_arbol.pintar_arbol()

