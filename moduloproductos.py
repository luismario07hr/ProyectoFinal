def ingresar_productos(productos):
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