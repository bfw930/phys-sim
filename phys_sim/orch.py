
''' orchestration module '''


''' imports '''

# functions
from .model import gen_data, add_node

from .phys import distance, gravity, get_fear



'''


'''


''' update state functions '''

def func(var):

    ''' var

    Args:
        var (np.array): track buffer

    Returns:
        (np.array): var

    '''

    # return
    return var



# update node-node euclidean distance
def update_distance(data, nodes):

    for n in [ (n1, n2) for n1 in nodes for n2 in nodes if n1 < n2 ]:

        dist = distance(data, n[0], n[1])

        data['nodes'][n[0]]['rels']['dist'][n[1]] = dist
        data['nodes'][n[1]]['rels']['dist'][n[0]] = dist



# update node-node force: gravity
def update_gravity(data, nodes):

    for n in [ (n1, n2) for n1 in nodes for n2 in nodes if n1 < n2 ]:

        grav = gravity(data, n[0], n[1])

        data['nodes'][n[0]]['rels']['gravity'][n[1]] = grav
        data['nodes'][n[1]]['rels']['gravity'][n[0]] = [ -g for g in grav ]



def update_fear(data, nodes):
    for n in [ (n1, n2) for n1 in nodes for n2 in nodes if n1 < n2 ]:
        fear = get_fear(data, n[0], n[1])
        data['nodes'][n[0]]['rels']['fear'][n[1]] = fear
        data['nodes'][n[1]]['rels']['fear'][n[0]] = [ -f for f in fear ]



# update node acceleration vector from net force vectors
def update_acc(data, nodes):

    for n in nodes:

        grav = data['nodes'][n]['rels']['gravity']
        net_g = [ sum([i[d] for i in grav.values()]) for d in range(len(list(grav.values())[0])) ]

        if 'fear' in data['nodes'][n]['rels'].keys():

            fear = data['nodes'][n]['rels']['fear']
            net_d = [ sum([i[d] for i in fear.values()]) for d in range(len(list(fear.values())[0])) ]

            net_f = np.array(net_g) + np.array(net_d)

        else:

            net_f = net_g

        mass = data['nodes'][n]['params']['mass']
        net_a = [ f/mass for f in net_f ]

        # set node object net acc vector
        data['nodes'][n]['params']['acc'] = net_a



# update node velocity and position vectors from acceleration vector
def update_vel_pos(data, nodes, t_delta):

    for n in range(data['n_nodes']):

        pos = data['nodes'][n]['params']['pos']
        vel = data['nodes'][n]['params']['vel']
        acc = data['nodes'][n]['params']['acc']

        n_vel = [ vel[d] + acc[d]*t_delta for d in range(len(acc)) ]

        n_pos = [ pos[d] + vel[d]*t_delta + .5*acc[d]*t_delta**2 for d in range(len(acc)) ]

        # set node object pos/vel vector
        data['nodes'][n]['params']['pos'] = n_pos
        data['nodes'][n]['params']['vel'] = n_vel



# iterate simulation by uniform timestep, calculate net force, update positions
def timestep(data, nodes, t_delta, use_fear = False):

    update_distance(data, nodes)
    update_gravity(data, nodes)

    if use_fear:
        update_fear(data, nodes)

    update_acc(data, nodes)
    update_vel_pos(data, nodes, t_delta)



# initialise data storage object, generate N nodes
def init(N = 10, use_fear = False):

    # initialise model data structure
    data = gen_data()

    # add nodes to model
    for _ in range(N):
        add_node(data, use_fear = use_fear)

    # weight
    #for n in range(data['n_nodes']):
    #    data['nodes'][n]['params']['pos'][2] += 100

    return data
