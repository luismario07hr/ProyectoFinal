def ingresar_productos(productos, numcode): #funcion para ingresar productos
    print ("------------------------------------------------------")
    print (f"Ingresar Producto")
    numcode += 1 #Cambio automático deo contador
    producto = {} #Diccionario
    
    #Agregar los datos al diccionario
    producto["Nombre"] = input("Ingrese el nombre del producto: ")
    producto["Codigo"] = "P" + str(f"{numcode:03d}")
    producto["Cantidad"] = int(input("Ingrese la cantidad del producto (números enteros): "))
    producto["Precio"] = float(input("Ingrese el precio del producto (enteros o decimales): "))
    producto["Categoria"] = input("Ingrese la categoría del producto: ")
    producto["Estante"] = input ("Ingrese en que estante está el artículo (1-10): ")
    productos.append(producto)
    print ("------------------------------------------------------")
    return numcode

def mostrar_productos (productos):
    if productos == []: #Si la lista esta vacia, mostrar que no hay productos
        print ("------------------------------------------------------")
        print ("No hay productos disponibles")
        print ("------------------------------------------------------")
    else:
        print ("------------------------------------------------------")
        print("Los productos disponibles son: ") #Mostrar producto por producto con todos sus datos
        for producto in productos: 
            for x, y in producto.items(): 
                print (f"\t{x}: {y}\t")
            print ("------------------------------------------------------")
        
def cantidad_producto (productos): 
    print ("------------------------------------------------------")
    eleccion_producto = input("Elija el código del producto a mostrar: ").capitalize() 
    cantidad = 0
    nombre = None
    for producto in productos: 
        if eleccion_producto == producto["Codigo"]:
            cantidad = producto["Cantidad"]
            nombre = producto["Nombre"]
    
    if nombre == None and cantidad == 0: #
        print ("------------------------------------------------------")
        print ("Lo siento, no hay productos con ese código")
        print ("------------------------------------------------------")
        return
    elif cantidad == 0: #Si la cantidad es 0, mostrar que no hay stock
        print (f"No hay stock de {nombre}")
    else: #Mostrar el producto y la cantidad
        print (f"La cantidad del producto {nombre} es {cantidad}")
        print ("------------------------------------------------------")
        
        
def eliminar_productos (productos, productos_eliminados): 
    print ("------------------------------------------------------")
    eleccion = input("Ingrese el código del producto a eliminar: ").capitalize()
    eliminado = 0
    for x, producto in enumerate(productos): 
        if eleccion == producto["Codigo"]:
            eliminado = productos.pop(x)
            productos_eliminados.append(eliminado)
            print ("Producto eliminado exitosamente")
            print ("------------------------------------------------------")
            break
       
    if eliminado == 0: 
        print ("------------------------------------------------------")
        print ("No existe ningún producto con ese código")
        print ("------------------------------------------------------")
        return
        
    
def mostrar_estante(productos):
    elegir_estante = input("Elija el estante (1-10) en el que están los artículos: ")
    for producto in productos:
        print ("------------------------------------")
        if elegir_estante == producto["Estante"]: 
            print (producto["Nombre"])
        print ("------------------------------------")
        
def producto_eliminado(productos_eliminados): 
    if productos_eliminados == []: #Si la lista esta vacia, mostrar que no hay productos eliminados
        print ("------------------------------------------------------")
        print ("No hay productos eliminados")
        print ("------------------------------------------------------")
    else:
        print ("------------------------------------------------------")
        print("Los productos eliminados son: ") #Mostrar producto por producto con todos sus datos
        for producto in productos_eliminados: 
            print (f"Nombre: {producto["Nombre"]}")
            print (f"Código: {producto["Codigo"]}")
            print (f"Categoria: {producto["Categoria"]}")
            print ("------------------------------------------------------")
            
def agregar_producto(productos): #Funcion para agregar productos cuando se hagan pedidos al mayorista
    print ("------------------------------------------------------")
    producto_elegido = input("Ingrese el código del producto: ").capitalize()
    codigo_pedido = None

    for producto in productos: 
        if producto_elegido == producto["Codigo"]:
            print (f"El producto es {producto["Nombre"]}") 
            codigo_pedido = producto["Codigo"]
            cantidad_aagregar = int(input("Ingrese la cantidad a agregar: "))

            if cantidad_aagregar < 0: 
                print ("No puedes agregar números negativos")
                print ("------------------------------------------------------")
            else: 
                cantidad_final = producto["Cantidad"] + cantidad_aagregar
                producto["Cantidad"] = cantidad_final
    
    if codigo_pedido == None:
        print ("------------------------------------------------------")
        print ("No hay artículos con ese código")
        print ("------------------------------------------------------")                                                                                              