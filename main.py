# main
from GUI import GUI
from Model import *
import numpy as np
from fctsmath import *
from Antenna import *
from ref_tr_diff import *

#taille de la carte et initialisation des murs
xmax=50
ymax=50

model=Model(xmax,ymax)
cat=2
model.setwalls(xmax,ymax, cat)
#model.setmatrice()

#création émetteur et récepteur
gain=1

tx=Antenna(gain,10,15)
rx=Antenna(gain,25,32)

#ATTENTION ici tx et rx désignent l'émetteur et le récepteur, mais
#dans la fct reflexion ils désignent le tuple contenant la position

#réflexion
rays=reflexion((tx.x,tx.y),(rx.x,rx.y),xmax,ymax,model.getwalls())
GUI(model.getwalls(),xmax,ymax,rays)



"""
#test rayonnement
xtx=10
ytx=15

xrx=25
yrx=32

tx=(xtx,ytx)
rx=(xrx,yrx)

im=[0]*4

#première réflexion
im[0]=(2*xmax-xtx,ytx) #right
im[1]=(xtx,-ytx) #up
im[2]=(-xtx,ytx) #left
im[3]=(xtx,2*ymax-ytx)  #bottom

#trouver les pt d'intersection avec les murs
pt_interleft=line_intersection([im[2],rx],[(0,0),(0,50)])

rays=[0]*2
rays[0]=[tx,pt_interleft]
rays[1]=[pt_interleft,rx]

GUI(model.getwalls(),xmax,ymax,rays)
"""

    









