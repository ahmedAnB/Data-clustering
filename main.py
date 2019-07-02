from timeit import timeit
from sys import argv
from math import sqrt

from affichage_point import *

#declaration des constantes

heta = 10**-5
dimension =2 


def volumetric_cost(R, S = None):
    """
    computes the volume of a Rectangle R
    """
    if S is None:
        if not(isinstance(R[0],list)):
            return 0
        else:
            result = 0
            for xi_lower, xi_upper in zip(R[0],R[1]):
                result *= abs(xi_upper - xi_lower)
            return result
    else:
        return abs(volumetric_cost(R) - volumetric_cost(S))


def merge_gain_volumme(R, S):
    """
    Computes the volume created by merging this 2 rectangles
    """
    return volumetric_cost(merge(R,S)) - volumetric_cost(R) - volumetric_cost(S)


def distance_lp(R,S, p = 2):
    """
    return the Lp distance btw R and S
    """
    R1 = R
    S1 = S
    if isinstance(R[0],list):
       R1= R[0]
    if isinstance(S[0],list):
       S1= S[0]
    result = 0
    
    for ri, si in zip(R1, S1):
        result += abs(ri -si)**p
    
    return result ** (1/p)


def rect_center(S):
    """
    compute the center of a rectangle
    """
    center = []
    for i in dimension:
        center.append(abs(S[0][i] - S[1][i])/2)
    return center

def minimum_rect(set_point):
    """
    find the minimum rectangle for a set of point
    return bouding box
    """
    R_min, S_max = [], []
    for i in range(dimension):
        L = [point[i] for point in set_point]
        R_min.append(min(L))
        S_max.append(max(L))
    return((R_min,S_max))


def distance(R, S):
    """
    compute the square distance  between two rectangles R and S
    """
    if R == None:
        return 0
    if S == None: 
        return 0
    if len(S)==1:
        S = S[0]
    if len(R)==1:
        R = R[0]
    condition_s = not(isinstance(S[0], list))
    condition_r = not(isinstance(R[0], list))
    if condition_r and condition_s:#distance btw 2 points
        result = 0
        for i in range(dimension):
            result += (R[i] - S[i])**2
        return result
    elif condition_s:
        copie = R
        R = S
        S = copie
    if not(isinstance(R[0], list)):#transformation of a point in a rect
        R1 = [R, R]
        return distance(R1, S)

    p_min = []
    p_max = []
    
    for i in range(dimension):#definition of volumetric distance
        p_min.append(min([R[0][i], R[1][i], S[0][i], S[1][i]]))
        p_max.append(max([R[0][i], R[1][i], S[0][i], S[1][i]]))
    
    return distance(p_min, p_max)




def cost_rectangle(set_rectangle):
    """
    computes the cost of a set of rectangle
    """
    cout = 0
    
    for rect in set_rectangle:
        R = rect[0]
        S = rect[1]
        cout += distance(R, S)
    
    return cout

def creation_hash_table(set_point, epsilon):
    """
    return the hash table complete
    The algo computes for each point a  key (=lower) and places this point in the corresponding position in the hash table
    it means that the algorithme creates an epsilon-size grid and places every point in its corresponding square
    """
    hash_table = {}#initialisation
    
    for point in set_point:#each point
        lower = tuple(int(point[i]/epsilon) for i in range(dimension))#compute key
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


def epsilon_variation_algo(set_point, lenght_set_point):
    """
    the algoritme decreases epsion in order to find the perfect size for the hash table
    the perfect size condition is also the stopping_condition
    """
    #initialisation
    hash_table = {}
    epsilon = 0.1
    hash_table = creation_hash_table(set_point, epsilon)
  #  #while the stopping condition is False
  #  while not stop_condition(hash_table, lenght_set_point):
  #      #decrease epsilon and create the HT
  #      epsilon /= 2
  #      hash_table = creation_hash_table(set_point, epsilon)
    
    return hash_table

        
