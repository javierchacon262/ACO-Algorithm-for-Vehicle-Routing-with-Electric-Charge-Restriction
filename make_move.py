def make_move(self, dest):
        
        # Since self.node simply refers to self.visited[-1], which will be
        # changed before we return to calling code, store a reference now.
        ori = self.node()

        # When dest is None, all nodes have been visited but we may not
        # have returned to the node on which we started. If we have, then
        # just do nothing and return None. Otherwise, set the dest to the
        # node on which we started and don't try to move it from unvisited
        # to visited because it was the first one to be moved.
        if dest is None:
            print("\nRegreso al depot:")
            dest = self.start   # last move is back to the start
            self.visited.append(dest)
            self.time = 0
            self.energia = cop.copy(self.world.cargaE)
            self.merca = cop.copy(self.mercaMax)
            if type(ori) == list:
                if type(dest) == list:
                    if ori[0] != dest[0]:
                        edge = self.world.edges[ori[0], dest[0]]
                    else:
                        edge = None
                else:
                    if ori[0] != dest:
                        edge = self.world.edges[ori[0], dest]
                    else:
                        edge = None
            else:
                if type(dest) == list:
                    if ori != dest[0]:
                        edge = self.world.edges[ori, dest[0]]
                    else:
                        edge = None
                else:
                    if ori != dest:
                        edge = self.world.edges[ori, dest]
                    else:
                        edge = None
            return edge, self
        else:
            if type(dest) == list:
                print("\nDestino tipe lista: ", dest)
                self.visited.append(dest[0])
                dest[0].flagV = True
            else:
                self.visited.append(dest)
                dest.flagV = True
        print
        if type(ori) == list:
            coord1 = ori[0].getCoord()
            if type(dest) == list:
                coord2 = dest[0].getCoord()
                print("1", ori[0]==dest[0])
                if ori[0]==dest[0]:
                    print("ori: ", ori[0].getCoord())
                    print("dest: ", dest[0].getCoord())
                else:    
                    edge = self.world.edges[ori[0], dest[0]]
                    self.traveled.append(edge)
                    dist = (self.world.costoVeh) + (self.world.costoDis * euclidean(coord1, coord2))
                    self.energia -= self.world.conRate * dist
                    print("dist: ", dist)
                    self.distance += dist
                    print("distance: ", self.distance)
                    self.cont += 1
                    print(self.cont)
                    return edge, self
            else:
                coord2 = dest.getCoord()
                print("2", ori[0]==dest)
                if ori[0]==dest:
                    print("ori: ", ori[0].getCoord())
                    print("dest: ", dest.getCoord())
                else:    
                    edge = self.world.edges[ori[0], dest]
                    self.traveled.append(edge)
                    dist = (self.world.costoVeh) + (self.world.costoDis * euclidean(coord1, coord2))
                    self.energia -= self.world.conRate * dist
                    print("dist: ", dist)
                    self.distance += dist
                    print("distance: ", self.distance)
                    self.cont += 1
                    print(self.cont)
                    return edge, self
        else:
            coord1 = ori.getCoord()
            if type(dest) == list:
                coord2 = dest[0].getCoord()
                print("3", ori==dest[0])
                if ori == dest[0]:
                    print("ori: ", ori.getCoord())
                    print("dest: ", dest[0].getCoord())
                else:    
                    edge = self.world.edges[ori, dest[0]]
                    self.traveled.append(edge)
                    dist = (self.world.costoVeh) + (self.world.costoDis * euclidean(coord1, coord2))
                    self.energia -= self.world.conRate * dist
                    print("dist: ", dist)
                    self.distance += dist
                    print("distance: ", self.distance)
                    self.cont += 1
                    print(self.cont)
                    return edge, self
            else:
                coord2 = dest.getCoord()
                print("4", ori==dest)
                if ori == dest:
                    print("ori: ", ori.getCoord())
                    print("dest: ", dest.getCoord())
                else:    
                    edge = self.world.edges[ori, dest]
                    self.traveled.append(edge)
                    dist = (self.world.costoVeh) + (self.world.costoDis * euclidean(coord1, coord2))
                    self.energia -= self.world.conRate * dist
                    print("dist: ", dist)
                    self.distance += dist
                    print("distance: ", self.distance)
                    self.cont += 1
                    print(self.cont)
                    return edge, self