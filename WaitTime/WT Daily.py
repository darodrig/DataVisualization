from bokeh.plotting import figure, output_file, show
from bokeh.models.glyphs import Line as Line_glyph
from bokeh.models import ColumnDataSource, Title, Range1d, BoxAnnotation
import numpy as np

output_file("WTDaily.html")

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
    p.inverted_triangle(x, y,size=15, color="navy", alpha=0.5)
    p.grid.grid_line_color = None
    p.background_fill_color = "white"
    p.y_range = Range1d(0, 11)
    p.x_range = Range1d(0,x[-1])
    p.xaxis.axis_label = "Class Duration"
    p.yaxis.axis_label = "Wait Time"
    
#background fill color : Box Annotations
    GoodWT = BoxAnnotation(bottom=3, top=10, fill_alpha=0.1, fill_color='green')
    BadWT = BoxAnnotation(top=3, fill_alpha=0.1, fill_color='red')

#line colors need to be figured out

#calculate median : numpy
    WT_median = np.median(WTData)
    if WT_median >= 3:
        WT_median_color = "green"
    else: 
        WT_median_color = "red"

#median line : LineGlyph 
    M_Line = p.line(x=[0,x[-1]], y=[WT_median,WT_median],
                            line_color=WT_median_color, line_width=2)

#ideal line : LineGlyph
    I_Line = p.line([0,x[-1]],[3,3], line_color='green', line_width=2)
    return p

show(p)