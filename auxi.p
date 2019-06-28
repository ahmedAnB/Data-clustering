
from timeit import timeit
from sys import argv




class Branche:
	
	def __init__(self, valeur, enfants, carre):
		self.cout = valeur
		self.enfant = enfants		
		self.carre = carre

def node_kd:
    
    def __init__(self, point, axis, childrens):
        self.point = point
        self.axis = axis
        self.children = children

def load_instance(filename):
    """
    loads .pts file.
    returns distance limit and points.
    """
    with open(filename, "r") as instance_file:
        lines = iter(instance_file)
        distance = float(next(lines))
        points = [Point([float(f) for f in l.split(",")]) for l in lines]
	
    return distance, points


def print_components_sizes(distance, points):
    """
    affichage des tailles triees de chaque composante
    """
    pass  # TODO: afficher la solution

def cost_function(h, w):
	"""
	definition of the cost function 
	"""
	return(h**2 + w **2)	


def divide_h_v(set_point):
	"""
	the fucution will divide the set of point and create two other separed horizontally or vertivally dependind
	th set of point is sorted on the axis in which we will divide
	"""
	n = len(set_point)
	if X_bool:
		set1 = set_point[:n//2 +2]# includin n//2 + 1
		set2 = set_point[n//2 +1:]
	return(set1, set2)

def minimum_rectangle(set_point):
	"""
	return the minmum rectangle containing each point
	"""
	X = [p[0] for p in set_point]
	Y = [p[1] for p in set_point]
	
	x_min, y_min, x_max, y_max = min(X), min(Y), max(X), max(Y)	
	return([[x_min, y_min], [x_max, y_max]])

def size_rectangle(top_right, bottom_left):
	"""
	return the height and width of ractangle in entry
	"""
	width = top_right[0] - bottom_left[0]
	height = top_right[1] - bottom_left[1]
	return (width, height)

def divide_and_conquer_v1(set_point, X_bool, parent):
	"""
	on appliqque l'algoritme de division pour regner
	"""
	rectangle = minimum_rectangle(set_point)
	width, height = size_rectangle
	cout = cost_function(height, width)
	branche_courant = Branche(cout, [], rectangle)
	parent.enfant.append(branche_courant)
	if len(set_point) == 2:
		return True

	if X_bool:
		set_trie = sorted(set_point, key = lambda k:k[0])
	else:
		set_trie = sorted(set_point, key = lambda k:k[1])
	
	set_1, set_2 = divide_h_v(set_trie)
	
	divide_and_conquer_v1(set_1)
	divide_and_conquer_v1(set_2)

	
def plus_petite_distance(A, p1, p2):
    """
    Donne la plus petite distance en A p2, et A p1
    """
    if p1 is None:
        return p2
    if p2 is None:
        return p1
    
    d1 = distance(A, p1)
    d2 = distance(A,p2)
    
    if d1 > d2:
        return d2
    else : 
        return d1

dimension = 2

def create_kd_tree(set_point, axis):
    """
    create kd tree not depending on the type of point
    """
    if len(set_point)==0:
        return None

    
    pivot = mediane_set(set_point)
    set_2, set_1 = [],[]

    for point in set_point:
        if pivot[axis] > point[axis]:
            set_1.append(point)
        elif pivot[axis] < point[axis]:
            set_2.append(point)
        elif point != pivot:
            set_2.append(point)
    
    axis = (axis + 1 )% dimension
    return node_kd(pivot, axis, [create_kd_tree(set_1, axis), create_kd_tree(set_2, axis)])



def closest_neighboor(racine, A):
    """
    trouve le point le plus proche dans l'arbre
    """
    pivot = racine.point
    axis = racine.axis

    if pivot[axis] > A[axis]:
        next_branche = pivot.enfants[0]
        branch_oppose = pivot.enfant[1]
    else:
        next_branche = pivot.enfants[1]
        branch_oppose = pivot.enfant[0]
    
    best_point = plus_petite_distance(A, closest_neighboor(next_branche, A), pivot)
    
    if voisinage(A, best_dist, axis) > (A[axis] -  pivot[axis])**2
        best_point = plus_petite_distance(A, closest_neighboor(branch_oppose, A), best_point)
    
    return best_point





def main():
    """
    ne pas modifier: on charge une instance et on affiche les tailles
    """
    for instance in argv[1:]:
        distance, points = load_instance(instance)
		print_components_sizes(distance, points)
main()

