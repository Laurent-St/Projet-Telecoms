# main
from GUI import GUI
from Model import *
import numpy as np
from fctsmath import *
from Antenna import *
from ref_tr_diff import *

#taille de la carte et initialisation des murs
xmax=500
ymax=500

model=Model(xmax,ymax)
cat=1
model.setwalls(xmax,ymax, cat)
#model.setmatrice()

#création émetteur et récepteur
gain=1
txx=78
txy=246
rxx=376 #rxx et rxy sont les coordonnées en haut à gauche de la zone de réception
rxy=443

raystot=[]
tx=Antenna(gain,78,246)
tx.setpower_emission(0.1) #P_TX=0.1 Watt, voir calcul dans le rapport
PRX=0 #puissance totale
ls_PRX_pt_ij=[]
for i in range(0,4):
    for j in range(0,4):
        rx=Antenna(gain,rxx+i,rxy+j)
        rays=reflexion((tx.x,tx.y),(rx.x,rx.y),model.getwalls())
        PRX_pt_ij=0 #puissance recue juste au point considéré
        for ray in rays:
            raystot.append(ray)
            if ray.dis != None:
                PRX_pt_ij==PRX_pt_ij+ray.get_PRX_individuelle(tx)
        PRX=PRX+PRX_pt_ij
        ls_PRX_pt_ij.append(PRX_pt_ij)
        
PRX=PRX/nbre_pts

                
nbre_pts=(i+1)*(j+1)
print('nbre de pts=')
print(nbre_pts)

##rx=Antenna(gain,rxx,rxy)
##raystot=reflexion((tx.x,tx.y),(rx.x,rx.y),model.getwalls())

#calcul de la puissance
##PRX=0
##for ray in raystot:
##    if ray.dis != None:
##        PRX=PRX+ray.get_PRX_individuelle(tx)



#ATTENTION ici tx et rx désignent l'émetteur et le récepteur, mais
#dans la fct reflexion ils désignent le tuple contenant la position

#réflexion

GUI(model.getwalls(),xmax,ymax,raystot,ls_PRX_pt_ij,(rxx,rxy))
print(PRX)


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

    









