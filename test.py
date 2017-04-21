from test_intersection_vect import *
import numpy as np

xmax = 50
ymax = 50

xtx=10
ytx=15

xrx=25
yrx=32

tx=(xtx,ytx)
rx=(xrx,yrx)

im=[0]*4

im[0]=(2*xmax-xtx,ytx) #right
im[1]=(xtx,-ytx) #up
im[2]=(-xtx,ytx) #left
im[3]=(xtx,2*ymax-ytx)  #bottom

print (line_intersection([(0,0), (0,50)],[im[2],rx]))

##line1=[(-10,0),(50,0)]
##line2=[(0,-10),(0,50)]
##
##print (line_intersection(line1,line2))


