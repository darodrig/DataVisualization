from bokeh.plotting import figure, output_file, show
from bokeh.models.glyphs import Line as Line_glyph
from bokeh.models import ColumnDataSource, Title, Range1d, BoxAnnotation
import numpy as np

output_file("WTDaily1.html")

#Data Set (Variable inputs)
class_duration = 80 #how long class was (in minutes)
x = [8,14,23,36,42,57,69,70] #when questions were asked
y = [5,2,6,3,4,1,2,7] #wait times

#Figure
def main(data):
    p = figure(plot_width=600, plot_height=600,title="Wait Time After Question")
    #background fill color : Box Annotations
    
    p.add_layout(BoxAnnotation(bottom=3, top=11, fill_alpha=0.1, fill_color='#3FE258')) #GoodWT
    p.add_layout(BoxAnnotation(top=3, fill_alpha=0.1, fill_color='#E2793F')) #BadWT
    
    p.line([0,class_duration],[3,3], line_color='#3FE258', line_width=2,line_dash=[4,4])  #ideal line

    p.circle(x, y,size=15, color="black", alpha=1)
    p.grid.grid_line_color = None
    p.background_fill_color = "white"
    p.y_range = Range1d(0, 11)
    p.x_range = Range1d(0, class_duration)
    p.xaxis.axis_label = "Class Duration (minutes)"
    p.yaxis.axis_label = "Wait Time (seconds)"
    
    #style
    p.title.text_font_size = '28pt'
    p.title.align = 'center'
    p.xaxis.axis_label_text_font_size = '20pt'
    p.yaxis.axis_label_text_font_size = '20pt'
    p.yaxis.axis_label_text_font_style = "normal"
    p.xaxis.axis_label_text_font_style = "normal"
    p.xaxis.major_label_text_font_size = '16pt'
    p.yaxis.major_label_text_font_size = '16pt'
    p.xaxis.minor_tick_line_color = None

    #calculate median : numpy
    WT_median = np.median(x)
    if WT_median >= 3:
        WT_median_color = "#3FE258"
    else: 
        WT_median_color = "#E2793F"

    p.line(x=[0, class_duration], y=[WT_median,WT_median],
                            line_color=WT_median_color, line_width=2) #median line
                            
    show(p)

data = [x,y, class_duration]
main(data)