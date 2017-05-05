import numpy as np
import scipy as sc
import math as m
from fctsmath import*
from Ray import*
from Model import*
from Wall import*


#Calcul du coefficient de diffraction

#Vitesse de la lumière
c=3*10**8
#Nombre d'onde
beta = (2*m.pi*2.45*10**9)/c

       
#Valeurs d'angles en RADIANS       
def get_coeff_diff(s,s_p, phi,phi_p):
    
    L = s*s_p/(s+s_p)
    delta = m.pi - (phi-phi_p)
    x = 2*beta*L*(m.sin(delta/2)**2)
    
    #La fonction special.fresnel(z) renvoie : check "https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.special.fresnel.html"
    C = sc.special.fresnel(m.sqrt(2*x/m.pi))[1]
    S = sc.special.fresnel(m.sqrt(2*x/m.pi))[0]
    integ = m.sqrt(m.pi/2)*((1-1j)/2 - (C - 1j*S))
    F_T = 2*1j*m.sqrt(x)*np.exp(1j*x)*integ
    A = 2*m.sqrt(2*m.pi*beta*L)
    B = np.exp(-1j*m.pi/4)
    D = -(B/A) *(F_T/m.sin(delta/2))
    
   
    return np.absolute(D)


#Calcul des paramètres de la diffraction
def calcul_param_diff(vect_wall,vect_tx,vect_rx,arete,rays,tx,rx):
    phi_p = calc_angle_diff(vect_wall,vect_tx)
    phi = 2*np.pi - calc_angle_diff(vect_wall,vect_rx)
    s_p = dis_eucl(tx,arete)
    s = dis_eucl(rx,arete)
    ray1 = Ray(tx[0],tx[1], arete[0], arete[1], 1, None)
    ray2 =  Ray(arete[0], arete[1], rx[0],rx[1], 1, 1)
    ray2.coef = ray2.coef*get_coeff_diff(s,s_p, phi,phi_p)
    ray2.dis = ray2.dis*(s+s_p)
    rays.append(ray1)
    rays.append(ray2)
    
    
#Va donner les rayons diffractés

def diffraction(walls, aretes, coins, tx, rx):
    rays =[]
    #D'abord, on va créer la liste des aretes, avec lesquels il y aura diffraction
    i=0
    j=0
    while(i<len(aretes)):
        for wallbis in walls:
            if((wallbis.x1,wallbis.y1)== aretes[i] or (wallbis.x2, wallbis.y2)== aretes[i]):
                
                if((wallbis.x1,wallbis.y1)!=aretes[i]):
                    vect_wall = [wallbis.x1 - aretes[i][0], wallbis.y1 - aretes[i][1]]
                    vect_tx = [tx[0]-aretes[i][0], tx[1]-aretes[i][1]]
                    vect_rx = [rx[0]-aretes[i][0], rx[1]-aretes[i][1]]
                    calcul_param_diff(vect_wall,vect_tx,vect_rx,aretes[i],rays,tx,rx)
                    
                
                elif ((wallbis.x2, wallbis.y2) != aretes[i]):
                    vect_wall = [wallbis.x2 - aretes[i][0], wallbis.y2 - aretes[i][1]]
                    vect_tx = [tx[0]-aretes[i][0], tx[1]-aretes[i][1]]
                    vect_rx = [rx[0]-aretes[i][0], rx[1]-aretes[i][1]]
                    calcul_param_diff(vect_wall,vect_tx,vect_rx,aretes[i],rays,tx,rx)
        i+=1
        
        #Pour la diffraction avec les coins, on calcule la diffration avec l'arete d'un mur (formant la bissectrice du coin)
        #située au meme point que le coin
        
    while (j<len(coins)):
        #On définit les vecteurs représentant toutes les bissectrices possibles
        vect_bissec_1 = [-1,1]
        vect_bissec_2 = [1,1]
        vect_bissec_3=[1,-1]
        vect_bissec_4  = [-1,-1]
        angles =[]
        #On calcule l'angle entre le vecteur allant du coin au récepteur et les bissectrices, on choisit celle donnant le plus petit angle
        vect_tx = [tx[0]-coins[j][0],tx[1]-coins[j][1]]
        vect_rx = [rx[0]-coins[j][0], rx[1]-coins[j][1]]
        angle_1 = calc_angle_diff(vect_tx, vect_bissec_1)
        angle_2 = calc_angle_diff(vect_tx, vect_bissec_2)
        angle_3 = calc_angle_diff(vect_tx, vect_bissec_3)
        angle_4 = calc_angle_diff(vect_tx, vect_bissec_4)
        angles.append(angle_1)
        angles.append(angle_2)
        angles.append(angle_3)
        angles.append(angle_4)
        
        angle_min = min(angles)
                
        #Si l'angle le plus faible est le premier, on doit prendre le vecteur opposé à vect_bissec_1
        if (angle_min == angles[0]):
            
            vect_wall = vect_bissec_3
            calcul_param_diff(vect_wall,vect_tx,vect_rx,coins[j],rays,tx,rx)
        #Si l'angle le plus faible est le second, on doit prendre le vecteur opposé à vect_bissec_2
        if(angle_min == angles[1]):
            vect_wall = vect_bissec_4
            calcul_param_diff(vect_wall,vect_tx,vect_rx,coins[j],rays,tx,rx)
        #Si l'angle le plus faible est le troisième, on doit prendre le vecteur opposé à vect_bissec_3
        if(angle_min == angles[2]):
            vect_wall = vect_bissec_1
            calcul_param_diff(vect_wall,vect_tx,vect_rx,coins[j],rays,tx,rx)
        #Si l'angle le plus faible est le quatrième, on doit prendre le vecteur opposé à vect_bissec_4
        if(angle_min == angles[3]):
            vect_wall = vect_bissec_2
            calcul_param_diff(vect_wall,vect_tx,vect_rx,coins[j],rays,tx,rx)


        j+=1        
    return rays

