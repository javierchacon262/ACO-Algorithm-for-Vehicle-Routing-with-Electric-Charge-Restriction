def evalTiempo(self, nodo2, dist2, nodo3, dist3):
    v = self.world.velocity
    time = cop.deepcopy(self.time)
    flagOnTime = False
    flagSup = False
    flagDep = False
    flagN3 = False
    if nodo3 is not None:
        flagN3 = True:
    if time + (dist2/v) < nodo2.ventana[0]:
        #ESPERAR Y VIAJAR
        time += nodo2.ventana[0] - (dist2/v) - time
        #TIEMPO DE SERVICIO
        time += nodo2.tServicio
        if flagN3:
            if time + (dist3/v) < nodo3.ventana[0]:
                #ESPERAR Y VIAJAR NODO 3
                time += nodo3.ventana[0] - (dist3/v) - time
                #TIEMPO DE SERVICIO NODO 3
                time += nodo3.tServicio
            elif time + (dist3/v) > nodo3.ventana[0] and time + (dits3/v) < nodo3.ventana[1]:
                #VIAJE Y TIEMPO DE SERVICIO NODO3
                time += (dist3/v) + nodo3.tServicio
            elif time + (dist3/v) > nodo3.ventana[1]:
                #DESCARTAR NODO3
                mNode = max(self.)
    elif time + (dist2/v) > nodo2.ventana[0] and time + (dist2/v) < nodo2.ventana[1]:
        #VIAJE Y TIEMPO DE SERVICIO
        time += (dist2/v) + nodo2.tServicio
        if flagN3:
            if time + (dist3/v) < nodo3.ventana[0]:
                #ESPERAR Y VIAJAR NODO 3
                time += nodo3.ventana[0] - (dist3/v) - time
                #TIEMPO DE SERVICIO NODO 3
                time += nodo3.tServicio
            elif time + (dist3/v) > nodo3.ventana[0] and time + (dits3/v) < nodo3.ventana[1]:
                #VIAJE Y TIEMPO DE SERVICIO NODO3
                time += (dist3/v) + nodo3.tServicio
            elif time + (dist3/v) > nodo3.ventana[1]:
                #DESCARTAR NODO3
                mNode = max(self.)
    elif time + (dist2/v) > nodo2.ventana[1]:
        #DESCARTAR NODO 2 Y EVALUAR NODO 3
        mNode = max(self.)
        if flagN3:
            if time + (dist3/v) < nodo3.ventana[0]:
                #ESPERAR Y VIAJAR NODO 3
                time += nodo3.ventana[0] - (dist3/v) - time
                #TIEMPO DE SERVICIO NODO 3
                time += nodo3.tServicio
            elif time + (dist3/v) > nodo3.ventana[0] and time + (dits3/v) < nodo3.ventana[1]:
                #VIAJE Y TIEMPO DE SERVICIO NODO3
                time += (dist3/v) + nodo3.tServicio
            elif time + (dist3/v) > nodo3.ventana[1]:
                #DESCARTAR NODO3
                mNode = max(self.)
    return([flagOnTime, flagSup, flagDep, flagN3, time])

    