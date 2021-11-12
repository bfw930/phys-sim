
''' data model module '''


''' imports '''

# functions
#from .funcs import func

import random

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




### Data Structure Definition and State Initialisation Functions ###


## Generate Data Storage Object ##

## Details:
# define data storage object structure and set defaults
# includes current node count [integer], node storage object [dict]

## Inputs:
# none
## Outputs:
# data - data structure object [dict]

def gen_data():

    data = {}

    data['nodes'] = {}
    data['n_nodes'] = 0

    return data


## Generate Data Node Object ##

## Details:
# define data node object structure and set defaults
# includes node index [integer], params object [dict], rels object [dict]
# call gen_params, gen_rels for node param/rel objects

## Inputs:
# nid - node index identifier [integer]

## Outputs:
# node - data structure node object [dict]

def gen_node(nid, use_fear = False):

    node = {}

    node['nid'] = nid

    node['params'] = gen_params()
    node['rels'] = gen_rels(use_fear = use_fear)

    return node


## Generate Data Node Parameters Object ##

## Details:
# define node parameters object structure and set defaults
# includes node mass [float], node position/velocity/acceleration (n-dimensional) [array]

## Inputs:
# none

## Outputs:
# params - data node params object [dict]

def gen_params():

    params = {}

    params['mass'] = random.randint(1, 100)/1.

    dims = 2
    params['pos'] = []

    for d in range(dims):
        params['pos'].append(random.randint(-100, 100)/10.)
    params['vel'] = []

    for d in range(dims):
        params['vel'].append(random.randint(-10, 10)/100.)
    params['acc'] = []

    for d in range(dims):
        params['acc'].append(random.randint(-1, 1)/100.)

    return params


## Generate Data Node-Node Relations Object ##

## Details:
# define node relations object structure and set defaults
# includes node-node distance and (multiple) force objects [dict]

## Inputs:
# none

## Outputs:
# rels - data node rels object [dict]

def gen_rels(use_fear = False):

    rels = {}

    rels['dist'] = {}
    rels['gravity'] = {}

    if use_fear:
        rels['fear'] = {}

    return rels


## Generate and Add Data Node Object to Data Storage Object ##

## Details:
# get node index, update current node count
# call gen_node, add generated data node to data storage object

## Inputs:
# data - data storage object

## Outputs:
# none

def add_node(data, use_fear = False):

    nid = data['n_nodes']
    node = gen_node(nid, use_fear = use_fear)

    data['nodes'].update({nid:node})
    data['n_nodes'] += 1

