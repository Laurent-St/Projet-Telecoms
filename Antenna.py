class Antenna:
    "Classe pouvant représenter soit l'émetteur, soit le récepteur, étant donné"
    "que ceux-ci ont des propriétés duales"

    def __init__(self,gain,x,y):
        self.gain=gain
        self.x=x
        self.y=y
