#Evaluacion de las restricciones sobre la solucion optima local encontrada con el algoritmo de hormigas
costoVeh = 0
costoDis = 1
x = 1
#################################
#Velocidad, traer de la instancia
#################################
v = 1
#################################
#Vector de carros que crecera dinamicamente, dependiendo de la instancia
veCars = []
#Coordenadas de clientes nodes2
nodes2 = nodes[:]
estaciones2 = estaciones[:]
demandas2 = demandas[:]
conCars = 0
veCars.append(Vehiculo(conCars, 79.69, 200))
print("\n carga de mercancia inicial del carro: " + str(conCars) + "  =  " + str(veCars[conCars].cargaM) + "\n")
i = 0
nodo1 = None
nodo2 = None
dist = 0
time = 0
flagDep = False
while nodo2 != 0:
    if flagDep:
        #Deposito como nodo inicial
        nodo1 = int(vecSol[0][0])
        coord1 = nodes[0][str(nodo1)]
        flagDep = False
    else:
        nodo1 = int(vecSol[0][i])
        coord1 = nodes[0][str(nodo1)]
        
    nodo2 = int(vecSol[0][i+1])
    coord2 = nodes[0][str(nodo2)]
    #Primera Decicion: Carga de Mercancia
    if veCars[conCars].cargaM >= demandas[0][str(nodo2)][0] and flagDep == False:
        flagDep = False
        print("\n nodo1: " + str(nodo1) + "\n")
        #print("\n coordenadas nodo 1: ", coord1, "\n")
        print("\n nodo2: " + str(nodo2) + "\n")
        #print("\n coordenadas nodo 2: ", coord2, "\n")
        x = 1
        
        
        #FUNCION OBJETIVO:
        dist1 = (costoVeh * x) + (costoDis * euclidean(coord1, coord2) * x)
        
        
        #SUMA DE TIEMPO PARA CUADRAR CON LAS VENTANAS DE TIEMPO
        #Segunda Decicion A: Ventanas de Tiempo
        if (demandas[0][str(nodo2)][1] - (dist1 / v) - veCars[conCars].time) < 0:
            #Verifica que el tiempo que le toma en ir de un cliente a otro este dentro de la ventana de tiempo de ese nodo
            veCars[conCars].time += (dist1 / v)
        else:
            #cuando la condicion es mayor a cero significa que el carro debe esperar por el cliente para que abra,
            #El carro espera en el nodo anterior
            veCars[conCars].time += (dist1 / v) + (demandas[0][str(nodo2)][1] - (dist1 / v) - veCars[conCars].time)
            
        
        #Segunda Decicion B: Ventanas de Tiempo
        #Cuando esta dentro de la ventana de tiempo
        if veCars[conCars].time >= demandas[0][str(nodo2)][1] and veCars[conCars].time <= demandas[0][str(nodo2)][2]:
            veCars[conCars].cargaM -= demandas[0][str(nodo2)][0]
            veCars[conCars].time += demandas[0][str(nodo2)][3]
            dist += dist1
            print("\n carga restante carro: " + str(conCars) + "  =  " + str(veCars[conCars].cargaM) + "\n")
            #print("\n distancia euclideana: ", dist1, "\n")
            print("\n distancia euclideana acumulada: ", dist, "\n")
            i += 1
            
            
        elif veCars[conCars].time > demandas[0][str(nodo2)][2]:
            #Cuando esta por encima de la ventana de tiempo
            #Pregunta si el tiempo del carro es mayor a la ventana de tiempo mayor
            #Manda de Ultimos los nodos a los que no alcanza a llegar pero cuyas ventanas superiores de tiempo
            #son menores a la del nodo con ventana de tiempo maxima
            
            
            vecRest = vecSol[0][i+1:-2]
            if veCars[conCars].time < findMaxDict(demandas[0], vecRest):    
                veCars[conCars].time -= dist1 / v
                nodoUlt = vecSol[0].pop(i+1)
                vecSol[0].insert(-2, nodoUlt)
                print("###########################################################################################")
                print("\n Lista de Nodos Nueva por ventana de tiempo SUPERIOR: \n\n")
                print("###########################################################################################")
                
                
                
                
            else:
                #Si el tiempo acumulado del carro supera todas las ventanas de tiempo,
                #y sale un nuevo carro
                veCars[conCars].time -= dist1 / v
                flagDep = True
                nodo2 = int(vecSol[0][0])
                coord2 = nodes[0][str(nodo2)]
                print("################################################################")
                print("\n nodo2 regreso a deposito: " + str(nodo2) + "\n")
                print("\n coordenadas nodo 2: ", coord2, "\n")
                dist1 = (costoVeh * x) + (costoDis * euclidean(coord1, coord2) * x)
                dist += dist1
                nodo2 = None
                #Se aumenta el contador de carros y se crea el siguiente, 
                #Super importante actualizar los nodos y los coords
                conCars += 1
                veCars.append(Vehiculo(conCars, 79.69, 200))
                print("########################################################################")
                print("Nueva Ruta, Nuevo Carro:")
                print("########################################################################")
                #print("\n carga de mercancia inicial del carro: " + str(conCars) + "  =  " + str(veCars[conCars].cargaM) + "\n")
                #print("########################################################################")
    #Else de la Primera Decicion
    else:
        flagDep = True
        #Regreso al deposito del carro actual y continua el siguiente carro
        #Tener en cuenta que el segundo indice del siguiente statement se pone porque es el regreso al deposito
        nodo2 = int(vecSol[0][0])
        coord2 = nodes[0][str(nodo2)]
        print("################################################################")
        print("\n nodo2 regreso a deposito: " + str(nodo2) + "\n")
        print("\n coordenadas nodo 2: ", coord2, "\n")
        dist1 = (costoVeh * x) + (costoDis * euclidean(coord1, coord2) * x)
        dist += dist1
        nodo2 = None
        #Se aumenta el contador de carros y se crea el siguiente, 
        #Super importante actualizar los nodos y los coords
        conCars += 1
        veCars.append(Vehiculo(conCars, 79.69, 200))
        print("########################################################################")
        print("Nueva Ruta, Nuevo Carro:")
        print("########################################################################")
        #print("\n carga de mercancia inicial del carro: " + str(conCars) + "  =  " + str(veCars[conCars].cargaM) + "\n")
        #print("########################################################################")
        
print("\n\n contador de carros usados: " + str(conCars+1))