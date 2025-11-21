from modulopronosticos import ingresar_datos_mensuales, calcular_pronosticos, calcular_error_modelo
from moduloproductos import ingresar_productos, mostrar_productos, eliminar_productos, cantidad_producto, mostrar_estante, producto_eliminado, agregar_producto
from modulopedidos import colgar_pedido, mostrar_pedidos

#Listas donde se agregaran los datos (diccionarios)
productos = []
productos_eliminados = []
pedidos = []

#Contador
numcode = 0

# Diccionario para guardar datos del pronóstico (demandas, n, alpha)
datos_pronostico = {
    "demandas": [],
    "n": 0,
    "alpha": 0.0,
    "listo_para_error": False
}
#Mensaje de bienvenida para el usuario
inicio = input ("""Bienvenido Usuario, gracias por usar nuestro
programa. Este está diseñado para que llevar el inventario
de tus productos no sea un dolor de cabeza :).  Aquí, podrás
agregar los productos de tu tienda y montar los pedidos. 
El programa se encargará de actualizar todo de manera automática.
Para continuar, presiona enter """)

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
    elif opcion == "10": 
        calcular_error_modelo(datos_pronostico)
    elif opcion == "11": 
        agregar_producto(productos) #Agregar producto para aumentar el stock
    else: 
        print ("Opción no valida")
    
    pausa = input ("Presione enter para continuar. . . ")