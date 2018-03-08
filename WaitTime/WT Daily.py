from bokeh.plotting import figure, output_file, show
from bokeh.models.glyphs import Line as Line_glyph
from bokeh.models import ColumnDataSource, Title, Range1d, BoxAnnotation
import numpy as np

output_file("WTDaily1.html")

#Data Set
WTData = [5,0,6,3,4,1,2,7]
TimeData=[0,1,2,3,4,5,6,7]
x = TimeData
y = WTData

data = [x,y]

#Figure
def main(data):
    #source = ColumnDataSource(data=data)

    p = figure(plot_width=400, plot_height=400,title="Wait Time Daily")
    p.circle(x, y,size=15, color="navy", alpha=0.5)
    p.grid.grid_line_color = None
    p.background_fill_color = "white"
    p.y_range = Range1d(0, 10)
    p.x_range = Range1d(0,x[-1])
    p.xaxis.axis_label = "Class Duration"
    p.yaxis.axis_label = "Wait Time (sec)"
    
#background fill color : Box Annotations
    p.add_layout(BoxAnnotation(bottom=3, top=10, fill_alpha=0.1, fill_color='green')) #GoodWT
    p.add_layout(BoxAnnotation(top=3, fill_alpha=0.1, fill_color='red')) #BadWT

#line colors need to be figured out

#calculate median : numpy
    WT_median = np.median(WTData)
    if WT_median >= 3:
        WT_median_color = "green"
    else: 
        WT_median_color = "red"

    p.line(x=[0,x[-1]], y=[WT_median,WT_median],
                            line_color=WT_median_color, line_width=2) #median line
                            
    p.line([0,x[-1]],[3,3], line_color='green', line_width=2,line_dash=[4,4])  #ideal line
    
    show(p)

