from random import random, uniform

dimension = 3

def creation_point(n, dimension):
    """
    creates N random in D dimension in the [0, 1[ square
    """
    pts = []
    for i in range(n):   
        pt = []
        for d in range(dimension):
            pt.append(random())
        pts.append(pt)
    return pts

def creation_point_rectangles(nb_point, nb_rectangle, dimension):
    """
    creates nb_points in n rectangles in D dimension
    """
    pts = []
    sommets = creation_point(nb_rectangle, dimension)
    n = nb_point//nb_rectangle
    for j in range(nb_rectangle):
        for i in range(n):
            #print(sommets[j])
            pt = [uniform(sommets[j][k], sommets[j][k]+0.2) for k in range(dimension)]
            pts.append(pt)
    
    return pts


if __name__ == "__main__":
    pts = creation_point(1000, dimension)
    print(pts)
