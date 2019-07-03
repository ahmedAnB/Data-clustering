from creation_point import * 
from main import *
from affichage_point import * 
from creation_point import *

def fitting(set_rect1, set_rect2, n):
    """
    computes the probability of a point is in set1 but not in set2
    """
    false_positive = 0
    set_point_1 = tirage_points_set(set_rect1, n)
    for i, pt in enumerate(set_point_1):
        for rect in set_rect2:
            if not(inrectangle(pt, rect)):
                false_positive += 1
        print("point " ,i , " fait")
    print(" fitting fait ")
    return false_positive/n



def comparaison_theo_exp(nb_rectangle, dimension):
    n = 1000

    set_point, ensemble_repartition = creation_point_rectangles_2(n, nb_rectangle, dimension, True)
    print("creation_point_rectangles fait")
    set_rectangle = mv1_algo(set_point,nb_rectangle)
    print("algo realisé")
    

    return fitting(ensemble_repartition, set_rectangle, n), fitting(set_rectangle, ensemble_repartition, n) 

def big_test():
    dimension = 4 
    nb_rect_max = 20
    
    nbrs, fits1, fits2 = [], [], []
    for nb_rect in range(10,nb_rect_max):
        print("calcul pour nb_rect = ", nb_rect)
        fit1, fit2 = comparaison_theo_exp(nb_rect, dimension)
        nbrs.append(nb_rect)
        fits1.append(fit1)
        fits2.append(fit2)
        print("sauvegare réussi pour nb_rect =  ", nb_rect)    
    plt.plot(nbrs, fits1)
    plt.plot(nbrs, fits2)
    plt.show()

def explosion_dimension(dim_max):
    nb_point = 10
    for i in dim_max:
        t1 = time.time()
        set_rectangle = mv1_algo(set_point, dimension)
if __name__ == "__main__":
    print("lancement calcul")
    big_test()
