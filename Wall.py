class Wall:
    "Classe mur contenant les coordonnées (x1,y1) et (x2,y2)"
    def __init__(self,x1,x2,y1,y2,mat):
        #mat=material
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
        self.mat=mat
        if mat==1: # 1 = brique
            self.eps_r=4.6
            self.sig=0.02
        elif mat==2: # 2 = beton
            self.eps_r=5
            self.sig=0.014
        elif mat==3: # 3 = cloison
            self.eps_r=2.25
            self.sig=0.04

    def getmat(self):
        return self.mat
    
    
    
