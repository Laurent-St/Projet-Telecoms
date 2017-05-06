# main
from GUI import GUI
from Model import *
import numpy as np
from fctsmath import *
from Antenna import *
from ref_tr_diff import *
from isinwall import *
from diffraction import *

#taille de la carte et initialisation des murs
xmax=500
ymax=500
model=Model(xmax,ymax)
cat=1
model.setwalls(xmax,ymax, cat)

#ATTENTION ici tx et rx désignent l'émetteur et le récepteur, mais
#dans la fct reflexion ils désignent le tuple contenant la position

"""Calcul sur toute une zone"""
#ATTENTION NE PAS METTRE RECEPTEUR DANS LES MURS

gain=1.6981
txx=450
txy=60
raystot=[]
tx=Antenna(gain,txx,txy)
tx.setpower_emission(0.1) #P_TX=0.1 Watt, voir calcul dans le rapport
PRX=0 #puissance moyenne
#lsPRX=[[0]*xmax]*ymax
lsPRX=np.zeros((ymax+1,xmax+1)) #np.zeros((lignes,colonnes))
#lsPRX est la liste des puissances EN DBM
#MAIS ATTENTION il faut calculer le log après avoir sommé toutes les contributions,
#et pas sommer des logarithmes!!!
for i in range(0,ymax): #i: dimension y
#for i in np.arange(0.1,ymax,0.1):
    print('i=',i)
    for j in range(0,xmax): #j: dimension x
    #for j in np.arange(0.1,xmax,0.1):
        #print('j=',j)
        if isinwall(model.getwalls(),j,i) == False:
            rx=Antenna(gain,i,j) #on crée une antenne réceptrice en chaque point
            rays=reflexion((tx.x,tx.y),(rx.x,rx.y),model.getwalls())
            rays_diff=diffraction(model.getwalls(),model.getaretes(), model.getcoins(),(tx.x,tx.y),(rx.x,rx.y))
            rays.extend(rays_diff)
            ray_direct=onde_directe((tx.x,tx.y),(rx.x,rx.y),model.getwalls())
            #print('ray_direct.dis=',ray_direct.dis)
            lsPRX[i][j]=ray_direct.get_PRX_individuelle(tx) #puissance recue juste au point considéré
            #print('lsPRX[i][j]=',lsPRX[i][j])
            raystot.append(ray_direct)
            for ray in rays:
                raystot.append(ray)
                if ray.dis != None:
                    lsPRX[i][j]=lsPRX[i][j]+ray.get_PRX_individuelle(tx)
            PRX=PRX+lsPRX[i][j]
            lsPRX[i][j]=10*np.log(lsPRX[i][j]/0.001) #on passe en dBm seulement à la fin

#print(lsPRX)

#nbre_pts=xmax*ymax
#PRX=PRX/nbre_pts
#PRX_dBm=10*np.log(PRX/0.001)

GUI(model.getwalls(),xmax,ymax,raystot,lsPRX)

"""Calcul juste en un point
gain=1
txx=450
txy=60
rxx=150
rxy=100
tx=Antenna(gain,txx,txy)
tx.setpower_emission(0.1) #P_TX=0.1 Watt, voir calcul dans le rapport
rx=Antenna(gain,rxx,rxy)
raystot=reflexion((tx.x,tx.y),(rx.x,rx.y),model.getwalls())
rays_diff=diffraction(model.getwalls(),model.getaretes(), model.getcoins(),(tx.x,tx.y),(rx.x,rx.y))
raystot.extend(rays_diff)
print('temp1')
ray_direct=onde_directe((tx.x,tx.y),(rx.x,rx.y),model.getwalls())
print('temp2')
raystot.append(ray_direct)

#calcul de la puissance
PRX=0
##for ray in raystot:
##    if ray.dis != None:
##        PRX=PRX+ray.get_PRX_individuelle(tx)

##PRX_dBm=10*np.log(PRX/0.001)
##print('Puissance moyenne=',PRX)
##print('Puissance moyenne[dBm]=',PRX_dBm)


for ray in raystot:
    if ray.dis != None:
        PRX+=ray.get_PRX_individuelle(tx)

PRX=10*np.log(PRX/0.001) #on passe en dBm seulement à la fin
print(PRX)

#print(lsPRX)
GUI(model.getwalls(),xmax,ymax,raystot,PRX)"""


"""
#test rayonnement ANCIEN
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
