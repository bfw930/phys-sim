
''' visual rendering module '''


''' imports '''

## library functions ##

# functions
from .orch import timestep


# numerical image array handling / manipulation
import numpy as np


## visual display ##

# set qt(5) as rendering framework (display)
#%matplotlib qt

# matplotlib plotting for interactive image display
import matplotlib.pyplot as plt

# display colour / colourmap handling
import matplotlib.colors as colors
#import matplotlib.cm as cmx




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





### Initialise Interactive Display Figure ###

## Inputs ##
# none

## Outputs ##
# fig - matplotlib.pyplot figure reference
# axs - figure axes reference

def init_display(_ticks = False, _labels = False, _ax_lim = False):

    # ensure set interactive plotting on
    plt.ion()

    # initialise display figure and axes
    fig = plt.figure(figsize=(5, 5))
    axs = fig.add_subplot(111)

    plt.tight_layout()

    # set background colour
    axs.set_facecolor('k')
    #ax.set_facecolor((1.0, 0.47, 0.42))

    # set axes range, relative zero
    if _ax_lim:
        axs.set_xlim(-_ax_lim, _ax_lim)
        axs.set_ylim(-_ax_lim, _ax_lim)

    # clean format display, no ticks / labels
    if not _labels:
        axs.set_xticklabels('')
        axs.set_yticklabels('')

    if not _ticks:
        axs.set_xticks([])
        axs.set_yticks([])

    # return figure and axes
    return fig, axs




# run simulation over time period, display node positions
def plot_timestep(data, steps = 100, t_delta = 0.01, Hz = 60):

    # initialise figure
    fig, axs = init_display(_ax_lim = 100)

    # initialise plot
    x = [ data['nodes'][n]['params']['pos'][0] for n in range(data['n_nodes']) ]
    y = [ data['nodes'][n]['params']['pos'][1] for n in range(data['n_nodes']) ]
    #z = [ data['nodes'][n]['params']['pos'][2] for n in range(data['n_nodes']) ]
    m = [ data['nodes'][n]['params']['mass'] for n in range(data['n_nodes']) ]

    #sca = ax.scatter(x, y, s = [i for i in z], c = m)
    sca = axs.scatter(x, y, c = m, s = m, cmap = 'Reds', edgecolor = None)

    plt.pause(0.5)

    # iterate through time
    for ti in range(steps):
        nodes = list(data['nodes'].keys())

        # perform timestep
        timestep(data, nodes, t_delta)

        # only display every nth timestep update
        n = 1
        if ti % n == 0:

            x = []; y = []; z = []; lbls = []
            for n in range(data['n_nodes']):
                pos = data['nodes'][n]['params']['pos']
                x.append(pos[0])
                y.append(pos[1])
                #z.append(pos[2])
            sca.set_offsets(np.c_[x,y])

            #sca.set_sizes([i for i in z])

        plt.pause(Hz**-1)

