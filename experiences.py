from tests import *
#executes experiences

#computes the evolution between hash table's cells size and the error rate
#for 5000 points, 50 clusters, 3 dimension and size in arange(0.05, 0.6,0.01)
#evolution_error_side_grid(1000, 10, 5, 0.05, 0.6, 0.01)


#computes the evolution between the error rate and the number of cluster
#for 1000 points in 3d and [[1, 15]] cluster ititiaux
#evolution_error_cluster(5000,3,1,50,1)

#show the phenomenon 'curse of dimonsionnality'
#for 1000pts in dimension [[2, 9]] with 10 clusters
#explosion_dimension(2, 9,1000, 10)


#return the relation between epsilon and the isolation of the poins
#for dimension [[2, 160]], for 1000 pts, 
#dim_rect_mm_graphe(2, 160, 0.1,1.1, 0.1, 1000)


#the evolution between the cost function and the step of the algorithm
#for 1000 points 10 rectangles, 3 dimensions
evolution_nb_rectangle_cost(1000, 10, 4)
