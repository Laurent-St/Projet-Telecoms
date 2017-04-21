
from Wall import*

wall = Wall(1,1,0,0,1)
print(wall.get_coeff_trans(np.pi/8,0.02)+wall.get_coeff_reflex(np.pi/8,0.02))



