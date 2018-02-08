import matplotlib
# SUPER IMPORTANT - leads to all sorts of threading issues because matplotlib calls TK gui toolkit - which instantiates
# a non-displayed window and this causes tons of problems, errors, and crashes (oh my!)
matplotlib.use('Agg')
import numpy as np
#Don't forget the mpld3 library
import matplotlib.pyplot as plt, mpld3
from matplotlib.ticker import FuncFormatter

def to_percent(p, position):
    # Ignore the passed in position. This has the effect of scaling the default
    # tick locations.
    p = 100 * p
    # The percent symbol needs escaping in latex
    if matplotlib.rcParams['text.usetex'] is True:
        return '{:.1f}'.format(p) + r'$\%$'
    else:
        return '{:.1f}'.format(p) + '%'


def plot_talk_ratio(ta, st, dates):
    N = len(ta)
    ind = np.arange(N)  # the x locations for the groups
    width = .5

    p1 = plt.bar(ind, st, width, color='#3FA5E2')
    p2 = plt.bar(ind, ta, width, color='#E2793F',
                 bottom=st)
    formatter = FuncFormatter(to_percent)
    plt.title('Talk Ratio', fontsize=18)
    plt.legend((p1[0], p2[0]), ('Student', 'TA'))

    figure = plt.gca()
    figure.yaxis.set_major_formatter(formatter)
    figure.set_xlabel('Date')
    figure.get_yticklabels()[1].set_color('#3FE258')
    plt.plot([-1, N], [.2, .2], color='#3FE258', linestyle='--', linewidth=2)
    plt.xticks(ind, dates)
    plt.tick_params(axis='x', which='both', bottom='off',
                    top='off', labelbottom='on')


    #this is how I want things sent out
    fig_html = mpld3.fig_to_html(plt.gcf())
    plt.close()
    return(fig_html)





