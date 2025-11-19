def ingresar_datos_mensuales(datos_pronostico):
    print ("------------------------------------------------------")
    #Declaramos de nuevo la variable para borrar los datos si ya se habian ingresado
    datos_pronostico["demandas"] = []
    
    cantidad = int(input("¿Cuántos meses de datos en la demanda va a ingresar?: "))
    contador = 0
    while contador < cantidad:
        valor = float(input(f"Ingrese la demanda real del mes {contador + 1}: "))
        datos_pronostico["demandas"].append(valor)
        contador += 1
      
    print ("Datos guardados correctamente")
    print ("------------------------------------------------------")

def calcular_pronosticos(datos_pronostico):
    #Verificamos si la lista de demandas está vacía
    if datos_pronostico["demandas"] == []:
        print ("------------------------------------------------------")
        print ("No ha ingresado datos para calcular un pronóstico (Opción 7 -> Paso 1)")
        print ("------------------------------------------------------")
        return

    demandas = datos_pronostico["demandas"]
    total_datos = len(demandas)
    
    print ("------------------------------------------------------")
    print ("--- Cálculo de pronóstico: Promedio móvil simple ---")
    
    #1. Promedio móvil simple
    # Fórmula: Suma de las últimas n demandas / n 
    n = int(input("Promedio Móvil - Ingrese 'n' (periodos a promediar): "))
    
    if n > total_datos:
        print ("No hay suficientes datos para ese 'n'")
        
    else:
        suma = 0
        # Sumamos solo los últimos 'n' datos
        inicio = total_datos - n
        for i in range(inicio, total_datos):
            suma = suma + demandas[i]
            
        pronostico_movil = suma / n
        print (f"Pronóstico con promedio móvil simple): {pronostico_movil}")
    
    #2. Suavizamiento exponencial 
    # Fórmula: Ft+1 = Ft + alpha * (Dt - Ft) 
    """ La fórmula se basa en base a los siguientes datos:
    Pronóstico del último periodo
    Demanda de ese periodo
    Parámetro de suavización α (valor entre 0.0 y 1.0)"""
    
    alpha = float(input("Suavizamiento Exp. - Ingrese 'alpha' (0 a 1): "))
    
    #Asumimos que el primer pronóstico es igual a la primera demanda real
    pronostico_expo = demandas[0]
    
    # Se hace el calculo mes a mes, sólo interesa el dato del n + 1, es decir el próximo mes
    for i in range(0, total_datos):
        demanda_actual = demandas[i]
        pronostico_expo = pronostico_expo + alpha * (demanda_actual - pronostico_expo)
        
    print (f"Pronóstico con suavizamiento exponencial): {pronostico_expo}")
    print ("------------------------------------------------------")
    
    datos_pronostico["n"] = n
    datos_pronostico["alpha"] = alpha
    datos_pronostico["listo_para_error"] = True

def calcular_error_modelo(datos_pronostico):
    #Verificamos si ya se hizo el cúlculo de los pronósticos antes
    if datos_pronostico["listo_para_error"] == False:
        print ("------------------------------------------------------")
        print ("Primero debe realizar los cálculos de los pronósticos (Opción 7)")
        print ("------------------------------------------------------")
        return

    demandas = datos_pronostico["demandas"]
    n = datos_pronostico["n"]
    alpha = datos_pronostico["alpha"]
    total_datos = len(demandas)
    
    print ("------------------------------------------------------")
    print ("--- Cálculo del error (MSE) ---")
    print ("Veremos la diferencia entre los dos modelos de pronósticos")
    
    #Error promedio móvil simple
    # Error = Valor Real - Valor Pronosticado
    # Fólmula (MSE):  Suma de los n errores al cuadrado / cantidad de n
    suma_error_movil = 0
    contador_movil = 0
    mse_movil = 0
    # Solo podemos calcular error a partir del mes n, porque sino no habria suficientes datos
    for mes_actual in range(n, total_datos):
        suma_meses = 0
        inicio_rango = mes_actual - n
        
        for mes_anterior in range(inicio_rango, mes_actual):
            suma_meses = suma_meses + demandas[mes_anterior]
            
        #El pronóstico es el promedio de ese mes
        pronostico_calculado = suma_meses / n
        
        #Obtener lo que realmente vendimos ese mes
        venta_real = demandas[mes_actual]
        
        #Calcular el error (Diferencia entre realidad y pronóstico)
        error = venta_real - pronostico_calculado
        
        #Elevamos al cuadrado 
        error_cuadrado = error * error
        
        #Acumulamos este error en la suma total
        suma_error_movil = suma_error_movil + error_cuadrado
        contador_movil += 1

    #Evitar el caso de que se divida por cero
    if contador_movil != 0:
        mse_movil = suma_error_movil / contador_movil
        
    #Error Suavizamiento Exponencial
    # Fórmula de Pronóstico: Ft+1 = Ft + alpha * (Dt - Ft)
    # Fórmula Error (MSE): Suma de errores al cuadrado / cantidad
    suma_error_exponencial = 0
    contador_exponencial = 0
    mse_exponencial = 0
    #El primer pronóstico es igual a la primera demanda real
    pronostico_calculado = demandas[0]
    
    for i in range(0, total_datos - 1):
        #Los mismos pasos que en el promedio simple, solo se sustituye la formula del pronóstico
        venta_real_actual = demandas[i]
        pronostico_calculado = pronostico_calculado + alpha * (venta_real_actual - pronostico_calculado)
        venta_real_siguiente = demandas[i+1]
        error = venta_real_siguiente - pronostico_calculado
        error_cuadrado = error * error
        suma_error_exponencial = suma_error_exponencial + error_cuadrado
        contador_exponencial += 1
        
    if contador_exponencial != 0:
        mse_exponencial = suma_error_exponencial / contador_exponencial
  
        
    print (f"\nResultados del Error Cuadrático Medio (MSE):")
    print (f"\tPromedio Móvil (n={n}): {mse_movil}")
    print (f"\tSuavizamiento Exp (alpha={alpha}): {mse_exponencial}")  
    print ("------------------------------------------------------")