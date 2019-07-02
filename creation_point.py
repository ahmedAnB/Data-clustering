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

def incercle(pt, center, rayon):
    """
    return True if a point is the circle (center, rayon)
    """
    dist = 0
    for x1, x2 in zip(pt, center):
        dist += (x1 - x2)**2
    return dist <= (rayon**2)

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
            

def creation_point_rectangles_2(nb_point, nb_rectangle, dimension):
    """
    creates nb_points in n rectangles in D dimension
    """
    pts = []
    sommets = creation_point(nb_rectangle, dimension)
    n = nb_point//nb_rectangle
    for j in range(nb_rectangle):
        cote = [uniform(0, 0.5) for k in range(dimension)]

        for i in range(n):
            #print(sommets[j])
            pt = [uniform(sommets[j][k], sommets[j][k] + cote[k]) for k in range(dimension)]
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
