def energiaRst(self, node2):
        ############################################################################################################   
        eA = cop.deepcopy(self.energia)
        #Cuestiones Nodo Actual
        node1 = cop.deepcopy(self.node())
        coord1 = node1.getCoord()
        #Estacion Nodo Actual
        est1 = self.world.estaciones[self.look_charge(coord1)[0]]
        coordEst1 = est1.getCoord()
        distNAEst1 = (self.world.costoVeh) + (self.world.costoDis * euclidean(coord1, coordEst1))
        #Cuestiones Nodo Sig
        coord2 = node2.getCoord()
        distN2 = (self.world.costoVeh) + (self.world.costoDis * euclidean(coord1, coord2))
        est2 = self.world.estaciones[self.look_charge(coord2)[0]]
        coordEst2 = est2.getCoord()
        #distEst1N2 = (self.world.costoVeh) + (self.world.costoDis * euclidean(coordEst1, coord2))
        distN2Est2 = (self.world.costoVeh) + (self.world.costoDis * euclidean(coord2, coordEst2))
        #Energias
        cRate = self.world.conRate
        eNodo2 = (distN2 * cRate) + (distN2Est2 * cRate)
        eEst1 = distNAEst1 * cRate 

        vec = self.Selec14(node2)
        if len(vec) > 0:
            if vec[0] == node2:
                if len(vec) > 1:
                    node3 = vec[1]
                    print("\nnode3: ", node3, "\n")
                else:
                    node3 = None
            else:
                node3 = vec[0]
            if node3 != None:
                if type(node3) == list:
                    coord3 = node3[0].getCoord()
                else:
                    coord3 = node3.getCoord()
                distN3 = (self.world.costoVeh) + (self.world.costoDis * euclidean(coord2, coord3))
                est3 = self.world.estaciones[self.look_charge(coord3)[0]]
                coordEst3 = est3.getCoord()
                distN3Est3 = (self.world.costoVeh) + (self.world.costoDis * euclidean(coord3, coordEst3))
                eNE3 = (distN3 * cRate) + (distN3Est3 * cRate)
        else:
            node3 = None
        #tiempo
        time = 0
        ### flags ###
        flagEner = False
        flagN3 = False
        flagEst = False
        #Tomas de Decision
        if eA > eNodo2:
            flagEner = True
            #ver uno mas adelante
            if node3 is not None:
                if eA > (distN2 * cRate) + eNE3:
                    flagN3 = True
                else:
                    flagN3 = False
            else:
                flagN3 = False
            #ver necesidad de cargar
        elif eA > eEst1:
            #print("\nPuede ir a una estacion!\n")
            flagEst = True
        else:
            print("Error de ruta 2, Auto Estancado")
        return [flagEner, flagN3, flagEst, node2, node3, eA, time, vec]