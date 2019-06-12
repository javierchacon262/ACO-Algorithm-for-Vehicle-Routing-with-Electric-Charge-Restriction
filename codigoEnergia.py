def energiaR(carro, nodo1, nodo2, dist1, nodes, estNodo1, estNodo2, conRate, recRate, cargaMax, v, costoVeh, costoDis):
    ############################################################################################################   
    #Coordenadas de los nodos
    coord1 = self.node().getCoord()
    coord2 = node2.getCoord()
    #Energia actual del carro
    eA = float(self.energia)
    #Distancia al siguiente nodo
    distN2 = (self.world.costoVeh) + (self.world.costoDis * euclidean(coord1, coord2))
    #Energia hasta el siguiente nodo
    eNN = distN2 * self.world.conRate
    #Energia hasta la estacion mas cercana del siguiente nodo
    eNE = self.look_charge(coord2)[2] * self.world.conRate
    #Energia hasta la estacion mas cercana del nodo actual
    eAE = self.look_charge(coord1)[2] * self.world.conRate
    #Coordenadas del deposito
    depCoord = self.start.getCoord()
    #distancia estacion nodo actual al deposito
    distEstDep = (self.world.costoVeh) + (self.world.costoDis * euclidean(self.look_charge(coord1)[1], depCoord))
    #Energia de la estacion nodo actual al deposito
    eAEDEP = distEstDep * self.world.conRate
    #Tercer Nodo
    vec = self.Selec14(node2)
    if len(vec) > 0:
        node3 = vec[0]
        coord3 = node3.getCoord()
        distN3 = (self.world.costoVeh) + (self.world.costoDis * euclidean(coord2, coord3))
        eN3 = distN3 * self.world.conRate
        est3 = self.look_charge(coord3)
        CoordEst3 = est3[1]
        distNE3 = est3[2]
        eNE3 = distNE3 * self.world.conRate
    else:
        node3 = None
    #tiempo
    time = 0
    ### flags ###
    flagEner = False
    flagN3 = False
    flagEst = False
    flagDep = False
    #Tomas de Decision
    if eA - eNN - eNE > 0:
        flagEner = True
        #ver uno mas adelante
        if node3 is not None:
            if eA - eNN - eN3 - eNE3 > 0:
                flagN3 = True
            else:
                flagN3 = False
        else:
            flagN3 = False
        #ver necesidad de cargar
    elif eA - eAE > 0:
        flagEst = True
        if eA - eNN - eNE < 0:
            #ver uno mas adelante
            if node3 is not None:
                if eA - eNN - eN3 - eNE3 < 0:
                    dif = eNN + eN3 + eNE3 - eA
                    if dif <= cargaMax - eA:
                        #cargar lo necesario
                        #si no le alcanza para 2 nodos, carga para uno solo y vuelve a evaluar
                        eA += dif
                        time += dif/self.world.recRate
                        flagEner = True
                        flagN3 = True
                    else:
                        flagN3 = False
                        dif = eNN + eNE - eA
                        if dif <= cargaMax - eA:
                            eA += dif
                            time += dif/self.world.recRate
                            flagEner = True
                        elif eA - eAEDEP < 0:
                            flagDep = True
                        elif eA - eAEDEP > 0:
                            flagDep = True
            else:
                flagN3 = False
                dif = eNN + eNE - eA
                if dif <= cargaMax - eA:
                    eA += dif
                    time += dif/self.world.recRate
                    flagEner = True     
                elif eA - eAEDEP < 0:
                    flagDep = True
                elif eA - eAEDEP > 0:
                    flagDep = True
        else:
            flagEner = True
    else:
        print("Error de ruta 2, Auto Estancado")
        return None
    return [flagEner, flagEst, flagDep, nodo2, eA, time]