def colgar_pedido(pedidos, productos): 
    pedido = {}
    print ("------------------------------------------------------")
    producto_elegido = input("Ingrese el código del producto: ").capitalize()
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
                print ("------------------------------------------------------")
            else: 
                cantidad_final = producto["Cantidad"] - cantidad_apedir
                producto["Cantidad"] = cantidad_final
                
                precio_final = cantidad_apedir*producto["Precio"]
                pedido["Nombre"] = nombre_producto
                pedido["Codigo"] = codigo_pedido
                pedido["Cantidad"] = cantidad_apedir
                pedido["Total"] = precio_final
                print ("Pedido montado exitosamente")
                print ("------------------------------------------------------")
                pedidos.append(pedido)
    
    if codigo_pedido == None:
        print ("------------------------------------------------------")
        print ("No hay artículos con ese código")
        print ("------------------------------------------------------")
             
def mostrar_pedidos (pedidos):
    if pedidos == []: 
        print ("------------------------------------------------------")
        print ("No hay pedidos registrados")
        print ("------------------------------------------------------")
    else:
        for pedido in pedidos:
            print ("-----------------------------------")
            for x,y in pedido.items(): 
                print (f"\t {x}: {y}")
            print ("-----------------------------------")