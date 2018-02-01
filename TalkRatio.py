import matplotlib
import numpy as np
from numpy.random import randn
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


ST = [.1, .3, .12, .5, .1, .3, .12, .5]
TA = [.9, .7, .88, .5, .9, .7, .88, .5]
dates = ['12/1', '12/2', '12/3', '12/4', '12/5', '12/6', '12/7', '12/8']
def to_percent(y, position):
    # Ignore the passed in position. This has the effect of scaling the default
    # tick locations.
    s = str(100 * y)

    # The percent symbol needs escaping in latex
    if matplotlib.rcParams['text.usetex'] is True:
        return s + r'$\%$'
    else:
        return s + '%'

def plot_talk_ratio(ta, st, dates):
    N = len(ta)
    ind = np.arange(N)    # the x locations for the groups
    width = .5

    p1 = plt.bar(ind, st, width, color = '#3FA5E2')
    p2 = plt.bar(ind, ta, width, color = '#E2793F',
             bottom=st)
    formatter = FuncFormatter(to_percent)
    plt.title('Talk Ratio', fontsize=18)
    plt.legend((p1[0], p2[0]), ('Student', 'TA'))

    figure = plt.gca()
    figure.yaxis.set_major_formatter(formatter)
    figure.set_xlabel('Date')
    figure.get_yticklabels()[1].set_color('#3FE258')
    plt.plot([-1, N], [.2, .2], color = '#3FE258', linestyle ='--', linewidth=2)
    plt.xticks(ind, dates)
    plt.tick_params(axis='x', which='both', bottom = 'off',
                    top = 'off', labelbottom = 'on')
    plt.show()

plot_talk_ratio(TA, ST, dates)
    

