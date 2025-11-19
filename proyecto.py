from moduloproductos import ingresar_productos, mostrar_productos, eliminar_productos, cantidad_producto, mostrar_estante, producto_eliminado, agregar_producto
from modulopedidos import colgar_pedido, mostrar_pedidos

#Listas donde se agregaran los datos (diccionarios)
productos = []
productos_eliminados = []
pedidos = []

#Contador
numcode = 0

#Mensaje de bienvenida para el usuario
inicio = input ("""Bienvenido Usuario, gracias por usar nuestro
programa. Este está diseñado para que llevar el inventario
de tus productos no sea un dolor de cabeza :).  Aquí, podrás
agregar los productos de tu tienda y montar los pedidos. 
El programa se encargará de actualizar todo de manera automática.
Para continuar, envía cualquier caracter: """)

estado = True

#Menu donde se realizaran todas las acciones
while estado: 
    opcion = input("""(1: Agregar producto)
(2: Mostrar productos)
(3: Mostrar cantidad producto)
(4: Eliminar producto)
(5: Colgar pedido)
(6: Mostrar pedidos) 
(7: Mostrar productos en el estante)
(8: Mostrar productos eliminados)
(9: Mostrar pronóstico de la demanda del producto)
(10: Calcular el error)
(11: Agregar producto en stock)
(12: Salir)
Elija la opción (número): """)
 
    if opcion == "12": #Salir del programa
        print ("Gracias por usar nuestro sistema!!!!!!!!!!!")
        estado = False
    elif opcion == "1": #Ingresar productos
        numcode = ingresar_productos(productos, numcode)
    elif opcion == "2": #Mostrar todos los productos disponibles
        mostrar_productos (productos)
    elif opcion == "3": #Mostrar la cantidad que hay de un producto
        cantidad_producto (productos)
    elif opcion == "4": #Eliminar productos
        eliminar_productos (productos, productos_eliminados)
    elif opcion == "5": #Colgar pedidos
        colgar_pedido(pedidos, productos)
    elif opcion == "6": #Mostrar todos los pedidos
        mostrar_pedidos(pedidos)
    elif opcion == "7": #Mostrar estante
        mostrar_estante(productos)
    elif opcion == "8":
        producto_eliminado(productos_eliminados) #Mostrar los productos que se eliminan
    elif opcion == "9": 
        x = 0
    elif opcion == "10": 
        x = 0
    elif opcion == "11": 
        agregar_producto(productos)