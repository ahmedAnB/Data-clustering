from timeit import timeit
from sys import argv
from math import sqrt

from affichage_point import *


def volumetric_cost(R):
    """
    computes the volume of a Rectangle R
    """
    result = 1
    for xi_lower, xi_upper in zip(R[0],R[1]):
        result *= abs(xi_upper - xi_lower)
    return result


def merge_gain_volumme(R, S):
    """
    Computes the volume created by merging this 2 rectangles
    """
    return volumetric_cost(merge(R,S)) - volumetric_cost(R) - volumetric_cost(S)


def distance_lp(ptR,ptS, p = 1):
    """
    return the Lp distance between 2 points
    we assume that ptR, ptS are two points
    """
    result = 0
    
    for ri, si in zip(ptR, ptS):
        result += abs(ri -si)**p
    
    return result ** (1/p)


def distance(R, S):
    """
    compute the distance between two rectangle 
    """
    if R[0]==R[1] and S[0]==S[1]:
    #if R and S are two points we computes the L2 distance between them
        return distance_lp(R[0], S[0], 2)
    else:
    #else we search for the lower point and the upper point of the merged rectangle
        dimension = len(R[0])
        lower, upper = [], []
        for i in range(dimension):
            lower.append(min([R[0][i], R[1][i], S[0][i], S[1][i]]))
            upper.append(max([R[0][i], R[1][i], S[0][i], S[1][i]]))
        return distance_lp(lower, upper, 2)


def cost_rectangle(set_rectangle, distance_used = distance):
    """
    computes the cost of a set of rectangle
    """
    cout = 0
    
    for rect in set_rectangle:
        R = rect[0]
        S = rect[1]
        cout += distance_used(R, S)
    
    return cout



