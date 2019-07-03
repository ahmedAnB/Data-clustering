from creation_point import * 
from main import *
from affichage_point import * 
from creation_point import *
from time import clock



def fitting(set_rect1, set_rect2, n):
    """
    computes the probability of a point is in set1 but not in set2
    """
    false_positive = 0
    set_point_1 = tirage_points_set(set_rect1, n)
    for i, pt in enumerate(set_point_1):
        count=1
        for rect in set_rect2:
            if inrectangle(pt, rect):
                count=0
        false_positive += count
        
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
    dimension = 3 
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
    """
    shows the curse of dimension
    """
    nb_point = 1000
    tms, dims = [], []
    
    for dim in range(dim_max):
        print('dimension de calcul : ', dim)
        set_point = creation_point_rectangles(nb_point, nb_point//100, dim)
        t1 = clock()
        ht = mv1_algo(set_point, nb_point//100 )
        t2 = clock()
        tms.append(t2 - t1)
        dims.append(dim)
    
    plt.plot(dims, tms)
    plt.show()

if __name__ == "__main__":
    print("lancement calcul")
    big_test()
    #explosion_dimension(50)
