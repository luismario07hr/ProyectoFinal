def colgar_pedido(pedidos, productos): 
    pedido = {}
    producto_elegido = input("Ingrese el código del producto: ")
    codigo_pedido = None
    nombre_producto = None
    cantidad_final = 0
    precio_final = 0
    
    for producto in productos: 
        if producto_elegido == producto["Codigo"]: 
            codigo_pedido = producto["Codigo"]
            nombre_producto = producto["Nombre"]
            cantidad_apedir = int(input("Ingrese la cantidad a pedir: "))

            if cantidad_apedir > producto["Cantidad"]: 
                print ("Sorry, no hay suficiente stock para cubrir el pedido")
            else: 
                cantidad_final = producto["Cantidad"] - cantidad_apedir
                producto["Cantidad"] = cantidad_final
                
                precio_final = cantidad_apedir*producto["Precio"]
                pedido["Nombre"] = nombre_producto
                pedido["Codigo"] = codigo_pedido
                pedido["Cantidad"] = cantidad_apedir
                pedido["Total"] = precio_final
    
    if codigo_pedido == None:
        print ("No hay artículos con ese código")
             
    pedidos.append(pedido)
    for x,y in pedido.items(): 
        print (x, y)