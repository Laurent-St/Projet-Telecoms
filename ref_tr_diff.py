from fctsmath import *

def reflexion(tx,rx,xmax,ymax,walls):
    """
    tx et rx sont des tuples contenant la position en x et en y de l'émetteur et du récepteur
    ATTENTION: les recherches des 4 murs ainsi que des pts images, et l'attribution des rayons sont toujours faits dans l'ordre suivant:
    RIGHT, UP, LEFT, DOWN
    """
    
    #1) trouver les 4 murs les plus proches dans les 4 directions
    for wall in walls:
        minright=100000  #valeur très élevée pour que le premier élément de inter... soit d'office le premier min
        minup=100000
        minleft=100000
        mindown=100000
        if wall.x1>=tx[0] and wall.x1==wall.x2: #murs verticaux à droite de tx
            interright=line_intersection([tx,(wall.x1,tx[1])],[(wall.x1,wall.y1),(wall.x2,wall.y2)])
            #calcule l'intersection entre une ligne horizontale partant de tx vers la droite, et le mur
            if abs(interright[0]-tx[0])<minright: #cherche le mur qui a l'intersection la plus proche, cad la difference de x la plus faible
                minright=abs(interright[0]-tx[0])
                wallminright=wall
            
        elif wall.y1>=tx[1] and wall.y1==wall.y2: #murs horizontaux au-dessus de tx
            interrup=line_intersection([tx,(tx[0],wall.y1)],[(wall.x1,wall.y1),(wall.x2,wall.y2)])
            #calcule l'intersection entre une ligne verticale partant de tx vers le haut, et le mur
            if abs(interrup[1]-tx[1])<minup:
                minup=abs(interrup[1]-tx[1])
                wallminup=wall
            
        elif wall.x1<=tx[0] and wall.x1==wall.x2: #murs verticaux à gauche de tx
            interleft=line_intersection([tx,(wall.x1,tx[1])],[(wall.x1,wall.y1),(wall.x2,wall.y2)])
            if abs(interleft[0]-tx[0])<minleft:
                minleft=abs(interleft[0]-tx[0])
                wallminleft=wall
            
        else: #murs horizontaux en-dessous de tx
            interdown=line_intersection([tx,(tx[0],wall.y1)],[(wall.x1,wall.y1),(wall.x2,wall.y2)])
            if abs(interdown[1]-tx[1])<mindown:
                mindown=abs(interdown[1]-tx[1])
                wallmindown=wall

    reswall=[wallminright,wallminup,wallminleft,wallmindown]

    #2) trouver les points images: comprendre les distances à l'aide d'un dessin
    im=[0]*4
    im[0]=(2*reswall[0].x1-tx[0],tx[1])
    im[1]=(tx[0],2*reswall[1].y1-tx[1])
    im[2]=(2*reswall[2].x1-tx[0],tx[1])
    im[3]=(tx[0],2*reswall[3].y1-tx[1])

    #3) pts d'intersection entre mur et droite ptimage-rx, et tracer les rayons
    pt_inter=[0]*4
    rays=[0]*8 #2 fois plus grande que pt_inter car 2 rayons par réflexion
    j=0 #compteur pour les rayons
    for i in range (0,4):
        pt_inter[i]=line_intersection([im[i],rx],[(reswall[i].x1,reswall[i].y1),(reswall[i].x2,reswall[i].y2)])
        rays[j]=[tx,pt_inter[i]] #un rayon=une ligne cad [tuple,tuple]
        j=j+1
        rays[j]=[pt_inter[i],rx]
        j=j+1

    return rays

    #4) Reflexion double: A FAIRE

    
    
    
    
    
    
    
    
