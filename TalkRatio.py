'''import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

def to_percent(y, position):
    # Ignore the passed in position. This has the effect of scaling the default
    # tick locations.
    s = str(100 * y)

    # The percent symbol needs escaping in latex
    if matplotlib.rcParams['text.usetex'] is True:
        return s + r'$\%$'
    else:
        return s + '%'

N = 5
menMeans = (20, 35, 30, 35, 27)
womenMeans = (25, 32, 34, 20, 25)
menStd = (2, 3, 4, 1, 2)
womenStd = (3, 5, 2, 3, 3)
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, menMeans, width)
p2 = plt.bar(ind, womenMeans, width,
             bottom=menMeans)

plt.title('Talk Ratio')
plt.xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))
plt.yticks(np.arange(0, 101, 10))
plt.legend((p1[0], p2[0]), ('Student', 'TA'))
formatter = FuncFormatter(to_percent)

# Set the formatter
plt.gca().yaxis.set_major_formatter(formatter)
plt.show()
'''
import matplotlib
import numpy as np
from numpy.random import randn
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

test = [.1]
test1 = [.9]
ST = [.1, .3, .12, .5]
TA = [.9, .7, .88, .5]
def to_percent(y, position):
    # Ignore the passed in position. This has the effect of scaling the default
    # tick locations.
    s = str(100 * y)

    # The percent symbol needs escaping in latex
    if matplotlib.rcParams['text.usetex'] is True:
        return s + r'$\%$'
    else:
        return s + '%'

def plot_talk_ratio(ta, st):
    N = len(ta)
    ind = np.arange(N)    # the x locations for the groups
    width = 0.5

    p1 = plt.bar(ind, st, width, color = '#3FA5E2')
    p2 = plt.bar(ind, ta, width, color = '#3FE258',
             bottom=st)
    formatter = FuncFormatter(to_percent)
    plt.title('Talk Ratio', fontsize=18)
    plt.legend((p1[0], p2[0]), ('Student', 'TA'))

    figure = plt.gca()
    figure.yaxis.set_major_formatter(formatter)
    figure.set_xlabel('Date')
    figure.get_yticklabels()[1].set_color('green')
    plt.plot([-1, 4], [.2, .2], 'g--', linewidth=2)
    plt.xticks(ind, ['12/1', '12/3', '12/5', '12/7'])
    plt.show()

plot_talk_ratio(test, test1)
    

