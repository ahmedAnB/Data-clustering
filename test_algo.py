from creation_point import * 
from main import *
from affichage_point import * 

def fonction_pricipal():
    n = 1000
    nb_rectangle = 10 
    dimension = 2

    #set_point = creation_point_rectangles_2(n, nb_rectangle, dimension)
    set_point = creation_point_sur_cercle(n, nb_rectangle, dimension)
    
    #evolution_heta_cout(set_point)
    set_rectangle = sbs_m_algo(set_point,0.01)
    #evolution_nb_rectangle_cost(set_point)
    
    #print(len(set_rectangle))
    #afficher_plsr_pts_rect(set_rectangle, set_point)


def evolution_nb_rectangle_cost(set_point):
    
    Y, X = evolution_cost(set_point, 0.05)
    afficher_XY(X, Y)
    
 
def test_merge():
    R = ([0.29, 0.17], [0.38, 0.41])
    S = ([0.51, 0.00], [0.96, 0.47])
    RUS = merge_rectangle((R,S), [R, S])
    #print(RUS)
    afficher_plsr_pts_rect([R, S, RUS[0] ], None)

def evolution_heta_cout(set_point):
    hetas, couts, sets = algo_avec_variation_heta(set_point)
  #  for set_rect in sets[:len(sets)//2]:
  #       afficher_plsr_pts_rect(set_rect, set_point)
  #  
  #  print(hetas, couts)
    afficher_XY(hetas, couts)

if __name__ == "__main__":
    fonction_pricipal()
