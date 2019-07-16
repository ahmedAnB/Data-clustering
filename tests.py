from ceation_point import * 
from main import *
from affichage_point import * 
from creation_point import *
from time import clock
from fonctions_principal import mv1_algo_opti
import numpy
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from distance_use import *


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
                break
        false_positive += count
        
        print("point " ,i , " fait")
    print(" fitting fait ")
    return false_positive/n


def experience_between_theoritical_and_learned_cluster(nb_rectangle, dimension, n, graphic_started = False, epsilon = None):
    """
    computes the false postive and false negative rate of the learned cluster
    """
    
    n = 300

    set_point, starting_rectangle = creation_point_rectangles_2(n, nb_rectangle, dimension, True)
    print("creation_point_rectangles fait")
    if epsilon is not None:
        learn_rectangle = mv1_algo_opti(set_point, nb_rectangle, distance, epsilon)
    else:
        learn_rectangle = mv1_algo_opti(set_point, nb_rectangle, distance)
    if graphic_started:
        afficher_plsr_pts_rect_1(starting_rectangle, set_point, 1)
    
    print("algo realisé")

    false_positive = fitting(learn_rectangle,starting_rectangle, 1000) 
    false_negative = fitting(starting_rectangle, learn_rectangle, 1000)
    return false_negative, false_positive


def evolution_error_side_grid(nb_point, nb_rectangle, dimension, eps_min, eps_max, eps_step):
    """
    computes the evolution of error depedind on the original side of cells used for the hash table
    using mv1_algo
    """
    false_positives, false_negatives, epss =[], [], []
    for eps in arange(eps_min, eps_max, eps_step):
        fn , fp = experience_between_theoritical_and_learned_cluster(nb_rectangle, dimension, nb_point, False, eps)
        false_negatives.append(fn)
        false_positives.append(fp)
        epss.append(eps)
    plt.plot(epss, false_positives, label = 'false_positives')
    plt.plot(epss, false_negatives, label = 'false_negatives')
    plt.xlabel('cells sides')
    plt.ylabel('errors rate')
    plt.title(" evolution of the errors rate depending of hash table's cells size")


def evolution_error_cluster(n_point, dimension, nb_rect_min, nb_rect_max, nb_rect_step):
    """
    computes the evolution between the number of cluster initially and the error rate
    """
    
    nbrs, fits1, fits2 = [], [], []
    for nb_rect in range(nb_rect_min, nb_rect_max, nb_rect_step):
        print("calcul pour nb_rect = ", nb_rect)
        fit1, fit2 = experience_between_theoritical_and_learned_cluster(nb_rect, dimension, n_point, False)
        nbrs.append(nb_rect)
        fits1.append(fit1)
        fits2.append(fit2)
        print("sauvegare réussi pour nb_rect =  ", nb_rect)    
    print(' rate false positif ', fits2)
    print('rate false negatif', fits1)
    plt.plot(nbrs, fits2, color= 'blue', label = 'false positif ')
    plt.plot(nbrs, fits1, color = 'red', label = 'false negatif')
    plt.xlabel('Number of Rectangle')
    plt.ylabel('Error Rate')
    plt.title("evolution of the error rate depending on the number of cluster used initially")
    plt.show()

def explosion_dimension(dim_mini, dim_max, nb_point, nb_carre):
    """
    shows the curse of dimension
    cad increasing time computation with dimension
    """
    print('lacement calcul')
    tms, dims = [], []
    
    for dim in range(dim_mini, dim_max):
        print('dimension de calcul : ', dim)
        set_point = creation_point_rectangles_2(nb_point, nb_carre, dim)
        t1 = clock()
        #ht = mv1_algo(set_point, 10 )
        ht = mv1_algo_opti(set_point, nb_carre, distance, 0.2)
        t2 = clock()
        tms.append(t2 - t1)
        dims.append(dim)
        save = open('result_algo_2.txt', 'a')
        save.write('\n' + str(dim) + '   '+str(t2 - t1))
        print('ecriture ok')
        save.close()
    
    print(tms, dims)
    plt.plot(dims, tms)
    plt.xlabel('Dimension')
    plt.ylabel(' Computing time')
    plt.title(' Evolution time and dimension for n = 5000 et eps = 0.2')

def experience_isolated_points_3D(dim_mini, dim_max, eps_min, eps_max, eps_pas, nb_point):
    """
    computes the number the len set_rectangle after the hash table method
    experience that for a dimension the points are isolated
    the result is a graphe in 3D
    """
    epss, dims, lens = [], [], []
    save = open('save_dimi_opti.txt', 'w')
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
   

def dim_rect_mm_graphe(dim_mini, dim_max, eps_min, eps_max, eps_pas, nb_point):
    """
    computes the number the len set_rectangle after the hash table method
    experience that for a dimension the points are isolated
    the result is a graphe in 2D  
    """
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


def evolution_nb_rectangle_cost(nb_point):
    """
    shows the evolution of the cost depending on the numbered of merged rectangle in the cluster at each step
    """
    set_point = creation_point_rectangles(nb_point, nb_rectangle, dimension)
    Y, X = evolution_cost(set_point, 0.05)
    afficher_XY(X, Y)
    
 
def test_merge():
    """
    test if two ractangles merge well
    """

    R = ([0.29, 0.17], [0.38, 0.41])
    S = ([0.51, 0.00], [0.96, 0.47])
    RUS = merge_rectangle((R,S), [R, S])
    #print(RUS)
    afficher_plsr_pts_rect([R, S, RUS[0] ], None)


