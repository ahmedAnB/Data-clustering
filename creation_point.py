from random import random, uniform
from main import distance_lp
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

def incercle(pt, center, rayon):
    """
    return True if a point is the circle (center, rayon)
    """
    dist = 0
    for x1, x2 in zip(pt, center):
        dist += (x1 - x2)**2
    
    return dist <= (rayon**2)

def inrectangle(pt, R):
    '''
    return True if a point is a rectangle
    '''
#    print(R)
    lower, upper = R[0], R[1]
#    print(len(lower), len(pt))
    for i, x in enumerate(pt):
        if not(x>lower[i] and x<upper[i]):
            return False
    
    return True

def creation_point_sur_cercle(nb_point, nb_cercle, dimension):
    """
    creates points on a circle
    """
    
    pts = []
    n = nb_point//nb_cercle

    for j in range(nb_cercle):
        rayon = uniform(0.1, 0.3)
        #rayon = 1
        center = [random() for k in range(dimension)]
        i = 0
        while i < n:
            pt = [uniform(center[j]-rayon, center[j] + rayon) for j in range(dimension)]
            if incercle(pt, center, rayon):
                distance_c_pt = distance_lp(pt, center)
                pt_1 = [center[i] + (xi - center[i]) * rayon / distance_c_pt  for i, xi in enumerate(pt)] 
                pts.append(pt_1)
                i+=1
    return pts
    
def creation_point_cercle(nb_point, nb_cercle, dimension):
    """
    creates random circles and places points in these circles
    """
    
    pts = []
    n = nb_point//nb_cercle

    for j in range(nb_cercle):
        rayon = uniform(0.1, 0.3)
        center = [random() for k in range(dimension)]
        i = 0
        while i < n:
            pt = [uniform(center[j]-rayon, center[j] + rayon) for j in range(dimension)]
            if incercle(pt, center, rayon):
                pts.append(pt)
                i+=1
    return pts
            
def tirage_points_set(set_rectangle, nb_point):
    """
    creates n points in set_rectangle
    """
    n = nb_point//len(set_rectangle)
    pts = []
#    print(set_rectangle)
    for rect in set_rectangle:
#        print(rect)
        R, S = rect[0], rect[1]
        for i in range(n):
            pt = [uniform(R[i], S[i]) for i in range(len(R))]
            pts.append(pt)
    return pts

def creation_point_rectangles_2(nb_point, nb_rectangle, dimension, boole = False):
    """
    creates nb_points in n rectangles with random size in D dimension    
    """
    pts, cotes = [], []

    sommets = creation_point(nb_rectangle, dimension)
    n = nb_point//nb_rectangle
    for j in range(nb_rectangle):
        cote = [uniform(0, 0.5) for k in range(dimension)]
        cotes.append(cote)
        for i in range(n):
            #print(sommets[j])
            pt = [round(uniform(sommets[j][k], sommets[j][k] + cote[k]), 2) for k in range(dimension)]
            pts.append(pt)
    if boole:
        repartition_rect = []
        for k, R in enumerate(sommets):
            rect, cote = [], cotes[k]
            S = [xi + cote[i] for  i, xi in enumerate(R)]
            rect.append(R)
            rect.append(S)
            repartition_rect.append(rect)
        return pts, repartition_rect
    
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
