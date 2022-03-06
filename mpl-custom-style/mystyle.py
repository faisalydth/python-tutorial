# import module
from matplotlib import rcParams

# make a dictionary of your own configuration
myparams = {
    'figure.figsize' : [10.0, 6.0],
    'lines.linestyle' : '--',
    'lines.linewidth' : 3,
    'xtick.labelsize' : 'large',
    'ytick.labelsize' : 'large'
}

# set your own configuration
def set_params():
    for key, val in myparams.items():
        rcParams[key] = val