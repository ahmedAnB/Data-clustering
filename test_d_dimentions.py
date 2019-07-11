from creation_point import * 
from main import *
from affichage_point import * 
from creation_point import *
from time import clock
from fonctions_principal import mv1_algo_opti
import numpy
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

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
    n = 2000

    set_point, ensemble_repartition = creation_point_rectangles_2(n, nb_rectangle, dimension, True)
    print("creation_point_rectangles fait")
    set_rectangle = mv1_algo(set_point,nb_rectangle)
    print("algo realisé")

    return fitting(ensemble_repartition, set_rectangle, n), fitting(set_rectangle, ensemble_repartition, n) 

def big_test():
    dimension = 2
    nb_rect_max = 60
    
    nbrs, fits1, fits2 = [], [], []
    for nb_rect in range(10,nb_rect_max):
        print("calcul pour nb_rect = ", nb_rect)
        fit1, fit2 = comparaison_theo_exp(nb_rect, dimension)
        nbrs.append(nb_rect)
        fits1.append(fit1)
        fits2.append(fit2)
        print("sauvegare réussi pour nb_rect =  ", nb_rect)    
    plt.plot(nbrs, fits2, color= 'blue', label = 'faux positif ')
    plt.plot(nbrs, fits1, color = 'red', label = 'faux négatif')
    plt.xlabel('nb de rectangle')
    plt.ylabel('pourcentage erreur')
    plt.show()

def explosion_dimension(dim_mini, dim_max):
    """
    shows the curse of dimension
    """
    print('lacement calcul')
    nb_point = 1000
    nb_carre = 10
    tms, dims = [], []
    save = open('result_algo_2.txt', 'a')
    for dim in range(dim_mini, dim_max):
        print('dimension de calcul : ', dim)
        set_point = creation_point_rectangles_2(nb_point, nb_carre, dim)
        t1 = clock()
        #ht = mv1_algo(set_point, 10 )
        ht = mv1_algo_opti(set_point, nb_carre, distance)
        t2 = clock()
        tms.append(t2 - t1)
        dims.append(dim)
        save.write('\n' + str(dim) + '   '+str(t2 - t1))
        print('ecriture ok')
    save.close()
    
    print(tms, dims)
    plt.plot(dims, tms)
    plt.xlabel('dimension')
    plt.ylabel(' temps de calcul')
    plt.title('calcul evolution temps/dimension pour n = 5000 et eps = 0.2')

def dim_rect_init(dim_mini, dim_max, eps_min, eps_max, eps_pas):
    """
    computes the number the len set_rectangle after the hash table method
    """
    nb_point = 1000
    epss, dims, lens = [], [], []
    save = open('save_dim.txt', 'w')
    for eps in numpy.arange(eps_min, eps_max, eps_pas):
        for dim in range(dim_mini, dim_max):
            print('dimension de calcul : ', dim)
            set_point = creation_point_rectangles(nb_point, 10, dim)
            ht = epsilon_variation_algo(set_point, len(set_point),eps)
            dims.append(dim)
            lens.append(len(ht.keys()))
            epss.append(eps)
            save.write('\n' + str(dim) + ','+str(len(ht.keys()))+','+str(eps))
            print('ecriture ok')
    
    save.close()
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(dims, epss, lens)
    ax.set_xlabel('dimension')
    ax.set_zlabel('longeur table de hachage')
    ax.set_ylabel('epsilon')
    ax.text2D(0.05, 0.95, "Variation longeure HT avec epsilon, dimension, n =  1000", transform=ax.transAxes) 
    plt.show()
   
def dim_rect_mm_graphe(dim_mini, dim_max, eps_min, eps_max, eps_pas):
    """
    computes the number the len set_rectangle after the hash table method
    """
    nb_point = 1000
    epss, dims, lens = [], [], []
    save = open('save_dim.txt', 'w')
    for eps in numpy.arange(eps_min, eps_max, eps_pas):
        len_eps = []
        dims_eps = []
        for dim in range(dim_mini, dim_max):
            print('dimension de calcul : ', dim)
            set_point = creation_point_rectangles(nb_point, 10, dim)
            ht = epsilon_variation_algo(set_point, len(set_point),eps)
            len_eps.append(len(ht.keys()))
            dims_eps.append(dim)
        #print(len_eps, dims_eps)
        lab = "epsilon = " + str(eps)
        plt.plot(dims_eps, len_eps, label = lab)
    
    plt.xlabel('dimension')
    plt.ylabel('lenght hash table')
    plt.title('lenght variation depending on dimension and epsilon, n = 1000')
    plt.legend(loc='lower right') 
    plt.show()
if __name__ == "__main__":
    #big_test()
    #explosion_dimension(2,7)
    dim_rect_mm_graphe(2,160,0.1,1.1,0.1)
