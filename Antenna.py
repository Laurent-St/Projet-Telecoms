class Antenna:
    "Classe pouvant représenter soit l'émetteur, soit le récepteur, étant donné"
    "que ceux-ci ont des propriétés duales"

    def __init__(self,gain,x,y):
        self.gain=gain
        self.x=x
        self.y=y
        self.power_emission=0
        self.power_reception=0
        self.h_e=-38.98 # [m]

        #VALEURS PAS SUREs
        self.r_joule=1000 # [ohms]     #A MODIFIER
        self.r_emission=1000            # A MODIFIER
        self.r_tot=self.r_joule+self.r_emission

    def setpower_emission(self,power_emission):
        self.power_emission=power_emission

    def setpower_reception(self,power_reception):
        self.power_reception=power_reception
