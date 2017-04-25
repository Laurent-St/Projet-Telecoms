##
##from Wall import*
##
##wall = Wall(1,1,0,0,1)
##print(wall.get_coeff_trans(np.pi/8,0.02)+wall.get_coeff_reflex(np.pi/8,0.02))
##
##

def intersection(s1, s2):
       segment_endpoints = []
       left = max(min(s1[0][0], s1[1][0]), min(s2[0][0], s2[1][0]))
       right = min(max(s1[0][0], s1[1][0]), max(s2[0][0], s2[1][0]))
       top = max(min(s1[0][1], s1[1][1]), min(s2[0][1], s2[1][1]))
       print(top)
       bottom = min(max(s1[0][1], s1[1][1]), max(s2[0][1], s2[1][1]))
        
       if top > bottom or left > right:
          segment_endpoints = []
          print ('NO INTERSECTION')
          return segment_endpoints
        
       elif top == bottom and left == right:
          segment_endpoints.append(left)
          segment_endpoints.append(top)

          res=(top,left)
          
          print ('POINT INTERSECTION')
          return res
    
       else:	
          segment_endpoints.append(left)
          segment_endpoints.append(bottom)
          segment_endpoints.append(right)
          segment_endpoints.append(top)
          print ('SEGMENT INTERSECTION')
          res=(right,top)
          return res

