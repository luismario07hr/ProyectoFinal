from moduloproductos import ingresar_productos, mostras_prodcutos, eliminar_productos, cantidad_producto 
from pedidos import colgar_pedido

productos = []
productos_eliminados = []
pedidos = []

numcode = 1

estado = True
while estado: 
    opcion = input("""(1: Agregar producto)
(2: Mostrar productos)
(3: Mostrar cantidad producto)
(4: Eliminar producto)
(5: Colgar pedido)
(6: Mostrar pedidos)
(7: Pronóstico de demanda)
(8: Calcular el error)
(9: Salir)
Elija la opción: """)
    
    if opcion == "7": 
        estado = False
    elif opcion == "1": 
        ingresar_productos(productos, numcode)
    elif opcion == "2": 
        mostras_prodcutos (productos)
    elif opcion == "3": 
        cantidad_producto (productos)
    elif opcion == "4": 
        eliminar_productos (productos, productos_eliminados)
    elif opcion == "5": 
        colgar_pedido(pedidos, productos)
    elif opcion == "6": 
        x = 0
    elif opcion == "7":
        x = 0
    elif opcion == "8":
        x = 0
    elif opcion == "9":
        x = 0
    