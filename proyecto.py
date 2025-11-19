from moduloproductos import ingresar_productos, mostras_prodcutos, eliminar_productos, cantidad_producto 
from modulopedidos import colgar_pedido #, mostrar_pedidos
from modulopronosticos import ingresar_datos_mensuales, calcular_pronosticos, calcular_error_modelo

productos = []
productos_eliminados = []
pedidos = []
numcode = 0

# Diccionario para guardar datos del pronóstico (demandas, n, alpha)
datos_pronostico = {
    "demandas": [],
    "n": 0,
    "alpha": 0.0,
    "listo_para_error": False
}

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
    
    if opcion == "9":
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
    # Sub-menú para elegir entre datos nuevos o anteriores 
        print("1. Ingresar nuevos datos históricos")
        print("2. Usar datos existentes para calcular")
        sub_opcion = input("Seleccione (1-2): ")
        
        if sub_opcion == "1":
            ingresar_datos_mensuales(datos_pronostico)
            calcular_pronosticos(datos_pronostico)
        elif sub_opcion == "2":
            calcular_pronosticos(datos_pronostico)
        else: 
            print ("Opción no válida, intente de nuevo pls")
            
    elif opcion == "8":
        calcular_error_modelo(datos_pronostico)
        
    pausa = input ("Preione enter para continuar. . . ")