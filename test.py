from fctsmath import *
import math as m

line1=[(0,-2),(1,1)]
line2=[(0,0),(2,0)]

theta1=calcAngle(line1,line2)
#t1deg=theta1*360/(2*m.pi)
print(theta1)
x1=abs(m.cos(theta1))
print(x1)

line3=[(1,1),(2,-2)]
line4=[(0,0),(2,0)]

theta2=calcAngle(line3,line4)
#t2deg=theta2*360/(2*m.pi)
x2=abs(m.cos(theta2))
print(x2)
print(theta2)