def naive_nearest_neighboor(set_rectangle, distance_used = distance):
    """
    This algorithme find the nearest neigboor by testing every combination
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

def init_array_distance(set_rectangle, distance_used = distance):
    '''
    create the array whitch define the distance btw two, rectangle
    '''
    n = len(set_rectangle)
    array_distance = [[0]*n]*n
    #print(array_distance)
    
    for i in range(n):
        for j in range(i+1, n):
            dist = distance_used(set_rectangle[i], set_rectangle[j])
            array_distance[i][j] = dist        
            array_distance[j][i] = dist          
    return array_distance

def min_ij_arrray(array, set_rectangle, n):
    """
    find the coordonnate minimum in a array
    """
    array1 = array.copy()
    min_dist = array[0][1]
    nearest_neighboor = (set_rectangle[0], set_rectangle[1], 0, 1)   
    
    for i in range(n):
        for j in range(i+1, n):
            print("i = ",i, " j = ", j," n = ", n)
            dist = array1[i][j]
            print("dist " , dist, " min_dist ", min_dist) 
            if dist < min_dist:
                nearest_neighboor = (set_rectangle[i], set_rectangle[j], i, j)
                min_dist = dist
                print("new min_dist ", min_dist)
    print("######################################################")
    return nearest_neighboor[2], nearest_neighboor[3]

def merge_array(R, i, S, j,  array_distance, set_rectangle, distance_used):
    """
    merge two rectangles (column i and j)
    """
 #   print(R in set_rectangle, "MA")
 #   print(S in set_rectangle)
    copy_set_rectangle = set_rectangle.copy()
    array1 = array_distance.copy()
    #initialisation
    R1 = R
    S1 = S
    if len(set_rectangle) == 1:
        return
    #transform a point in a rectangle
    if not(isinstance(R[0], list)):
        R1 = [R, R]
    if not(isinstance(S[0], list)):
        S1 = [S, S]

    p_min = []
    p_max = []
    #merge the two rectangle
    for i in range(dimension):
        p_min.append(min([R1[0][i], R1[1][i], S1[0][i], S1[1][i]]))
        p_max.append(max([R1[0][i], R1[1][i], S1[0][i], S1[1][i]]))
    
    RUS = [p_min, p_max]
   # print(S in copy_set_rectangle, 's in set_rectangle')   
    copie_2_set = [rect for rect in copy_set_rectangle if rect != S and rect != R] 
   # print(S in copie_2_set, R in copie_2_set,  's et r in set_rectangle')

    
    
    cR = array1[i]
    cS = array1[j]
    #copie_array = [array1[k] for k in range(len(array1)) if (k != i and k != j)]
    copie_array = [[array1[k][l] for l in range(len(array1[k])) if l != i and l !=j] for k in range(len(array1)) if (k != i and k != j)] 
    print(len(copie_array))
    
    dist_RUS = []
    
    for indice, column in enumerate(copie_array):
       # print("indice ", indice," len(copie_2_set) ", len(copie_2_set)," len(copie_array) ",len(copie_array))
        dist = distance_used(copie_2_set[indice], RUS)
        column.append(dist)
        dist_RUS.append(dist)
        
    dist_RUS.append(0) 
    
   # ddfor r in copie_array:
   #     print(len(r), len(copie_2_set))
    
    copie_array.append(dist_RUS)
    copie_2_set.append(RUS)   
    
    return copie_array, copie_2_set


def less_naive_methode(set_rectangle, array_distance):
    """
    find the nearest neigboor by using an and array to store every distance
    """
    n = len(set_rectangle)
    if len(set_rectangle) == 1:
        return None
    
    nn1, nn2 = min_ij_arrray(array_distance, set_rectangle, n)
    return set_rectangle[nn1], nn1,  set_rectangle[nn2], nn2 

def merge_bonus(points):
    """
    computes the potential bonus for merging two points
    """
    if points == None:
        return 0

    R = points[0]
    S = points[1]
    
    if not(isinstance(R[0], list)):
        R = [R, R]
    if not(isinstance(S[0], list)):
        S = [S, S]
    
    dR = distance([R[0]], [R[1]])
    dS = distance([S[0]], [S[1]])
    dR_S = distance(R, S)
    
    return dR_S - (dS + dR)

def merge_rectangle(nearest_neighboor, set_rectangle):
    """
    merge the 2 rectancle in nearest_neigboor
    """
    #initialisation
    R = nearest_neighboor[0]
    S = nearest_neighboor[1]
    R1 = nearest_neighboor[0]
    S1 = nearest_neighboor[1]
   
    #transform a point in a rectangle
    if not(isinstance(R[0], list)):
        R1 = [R, R]
    if not(isinstance(S[0], list)):
        S1 = [S, S]

    p_min = []
    p_max = []
    #merge the two rectangle
    for i in range(dimension):
        p_min.append(min([R1[0][i], R1[1][i], S1[0][i], S1[1][i]]))
        p_max.append(max([R1[0][i], R1[1][i], S1[0][i], S1[1][i]]))
    
    
    #update the set of rectangles
    set_rectangle.remove(S)
    set_rectangle.remove(R)
    set_rectangle.append([p_min, p_max])
    
    return(set_rectangle)

def sbs_m_algo_v2(set_point, eta):
    """
    executes step by step the master_algo using array_distance
    """
    distance_used = volumetric_cost


    #find the perfect hash table
    hash_table = epsilon_variation_algo(set_point, len(set_point))
    
    #define the minimal number of rectangle
    min_nb_rectangle = sqrt(len(set_point))
    
    #convert the hash table in a set of rectangles
    set_rectangle = [minimum_rect(hash_table[key]) for key in hash_table.keys()]
    #apply the NN algorithm while the condition is not False
    i = 0 
    array_distance = init_array_distance(set_rectangle, distance_used)
    while True:
        #find the NN
        i+=1
        afficher_plsr_pts_rect_1(set_rectangle, set_point, i)
        i+=1
        R,nn1, S, nn2 = less_naive_methode(set_rectangle, array_distance)
        nearest_neighboor = (R, S)
        #if the merge of the NN is better than heta or there is enough rectangle
        #if merge_bonus(nearest_neighboor) > heta or len(set_rectangle) > min_nb_rectangle:
        afficher_plsr_pts_rect_3(set_rectangle, set_point, i, nearest_neighboor, [R[0],S[0]])
        if len(set_rectangle) > 2:
            #merge the NN
            array_distance, set_rectangle = merge_array(R, nn1, S, nn2, array_distance, set_rectangle, distance_used)
        #stop the algorithm
        else:
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
        nearest_neighboor = naive_nearest_neighboor(set_rectangle, distance)
        #if the merge of the NN is better than heta or there is enough rectangle
        #if merge_bonus(nearest_neighboor) > heta or len(set_rectangle) > min_nb_rectangle:
        afficher_plsr_pts_rect_3(set_rectangle, set_point, i, nearest_neighboor, [nearest_neighboor[0][0], nearest_neighboor[1][0]])
        if len(set_rectangle) > 2:
            #merge the NN
            set_rectangle = merge_rectangle(nearest_neighboor, set_rectangle)
        #stop the algorithm
        else:
            return set_rectangle



def master_algorithme(set_point, heta):
    """
    combination of the two precedent algorithme
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
        #if the merge of the NN is better than heta or there is enough rectangle
        #if merge_bonus(nearest_neighboor) > heta or len(set_rectangle) > min_nb_rectangle:
        i+=1
        if len(set_rectangle) > 2:
            #merge the NN
            set_rectangle = merge_rectangle(nearest_neighboor, set_rectangle)
        #stop the algorithm
        else:
            return set_rectangle

def evolution_cost(set_point, eta):
    """
    return the evoluution of the cost depending on the number of rectangle
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
        #if the merge of the NN is better than heta or there is enough rectangle
        #if merge_bonus(nearest_neighboor) > heta or len(set_rectangle) > min_nb_rectangle:
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












