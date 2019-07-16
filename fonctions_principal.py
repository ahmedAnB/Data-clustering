from affichage_point import *
from sortedcontainers import SortedList
from main import premiers_rectangles, distance, merge_rectangle
#declaration des constantes

def key(L):
    """
    return the first element of a list
    use for ordering keys in the sorted list
    """
    return L[0]


def conv_tuple(rect):
    """
    convert a rectangle into a tuple
    """
    return (tuple(rect[0]), tuple(rect[1]))


def conv_list(rect_tuple):
    """
    convert in a list a tuple_rect
    """
    return[[list(pt) for pt in pts] for pts in rect_tuple]


def init_sl(set_rectangle, distance_used):
    """
    Initialisation of the sorted list
    quadratic complexity
    """
    #creation of the SL
    s = SortedList()
    h = []
    #computes for every couple of rectangle the distance between them and add it to a list
    for i, rect_i in enumerate(set_rectangle):
        rect_i1 = conv_tuple(rect_i)
        
        for rect_j in set_rectangle[i+1:]:
            #computes the distance between Ri, Rj
            rect_j1 = conv_tuple(rect_j)
            di_j = distance_used(rect_j, rect_i)
            #add the element to the list
            h.append((di_j,{rect_i1, rect_j1}))
    
    #sorts the list using the first element of each cell
    s = SortedList(h,key)
    return s


def search_and_destroy(rect_1,rect_2, sl, set_rectangle, distance_used):
    """
    looks every apparition of rect_1, rect_2, in sl and deletes it
    """
    sl1 = sl.copy()
    dr1 = []
    dr2 = []
    #convert rectangles in Tuples    
    rect_11 = conv_tuple(rect_1)
    rect_21 = conv_tuple(rect_2)
    #search of every apparition of rect1 and rect2
    for rect_i in set_rectangle:
        rect_i1 = conv_tuple(rect_i)
        
        if rect_i != rect_1 and rect_i!= rect_2:
            #computes the key used to represente the distance between R1, Ri and R2, Ri
            clef_1 =(distance_used(rect_1, rect_i), {rect_i1, rect_11})
            clef_2 = (distance_used(rect_2, rect_i), {rect_i1, rect_21})
            #delete the element
            if clef_1 == clef_2:
                sl1.remove(clef_1)
            else:
                sl1.remove(clef_2)
                sl1.remove(clef_1)
    #remove the distance between R1 and R2
    sl1.remove((distance_used(rect_2,rect_1), {rect_11, rect_21}))
    
    return sl1


def ajout_merge_rectangle(merged_rectangle, sl1, set_rectangle_1, distance_used):
    '''
    add to the sl1 every distance between merged_rectangle and the others ones
    '''
    #copy the sl and convert tuple merged_rectangle
    sl2 = sl1.copy()
    merged_rectangle1 = conv_tuple(merged_rectangle)
    
    for rect_i in set_rectangle_1:
        if rect_i != merged_rectangle:
            rect_i1 = conv_tuple(rect_i)
            #computes the cell of the distance between Ri and merged_rectangle
            di = distance_used(rect_i, merged_rectangle)
            clef = [(di, {rect_i1, merged_rectangle1})]
            #add the cell to the SL
            sl2 += clef
    
    return sl2


def sl_merge_rectangle(sl, set_rectangle, nn, distance_used):
    """
    merge the two rectangle in nn and updates set_rectangle
    """
    #convert nn in a list
    nn1 = conv_list(nn)
    #merge rectangles in nn and update the SL
    merged_rectangle = merge_rectangle(nn1, set_rectangle, True)
    set_rectangle_1 = merge_rectangle(nn1, set_rectangle)
    #update the SL
    sl1 = search_and_destroy(nn1[0],nn1[1], sl, set_rectangle, distance_used)
    sl2 = ajout_merge_rectangle(merged_rectangle, sl1, set_rectangle_1, distance_used)
    
    return sl2, set_rectangle_1


def mv1_algo_opti(set_point, nb_rect_max, distance_used):
    """
    mv1 algo with sorted list
    """
    #initialization
    set_rectangle = premiers_rectangles(set_point)
    sl = init_sl(set_rectangle, distance_used)
    
    while len(set_rectangle) > nb_rect_max:
        #find the nearest neighboor
        nn = sl[0][1]
        #merge the nearest neighboor and update the SL
        sl, set_rectangle = sl_merge_rectangle(sl, set_rectangle, nn, distance_used)
    
    return set_rectangle


def ss_mv1_opti(set_point, nb_rect_max, distance_used):
    """
    mv1 algo with sorted list but step by step visualisation possible
    """
    set_rectangle = premiers_rectangles(set_point)
    sl = init_sl(set_rectangle, distance_used)
    i = 0
    while len(set_rectangle) > nb_rect_max:
        i += 1
        afficher_plsr_pts_rect_1(set_rectangle, set_point, i)
        i+=1
        nn = sl[0][1]
        afficher_plsr_pts_rect_2(set_rectangle, set_point, i, conv_list(nn))
        sl, set_rectangle = sl_merge_rectangle(sl, set_rectangle, nn, distance_used)
    return set_rectangle



