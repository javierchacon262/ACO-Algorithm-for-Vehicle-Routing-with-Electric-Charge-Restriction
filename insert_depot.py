def insert_depot(self):
        print("\nInserta depot: \n")
        node1 = self.node()
        if type(node1) == list:
            node1 = node1[0]
        time = 0
        coordDep = self.start.getCoord()
        coord1 = node1.getCoord()
        dist1 = (self.world.costoVeh) + (self.world.costoDis * euclidean(coord1, coordDep))
        enerDep = self.world.conRate * dist1
        if node1.tipo == 'e':
            print("\nse encuentra en una estacion: ")
            if self.energia <= enerDep and enerDep <= self.world.cargaE:
                dif = enerDep - self.energia
                time += dif/self.world.recRate
                self.energia = enerDep
                self.make_move(None)
            elif self.energia <= enerDep and enerDep > self.world.cargaE:
                Est = self.look_charge(coord1)
                nodEst = self.world.estaciones[Est[0]]
                print("\n estacion mas cercana: ", Est[0])
                coordEst = nodEst.getCoord()
                distNE = (self.world.costoVeh) + (self.world.costoDis * euclidean(coord1, coordEst))
                print("\ndistancia: ", distNE)
                enerEst = distNE * self.world.conRate
                print("\nEnergia actual: ", self.energia)
                print("\nEnergia necesaria: ", enerEst)
                if self.energia <= enerEst and enerEst <= self.world.cargaE:
                    print("\nBuscando otra estacion:\n")
                    dif = enerEst - self.energia
                    time += dif/self.world.recRate
                    self.energia = enerEst
                    self.make_move(nodEst)
                    self.insert_depot()
                elif self.energia >= enerEst:
                    print("\nViaja a una estacion cercana: ")
                    self.make_move(nodEst)
                    self.insert_depot()
                else:
                    print("\nError, No puede ir a ninguna estacion: 1\n")
            elif self.energia >= enerDep:
                self.make_move(None)
        elif node1.tipo == 'c':
            if self.energia <= enerDep:
                Est = self.look_charge(coord1)
                nodEst = self.world.estaciones[Est[0]]
                print("\Se encuentra en un cliente: ")
                print("\n estacion mas cercana: ", Est[0])
                coordEst = nodEst.getCoord()
                distNE = (self.world.costoVeh) + (self.world.costoDis * euclidean(coord1, coordEst))
                print("\ndistancia: ", distNE)
                enerEst = distNE * self.world.conRate
                print("\nEnergia actual: ", self.energia)
                print("\nEnergia necesaria: ", enerEst)
                if self.energia <= enerEst and enerEst <= self.world.cargaE:
                    print("\nBuscando otra estacion:\n")
                    dif = enerEst - self.energia
                    time += dif/self.world.recRate
                    self.energia = enerEst
                    self.make_move(nodEst)
                    self.insert_depot()
                elif self.energia >= enerEst:
                    print("\nViaja a una estacion cercana: ")
                    self.make_move(nodEst)
                    self.insert_depot()
                else:
                    print("\nError, No puede ir a ninguna estacion: 2\n")
            elif self.energia >= enerDep:
                self.make_move(None)
        return self