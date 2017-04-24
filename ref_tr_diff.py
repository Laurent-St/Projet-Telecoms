from fctsmath import *
import math as m
def reflexion(tx,rx,xmax,ymax,walls):
    """
    tx et rx sont des tuples contenant la position en x et en y de l'émetteur et du récepteur
    ATTENTION: les recherches des 4 murs ainsi que des pts images, et l'attribution des rayons sont toujours faits dans l'ordre suivant:
    RIGHT, UP, LEFT, DOWN
    """
    
    #1) trouver les 4 murs les plus proches dans les 4 directions
    for wall in walls:
##        minright=100000  #valeur très élevée pour que le premier élément de inter... soit d'office le premier min
##        minup=100000
##        minleft=100000
##        mindown=100000
        interright=[]
        interup=[]
        interleft=[]
        interdown=[]
        wallright=[]
        wallup=[]
        wallleft=[]
        walldown=[]
        imright=[]
        imup=[]
        imleft=[]
        imdown=[]
        if wall.x1>=tx[0] and wall.x1==wall.x2: #murs verticaux à droite de tx
            interright.append(line_intersection([tx,(wall.x1,tx[1])],[(wall.x1,wall.y1),(wall.x2,wall.y2)]))
            wallright.append(wall)
            #calcule l'intersection entre une ligne horizontale partant de tx vers la droite, et le mur
            imright.append((2*wall.x1-tx[0],tx[1]))
##            if abs(interright[0]-tx[0])<minright: #cherche le mur qui a l'intersection la plus proche, cad la difference de x la plus faible
##                minright=abs(interright[0]-tx[0])
##                wallminright=wall
            

            
        elif wall.y1>=tx[1] and wall.y1==wall.y2: #murs horizontaux au-dessus de tx
            interrup.append(line_intersection([tx,(tx[0],wall.y1)],[(wall.x1,wall.y1),(wall.x2,wall.y2)]))
            wallup.append(wall)
            #calcule l'intersection entre une ligne verticale partant de tx vers le haut, et le mur
            imup.append((tx[0],2*wall.y1-tx[1]))
##
##            if abs(interrup[1]-tx[1])<minup:
##                minup=abs(interrup[1]-tx[1])
##                wallminup=wall
            
        elif wall.x1<=tx[0] and wall.x1==wall.x2: #murs verticaux à gauche de tx
            interleft.append(line_intersection([tx,(wall.x1,tx[1])],[(wall.x1,wall.y1),(wall.x2,wall.y2)]))
            wallleft.append(wall)
            imleft.append((2*wall.x1-tx[0],tx[1]))

##            if abs(interleft[0]-tx[0])<minleft:
##                minleft=abs(interleft[0]-tx[0])
##                wallminleft=wall
            
        else: #murs horizontaux en-dessous de tx
            interdown.append(line_intersection([tx,(tx[0],wall.y1)],[(wall.x1,wall.y1),(wall.x2,wall.y2)]))
            walldown.append(wall)
            imdown.append((tx[0],2*wall.y1-tx[1]))

##            if abs(interdown[1]-tx[1])<mindown:
##                mindown=abs(interdown[1]-tx[1])
##                wallmindown=wall

##    reswall=[wallminright,wallminup,wallminleft,wallmindown]
        

    #2) trouver les points images: comprendre les distances à l'aide d'un dessin
##    im=[0]*4
##    im[0]=(2*reswall[0].x1-tx[0],tx[1])
##    im[1]=(tx[0],2*reswall[1].y1-tx[1])
##    im[2]=(2*reswall[2].x1-tx[0],tx[1])
##    im[3]=(tx[0],2*reswall[3].y1-tx[1])

    #3) pts d'intersection entre mur et droite ptimage-rx, et tracer les rayons
##    pt_inter=[]
    rays=[] #2 fois plus grande que pt_inter car 2 rayons par réflexion
##    j=0 #compteur pour les rayons
##    for i in range (0,4):
##        pt_inter[i]=line_intersection([im[i],rx],[(reswall[i].x1,reswall[i].y1),(reswall[i].x2,reswall[i].y2)])
##        rays[j]=[tx,pt_inter[i]] #un rayon=une ligne cad [tuple,tuple]
##        j=j+1
##        rays[j]=[pt_inter[i],rx]
##        j=j+1
    pt_inter_right=[]
    for i in range(0,length(wallright)):
        pt_inter_right.append(line_intersection([imright[i],rx],[(wallright[i].x1,wallright[i].y1),(wallright[i].x2,wallright[i].y2)]))
        line1=[tx,pt_inter_right[i]]
        ray1=Ray(tx[0],tx[1],pt_inter_right[i][0],pt_inter_right[i][1],1) #coef est mis à 1
        ray2=Ray(pt_inter_right[i][0],pt_inter_right[i][1],rx[0],rx[1])
        theta_i= m.pi/2 - calcAngle(ray1, wallright[i])
        ray2.coef=ray2.coef*wallright[i].get_coeff_reflex(theta_i)
        rays.append(ray1)
        
    pt_inter_up=[]
    i=0
    for i in range(0,length(wallup)):
        pt_inter_up.append(line_intersection([imup[i],rx],[(wallup[i].x1,wallup[i].y1),(wallup[i].x2,wallup[i].y2)]))

    pt_inter_left=[]
    i=0
    for i in range(0,length(wallleft)):
        pt_inter_left.append(line_intersection([imleft[i],rx],[(wallleft[i].x1,wallleft[i].y1),(wallleft[i].x2,walllef[i].y2)]))

    pt_inter_down=[]
    i=0
    for i in range(0,length(walldown)):
        pt_inter_down.append(line_intersection([imdown[i],rx],[(walldown[i].x1,walldown.y1),(walldown[i].x2,walldown[i].y2)]))

    return rays

    #4) Reflexion double: A FAIRE

    
    
    
    
    
    
    
    
