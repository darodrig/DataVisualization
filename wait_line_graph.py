import matplotlib.pyplot as plt
import matplotlib
import matplotlib.patches as patches
from matplotlib.collections import PatchCollection

# Set up data
data = [(0, 'class_start', 0), (10, 'WT1A', 5), (300, 'WT2A', 8), (1200, 'WT1A', 2), (3600, 'class_end', 0)]

wt1a_data = []
for i in range(len(data)):
  if(data[i][1] == 'WT1A'):
    wt1a_data.append(data[i])

time_stamp, event_type, duration = zip(*wt1a_data)
time_start = data[0][0]
time_end = data[-1][0]

goal = 1

plt.scatter(time_stamp, duration, marker='o', color='#3fa5e2')
plt.xlabel('Time Elapsed (secs)')
plt.ylabel('Wait Time (secs)')
plt.xlim((0, time_end))
plt.ylim((0, 12))

x = range(0, time_end)
y = [3] * 50

if goal == 1:
  plt.fill_between(x, 0, 3, alpha=0.3, color='#ffb47f')  
  plt.fill_between(x, 3, 12, alpha=0.3, color='#9fd2f0')  

plt.show()
plt.savefig('daily_wait_line_graph.png')

