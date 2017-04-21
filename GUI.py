
import numpy as np
import matplotlib as mp
from graphics import *
from Wall import Wall

def GUI(walls,xmax,ymax, rays):
    "L'origine des coordonnées (x=0,y=0) est en haut à gauche"
    "ATTENTION quand on accède à une matrice c'est colonnes puis lignes"
    "ATTENTION le index commencent en (0,0)"
    
    "Génère les murs de la maison d'Alexandre: xmax=500, ymax=998"
    "Chaque porte fait 83 éléments"

    "Un 0 représente un élément sans rien, un 1 de la brique, 2 béton et 3 une cloison"

    #tracé des murs
    win=GraphWin('Window',xmax,ymax)  #objet prédéfini pour initialiser la fenetre avec Graphics
    
    for wall in walls:
        
        p1=Point(wall.x1,wall.y1) #on fait *0.5 pour que tout s'affiche dans la fenetre
        p2=Point(wall.x2,wall.y2)
        line=Line(p1,p2)
        line.draw(win)
        if wall.mat==1:
            line.setOutline('black')
        elif wall.mat==2:
            line.setOutline('red')
        elif wall.mat==3:
            line.setOutline('blue')

    for ray in rays:
        line = Line(Point(ray[0][0],ray[0][1]), Point(ray[1][0],ray[1][1]))
        line.draw(win)
            
##    while(1):
##        clickpoint = win.checkMouse()
##        if (clickpoint!=None):
##            print(clickpoint)


    
            
            
    

#hlines= lignes horizontales
#vlines= lignes verticales
