from timeit import timeit
from sys import argv
from math import sqrt
from distance_use import *

from affichage_point import *


def rect_center(S):
    """
    computes the center of a rectangle
    """
    center = []
    dimension = len(S[0])
    for i in dimension:
        center.append(abs(S[0][i] - S[1][i])/2)
    return center


def minimum_rect(set_point, boole = False):
    """
    return the bouding box of a set of point
    """
    dimension = len(set_point[0][0])
    R_min, S_max = [], []
    for i in range(dimension):
        L = [point[0][i] for point in set_point]
        R_min.append(min(L))
        S_max.append(max(L))
    if boole:
        return([R_min,S_max])
    else:
        return((R_min,S_max))


def creation_hash_table(set_point, epsilon):
    """
    return the hash table complete
    The algo computes for each point a  key (=lower) and places this point in the corresponding position in the hash table
    it means that the algorithme creates an epsilon-size grid and places every point in its corresponding square
    """
    hash_table = {}#initialisation
    dimension = len(set_point[0][0])
    
    for point in set_point:#each point
        pt1 = point[0]
        lower = tuple(int(pt1[i]/epsilon) for i in range(dimension))#compute key
        if lower in hash_table.keys():#add the point in the HT 
            hash_table[lower].append(point)
        else:
            hash_table[lower] = [point]

    return hash_table


def stop_condition(hash_table, lenght_set_point):
    """
    return True if the stopping condition is respected
    the stopping condition is :
    it exists a key for card(HT[key]) <= sqrt(n)
    """
    sqrt_n = sqrt(lenght_set_point)
    if hash_table == {}:
        return False
    elif len(hash_table.keys()) <= sqrt_n:
        return True
    else:
        return False


def stop_condition_1(hash_table, lenght_set_point, epsilon):
    """
    return True if the stopping condition is respected
    the stopping condition is :
    it exists a key for card(HT[key]) <= sqrt(n)
    """

    sqrt_n = sqrt(lenght_set_point)
    if hash_table == {}:
        return False
    elif epsilon < 0.05:
        return True
    else:
        return False


def epsilon_variation_algo(set_point, inutile,  epsilon = 0.1):
    """
    the algorithm creates the Hash table correspponding to a set of point
    """
    #initialisation
    hash_table = {}
    hash_table = creation_hash_table(set_point, epsilon)

    return hash_table


def premiers_rectangles(set_point, epsilon = 0.1):
    '''
    return the first rectangles of an set of point juste after using hash table algorithm
    '''
    
    hash_table = epsilon_variation_algo(set_point, epsilon)
    set_rectangle = [minimum_rect(hash_table[key], True) for key in hash_table.keys()]
    
    return set_rectangle


def naive_nearest_neighboor(set_rectangle, distance_used = distance):
    """
    This algorithme find the nearest neigboor by testing every possible combination of rectangle
    """
    n = len(set_rectangle)
    
    if len(set_rectangle) == 1:
        return None
    
    #initialisation
    min_dist = distance(set_rectangle[0], set_rectangle[1])
    nearest_neighboor = (set_rectangle[0], set_rectangle[1])
    
    #testing every combination
    for i in range(n):
        for j in range(i+1,n):
            dist = distance_used(set_rectangle[i], set_rectangle[j])
            if dist < min_dist:
                nearest_neighboor = (set_rectangle[i], set_rectangle[j])
                min_dist = dist

    return nearest_neighboor


def merge_bonus(points):
    """
    computes the potential bonus for merging two points
    """
    if points == None:
        return 0

    R = points[0]
    S = points[1]
    
    
    dR = distance([R[0]], [R[1]])
    dS = distance([S[0]], [S[1]])
    dR_S = distance(R, S)
    
    return dR_S - (dS + dR)


def merge_rectangle(nearest_neighboor, set_rectangle, option_return_rectangle = False):
    """
    merge the 2 rectancle in nearest_neigboor and can return it without updating set_rectangle
    """
    #initialisation
    R1 = nearest_neighboor[0]
    S1 = nearest_neighboor[1]
    set_rectangle1 = set_rectangle.copy()
    dimension = len(R1[0])
    p_min = []
    p_max = []
    #merge the two rectangle
    for i in range(dimension):
        p_min.append(min([R1[0][i], R1[1][i], S1[0][i], S1[1][i]]))
        p_max.append(max([R1[0][i], R1[1][i], S1[0][i], S1[1][i]]))
    
    if option_return_rectangle:
        return [p_min, p_max]
    #update the set of rectangles
    set_rectangle1.remove(S1)
    set_rectangle1.remove(R1)
    set_rectangle1.append([p_min, p_max])
    
    return(set_rectangle1)


