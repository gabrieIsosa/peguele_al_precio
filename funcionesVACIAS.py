from principal import *
from configuracion import *
import random
import math
from extras import *
from button import Button

# lee el archivo y carga en la lista lista_producto todas las palabras
def lectura():
    lista_productos = []
    with open("productos.txt", "r") as f:
        for linea in f:
            partes = linea.split(",")
            if len(partes) == 3:
                nombre, precio_economico, precio_premium = partes
                lista_productos.append([nombre, int(precio_economico), int(precio_premium)])
    return lista_productos


#De la lista de productos elige uno al azar y devuelve una lista de 3 elementos, el primero el nombre del producto , el segundo si es economico
#o premium y el tercero el precio.
def buscar_producto(lista_productos):
    producto=[]
    c1=0
    rango=len(lista_productos)-1
    indiceprod=random.randint(0,rango)
    eleccion=random.randint(1,2)
    for x in range(len(lista_productos)):
        if(x==indiceprod):
            for elemento in lista_productos[x]:
                if (c1==0):
                    producto.append(elemento)
                if(c1==eleccion):
                    if(eleccion==1):
                        producto.append("(economico)")
                        producto.append(elemento)
                    elif(eleccion==2):
                        producto.append("(premium)")
                        producto.append(elemento)
                c1=c1+1
        c1=0
    return(producto)

#Elige el producto. Debe tener al menos dos productos con un valor similar
def dameProducto(lista_productos, margen):
    c1=0
    c2=0
    prod=buscar_producto(lista_productos)
    productoscomparados=[]
    nombre=prod[0]
    precio=prod[2]
    for sub_lista in lista_productos:
        for elem in sub_lista:
            if(type(elem) == str and elem!=nombre):
                nombreprod=elem
                c2=0
            elif(type(elem) == str and elem==nombre):
                nombreprod=elem
                c2=1
            elif(type(elem)!=str):
                #print(elem)
                if(elem>precio):
                    diferencia=elem-precio
                    if (diferencia<=margen):
                        c1=c1+1
                        if(nombreprod not in productoscomparados and c2!=1):
                            productoscomparados.append(nombreprod)
                elif(precio>elem):
                    diferencia=precio-elem
                    if(diferencia<=margen):
                        c1=c1+1
                        if(nombreprod not in productoscomparados and c2!=1):
                            productoscomparados.append(nombreprod)
                else:
                    c1=c1+1
        #print(c1)
        #print(productoscomparados)
        #print(prod)
        if(len(productoscomparados)>=1):
            return(prod,productoscomparados)

    return(0)


##lista=lectura()
##listaproducto=0
##listaproducto=dameProducto(lista,1000)
###print(listaproducto)
##producto=listaproducto[0]
###print(producto)


def elegirProductoGanador(producto,nombreprodacertado,margen):
    c1=0
    c2=0
    lista_productos=lectura()
    precio=producto[2]
    productoganador=[]
    productoganador.append(nombreprodacertado)
    for sub_lista in lista_productos:
        for elem in sub_lista:
            if(type(elem) == str and elem==nombreprodacertado):
                c1=1
            elif(type(elem)!=str):
                if(c1==1):
                    if(precio>elem):
                        diferencia=precio-elem
                        if(diferencia<=margen and c2==0):
                            productoganador.append("(economico)")
                            productoganador.append(elem)
                            return(productoganador)
                        elif(diferencia<=margen and c2==1):
                            productoganador.append("(premium)")
                            productoganador.append(elem)
                            return(productoganador)
                    elif(elem>precio):
                        diferencia=elem-precio
                        if(diferencia<=margen and c2==0):
                            productoganador.append("(economico)")
                            productoganador.append(elem)
                            return(productoganador)
                        elif(diferencia<=margen and c2==1):
                            productoganador.append("(premium)")
                            productoganador.append(elem)
                            return(productoganador)
                    c2=c2+1




#Devuelve True si existe el precio recibido como parametro aparece al menos 3 veces. Debe considerar el Margen.
##def esUnPrecioValido(precio, lista_productos, margen):
##    return True

# Busca el precio del producto_principal y el precio del producto_candidato, si son iguales o dentro
# del margen, entonces es valido y suma a la canasta el valor del producto. No suma si eligió directamente
#el producto
def procesar(producto_principal, producto_candidato, margen,eleccion):
    precioprodprincipal=producto_principal[2]
    precioprodcandidato=producto_candidato[2]
    nombreprodprincipal=producto_principal[0]
    nombreprodcandidato=producto_candidato[0]
    #print(precioprodprincipal)
    #print(precioprodcandidato)
    if(nombreprodprincipal==nombreprodcandidato):
        return(0,0)
    elif(precioprodprincipal>precioprodcandidato):
        diferencia=precioprodprincipal-precioprodcandidato
        if(diferencia<=margen):
            if(eleccion=="f"):
                return(precioprodcandidato,1)
            elif(eleccion=="m"):
                return(precioprodcandidato,0)
            elif(eleccion=="d"):
                return(precioprodcandidato,5)
        else:
            if(eleccion=="d"):
                return(0,-5)
            else:
                return(0,0)

    elif(precioprodcandidato>precioprodprincipal):
        diferencia=precioprodcandidato-precioprodprincipal
        if(diferencia<=margen):
            if(eleccion=="f"):
                return(precioprodcandidato,1)
            elif(eleccion=="m"):
                return(precioprodcandidato,0)
            elif(eleccion=="d"):
                return(precioprodcandidato,5)
        else:
            if(eleccion=="d"):
                return(0,-5)
            else:
                return(0,0)
    elif(precioprodcandidato==precioprodprincipal):
        if(eleccion=="f"):
            return(precioprodcandidato,1)
        elif(eleccion=="d"):
            return(precioprodcandidato,5)
        elif(eleccion=="m"):
            return(precioprodcandidato,0)

#Elegimos productos aleatorios, garantizando que al menos 2 tengan el mismo precio.
#De manera aleatoria se debera tomar el valor economico o el valor premium. Agregar al nombre '(economico)' o '(premium)'
#para que sea mostrado en pantalla.
def dameProductosAleatorios(productolista, lista_productos, margen,cantidad):
    c1=0
    productos_seleccionados=[]
    productosnodisponibles=[]
    productoprincipal=productolista[0]
    productoacertado=productolista[1]
    nombreprodacertado=productoacertado[0]
    nombreprodprincipal=productoprincipal[0]
    #print(nombreprodprincipal)
    #print(nombreprodacertado)
    productosnodisponibles.append(nombreprodacertado)
    productosnodisponibles.append(nombreprodprincipal)
    productoganador=elegirProductoGanador(productoprincipal,nombreprodacertado,margen)
    productos_seleccionados.append(productoprincipal)
    posicion=random.randint(0,5)
    #print(posicion)
    while len(productos_seleccionados)!=cantidad:
        #print(c1)
        productorelleno=buscar_producto(lista_productos)
        nombreprodrelleno=productorelleno[0]
        if(c1==posicion):
            c1=c1+1
            productos_seleccionados.append(productoganador)
        elif(nombreprodrelleno not in productosnodisponibles):
            productos_seleccionados.append(productorelleno)
            productosnodisponibles.append(nombreprodrelleno)
            c1=c1+1
    #print(productos_seleccionados)
    return(productos_seleccionados)



#print(dameProductosAleatorios(listaproducto,lista,1000))
