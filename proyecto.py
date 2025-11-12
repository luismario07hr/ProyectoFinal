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
        a = int(input("¿Cuántos productos desea agregar?: "))
        for x in range(a):
            producto = {}
            producto["Nombre"] = input("Ingrese el nombre del producto: ")
            producto["Codigo"] = "P00" + str(numcode)
            producto["Cantidad"] = int(input("Ingrese la cantidad del producto: "))
            producto["Precio"] = float(input("Ingrese el precio del producto: "))
            producto["Categoria"] = input("Ingrese la categoría del producto: ")
            producto["Lugar"] = input ("Ingrese en que estante está el artículo: ")
            productos.append(producto)
            numcode += 1
            print ("----------------------------------------")
        
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