def mv1_algo(set_point, nb_rectangle, option_ht = True, graphic_end = False, epsilon = 0.1):
    """
    working version of previous algorithm
    """
    if option_ht:
        #creates the hash table
        hash_table = epsilon_variation_algo(set_point, len(set_point), epsilon)
        min_nb_rectangle = sqrt(len(set_point))
        set_rectangle = [minimum_rect(hash_table[key]) for key in hash_table.keys()]
    
    else:
        set_rectangle = set_point

    while len(set_rectangle) > nb_rectangle:
        #apply the nearest neighboor algortihm
        nearest_neighboor = naive_nearest_neighboor(set_rectangle, distance_lp)
        set_rectangle = merge_rectangle(nearest_neighboor, set_rectangle)
    
    if graphic_end:
        afficher_plsr_pts_rect_1(set_rectangle, set_point, 0)
    
    return set_rectangle
    

def sbs_m_algo(set_point, eta):
    """
    executes step by step the master_algo
    """
    #find the perfect hash table
    hash_table = epsilon_variation_algo(set_point, len(set_point))
    
    #define the minimal number of rectangle
    min_nb_rectangle = sqrt(len(set_point))
    
    #convert the hash table in a set of rectangles
    set_rectangle = [minimum_rect(hash_table[key]) for key in hash_table.keys()]
    #apply the NN algorithm while the condition is not False
    i = 0 
    while True:
        #find the NN
        i+=1
        afficher_plsr_pts_rect_1(set_rectangle, set_point, i)
        i+=1
        nearest_neighboor = naive_nearest_neighboor(set_rectangle)
        afficher_plsr_pts_rect_2(set_rectangle, set_point, i, nearest_neighboor)
        
        if len(set_rectangle) > 2:
            #merge the NN
            set_rectangle = merge_rectangle(nearest_neighboor, set_rectangle)
        #stop the algorithm
        else:
            return set_rectangle


def master_algorithme(set_point, heta):
    """
    First implentation of the two precedent algorithm
    """
    #find the perfect hash table
    hash_table = epsilon_variation_algo(set_point, len(set_point))
    
    #define the minimal number of rectangle
    min_nb_rectangle = sqrt(len(set_point))
    
    #convert the hash table in a set of rectangles
    set_rectangle = [minimum_rect(hash_table[key]) for key in hash_table.keys()]
    #apply the NN algorithm while the condition is not False
    i = 0 
    while True:
        #find the NN
        afficher_plsr_pts_rect_1(set_rectangle, None, i)
        nearest_neighboor = naive_nearest_neighboor(set_rectangle)
        i+=1
        
        if len(set_rectangle) > 2:
            #merge the NN
            set_rectangle = merge_rectangle(nearest_neighboor, set_rectangle)
        #stop the algorithm
        else:
            return set_rectangle


def evolution_cost(set_point, eta):
    """
    return the evoluution of the cost depending on the number of cluster learned
    """
    #find the perfect hash table
    hash_table = epsilon_variation_algo(set_point, len(set_point))
    
    #define the minimal number of rectangle
    min_nb_rectangle = sqrt(len(set_point))
    couts = []
    valeur_nb_rectangle = []

    #convert the hash table in a set of rectangles
    set_rectangle = [minimum_rect(hash_table[key]) for key in hash_table.keys()]


    #apply the NN algorithm while the condition is not False
    i = 0 
    while True:
        #find the NN
        #afficher_plsr_pts_rect_1(set_rectangle, None, i)
        nearest_neighboor = naive_nearest_neighboor(set_rectangle)
        i+=1
        couts.append(cost_rectangle(set_rectangle))
        valeur_nb_rectangle.append(len(set_rectangle))

        if len(set_rectangle) > 2:
            #merge the NN
            set_rectangle = merge_rectangle(nearest_neighboor, set_rectangle)
        #stop the algorithm
        else:
            return couts, valeur_nb_rectangle


def algo_avec_variation_heta(set_point):
    """
    the algo executes for diffents values of heta
    and computes the evolution of the cost depending on heta
    """
    #initialisation
    heta = 1
    couts = []
    hetas = []
    sets = []

    while heta > 0.1:
        #apply the algoritm for heta
        set_rectangle = master_algorithme(set_point, heta)
        
        #compute the cost of the set of rectangle
        cout_rectangle = cost_rectangle(set_rectangle)
        
        #save values of heta and cost, and the set of rectangle
        hetas.append(heta)
        couts.append(cout_rectangle)
        sets.append(set_rectangle)
        
        #decrease the value of heta
        heta -=10**-1
    
    return hetas, couts, sets


