
''' physics simulation module '''


''' imports '''

# functions
#from .funcs import func


## data processing ##

# numerical image array handling / manipulation
import numpy as np


'''


'''


''' orchestration functions '''

def func(var):

    ''' var

    Args:
        var (np.array): track buffer

    Returns:
        (np.array): var

    '''

    # return
    return var





### Physics and Parameter Calculation Functions ###


## Calculate Node-Node Euclidean Distance ##

## Details:
# calculate inter-node euclidean distance from node position vectors

## Inputs:
# nid1, nid2 - data node indicies

## Outputs:
# dist - node-node distance [float]

def distance(data, nid1, nid2):

    n1 = data['nodes'][nid1]['params']['pos']
    n2 = data['nodes'][nid2]['params']['pos']

    # update to include dimensional weighting

    dist = sum([ (n2[i] - n1[i])**2 for i in range(len(n1)) ])**.5

    return dist


## Calculate Node-Node Force: Gravity ##

## Details:
# calculate inter-node force vector, gravity from node-node distance vector

## Inputs:
# nid1, nid2 - data node indicies

## Outputs:
# force - node-node force vector [float], (n-dimensional) array

def gravity(data, nid1, nid2):

    node1 = data['nodes'][nid1]
    node2 = data['nodes'][nid2]
    n1p = node1['params']['pos']
    n2p = node2['params']['pos']

    # get node-node distance each dimension (vector array)
    di = [ (n2p[i] - n1p[i]) for i in range(len(n1p)) ]
    dist = node1['rels']['dist'][nid2]

    n1m = node1['params']['mass']
    n2m = node2['params']['mass']

    G = 1.
    grav = G *( (n1m * n2m) / dist**2 )
    force = [ grav*d for d in di ]

    return force



def get_fear(data, nid1, nid2):

    node1 = data['nodes'][nid1]
    node2 = data['nodes'][nid2]
    n1p = node1['params']['pos']
    n2p = node2['params']['pos']

    di = [ (n2p[i] - n1p[i]) for i in range(len(n1p)) ]
    #dist = distance(node1, node2)
    dist = node1['rels']['dist'][nid2]

    n1m = node1['params']['mass']
    n2m = node2['params']['mass']
    k = 0.001
    force = -(k*(np.e**dist))
    return [ d*force for d in di ]


