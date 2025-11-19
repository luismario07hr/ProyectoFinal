from moduloproductos import ingresar_productos, mostras_prodcutos, eliminar_productos, cantidad_producto, mostrar_estante
from modulopedidos import colgar_pedido, mostrar_pedidos

productos = []
productos_eliminados = []
pedidos = []
numcode = 0

inicio = input ("""Bienvenido Usuario, gracias por usar nuestro
programa. Este está diseñado para que llevar el inventario
de tus productos no sea un dolor de cabeza :).  Aquí, podrás
agregar los productos de tu tienda y montar los pedidos. 
El programa se encargará de actualizar todo de manera automática.
Para continuar, envía cualquier caracter: """)

estado = True
while estado: 
    opcion = input("""(1: Agregar producto)
(2: Mostrar productos)
(3: Mostrar cantidad producto)
(4: Eliminar producto)
(5: Colgar pedido)
(6: Mostrar pedidos) 
(7: Mostrar productos en el estante)
(8: Mostrar pronóstico de la demanda del producto)
(9: Calcular el error)
(10: Salir)
Elija la opción (número): """)
 
    if opcion == "10":
        print ("Gracias por usar nuestro sistema!!!!!!!!!!!")
        estado = False
    elif opcion == "1": 
        numcode = ingresar_productos(productos, numcode)
    elif opcion == "2": 
        mostras_prodcutos (productos)
    elif opcion == "3": 
        cantidad_producto (productos)
    elif opcion == "4":
        eliminar_productos (productos, productos_eliminados)
    elif opcion == "5": 
        colgar_pedido(pedidos, productos)
    elif opcion == "6": 
        mostrar_pedidos(pedidos)
    elif opcion == "7":
        mostrar_estante(productos)
    elif opcion == "8":
        x = 0  
    elif opcion == "9": 
        x = 0