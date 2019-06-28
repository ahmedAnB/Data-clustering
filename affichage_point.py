import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import Rectangle
import matplotlib.animation as animation
from random import randint
import datetime
print("affichage bien importé")
size = 1 

def afficher_points_2D(set_points):
    """
    return the data neccessary to plot one set of point in 2 dimensions
    """
    X, Y = [p[0] for p in set_points], [p[1] for p in set_points]
    return(X, Y)

def afficher_rectangle(R):
    """
    Return Data neccessary to plot  one rectangle
    """
    rectangle = R
    buttom_left = rectangle[0]
    S = rectangle[1]
    #print("rectangle = ", rectangle, "et S = ", S)
    dx = abs(buttom_left[0] - S[0])
    dy = abs(buttom_left[1] - S[1])
    return([buttom_left[0], buttom_left[1], dx, dy])

def afficher_XY(X, Y):
    """
    plot Y in fuction of X
    """
    plt.plot(X,Y)
    plt.show()

def afficher_plsr_pts_rect_2(set_rectangles, set_points, i, red_rectangles):
    """
    Displays reactangles and/or points in 2 dimension
    """
    X, Y, ensembles_rect = None, None, None
    plt.figure()
    currentAxis = plt.gca()

    if set_points is not None:
        X,Y = afficher_points_2D(set_points)
        plt.scatter(X, Y, s=size)
    if set_rectangles is not None:
        ensembles_rect = []
        for rect in set_rectangles:
            if isinstance(rect[0],list):
                R = afficher_rectangle(rect)
#               print(R)
                if rect in red_rectangles:
                    currentAxis.add_patch(Rectangle((R[0], R[1]), R[2], R[3], fill=None, alpha=1, color = 'crimson'))
                else:
                    currentAxis.add_patch(Rectangle((R[0], R[1]), R[2], R[3], fill=None, alpha=1, color = 'black'))
    #plt.show()
    date = datetime.datetime.now()
    num =  str(i)
    plt.savefig("./animation/"+num+'.png')
    print("sauvegarde n° " + num + " réussi")


def afficher_plsr_pts_rect_1(set_rectangles, set_points, i):
    """
    Displays reactangles and/or points in 2 dimension
    """
    X, Y, ensembles_rect = None, None, None
    plt.figure()
    currentAxis = plt.gca()

    if set_points is not None:
        X,Y = afficher_points_2D(set_points)
        plt.scatter(X, Y,s = size)
    if set_rectangles is not None:
        ensembles_rect = []
        for rect in set_rectangles:
            if isinstance(rect[0],list):
                R = afficher_rectangle(rect)
#               print(R)
                currentAxis.add_patch(Rectangle((R[0], R[1]), R[2], R[3], fill=None, alpha=1))
    #plt.show()
    date = datetime.datetime.now()
    num = str(i)
    plt.savefig("./animation/"+num+'.png')
    print("sauvegarde n° " + num + "réussi")


def afficher_plsr_pts_rect(set_rectangles, set_points):
    """
    Displays reactangles and/or points in 2 dimension
    """
    X, Y, ensembles_rect = None, None, None
    plt.figure()
    currentAxis = plt.gca()

    if set_points is not None:
        X,Y = afficher_points_2D(set_points)
        plt.scatter(X, Y,s=size)
    if set_rectangles is not None:
        ensembles_rect = []
        for rect in set_rectangles:
            if isinstance(rect[0],list):
                R = afficher_rectangle(rect)
#               print(R)
                currentAxis.add_patch(Rectangle((R[0], R[1]), R[2], R[3], fill=None, alpha=1))
    #plt.show()
    date = datetime.datetime.now()
    num =  str(date.day)+ '_'+ str(date.day) + '_' + str(date.hour) + '_' +str(date.minute) + '_' +str(date.second)+ '_' + str(randint(1, 1000))
    plt.savefig("./animation/"+num+'.png')
    print("sauvegarde n° " + num + "réussi")


def afficher_rectangles(set_rectangles):
    """
    Displays rectangles 
    """
    plt.figure()
    
    currentAxis = plt.gca()
    #print(len(set_rectangles))    
    for rectangle in set_rectangles:
        buttom_left = rectangle[0]
        S = rectangle[1]
        dx = abs(buttom_left[0] - S[0])
        dy = abs(buttom_left[1] - S[1])
        currentAxis.add_patch(Rectangle((buttom_left[0], buttom_left[1]), dx, dy, fill=None, alpha=1))
    
    plt.show()      
  
