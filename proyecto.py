from moduloproductos import ingresar_productos

productos = []
productos_eliminados = []

numcode = 1

estado = True
while True: 
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
        ingresar_productos(productos)
    elif opcion == "2": 
        print (productos)
    elif opcion == "3": 
        x = 0 
    elif opcion == "4": 
        x = 0
    elif opcion == "5": 
        x = 0
    elif opcion == "6": 
        x = 0