from moduloproductos import ingresar_productos, mostras_prodcutos, eliminar_productos

productos = []
productos_eliminados = []

numcode = 1

estado = True
while estado: 
    opcion = input("""(1: Agregar producto)
(2: Mostrar productos)
(3: Cambiar cantidad producto)
(4: Eliminar producto)
(5: Pronóstico de demanda)
(6: Calcular el error)
(7: Salir)
Elija la opción: """)
    
    if opcion == "7": 
        estado = False
    elif opcion == "1": 
        ingresar_productos(productos, numcode)
    elif opcion == "2": 
        mostras_prodcutos (productos)
    elif opcion == "3": 
        eliminar_productos (productos, productos_eliminados)
    elif opcion == "4": 
        x = 0
    elif opcion == "5": 
        x = 0
    elif opcion == "6": 
        x = 0