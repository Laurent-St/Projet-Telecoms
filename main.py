# main
from GUI import GUI
from Model import *

xmax=500
ymax=500

model=Model(xmax,ymax)
cat=2
model.setwalls(xmax,ymax, cat)
model.setmatrice()

GUI(model.getwalls(),xmax,ymax)
