def can_move(self):
        #Aqui van las condiciones donde se ven los 1/4nodes mas cercanos y se evaluan con factibleNode para ver que
        #la hormiga se pueda mover o no
        flagEst = False
        if self.merca >= min(self.unvisited, key = lambda x : x.demanda).demanda:
            selec = self.Selec14(self.node())
            print("\nselec: ", len(selec), "\n")
            if len(selec) > 0:
                sel = []
                sel.clear()
                notF = []
                notF.clear()
                for i in range(len(selec)):
                    nod = selec[i]
                    if type(nod) == list:
                        fl = nod[0].flagV
                    else:
                        fl = nod.flagV
                    #print("\nEvaluacion nodo: ", i, "\n")
                    fact1 = self.factibleNode(selec[i])
                    if fact1[0] and not fl:
                        #print("\nfactible:\n")
                        sel.append(selec[i])
                        #print("\nflagGeneral: ", self.factibleNode(selec[i])[0])
                        #print("\nflagN3: ", self.factibleNode(selec[i])[1])
                        #print("\nflagEst: ", self.factibleNode(selec[i])[2])
                        #print("\nflagDep: ", self.factibleNode(selec[i])[3])
                    elif not fact1[0] and fact1[2] and not fact1[3]:
                        notF.append(selec[i])
                print("\nLength de notF:", len(notF))
                print("\nseleccion: ", len(sel))
                if self.node().tipo == 'e' or self.node() == self.start:
                    flagEst = True
                    ultNodo = self.visited[-2]
                    print("\nNodo anterior a mi: ", ultNodo)
                    print("\nNodo actual: ", self.node())
                else:
                    flagEst = False
                    ultNodo = self.visited[-2]
                    print("\nNodo anterior a mi: ", ultNodo)
                    print("\nNodo actual: ", self.node())
                
                return [sel, notF, flagEst]
            else:
                return []
        else:
            print("\nOutOfMerca...")
            return []

def insertStation():