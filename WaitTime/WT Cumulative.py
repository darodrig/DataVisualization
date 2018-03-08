from bokeh.plotting import figure, output_file, show
from bokeh.models.glyphs import Line as Line_glyph
from bokeh.models.glyphs import VBar
from bokeh.models import ColumnDataSource, Title, Range1d, BoxAnnotation
import numpy as np


def main(data):
    
    WT_medians = [4,2,1,0,6]
    Recitations = [0,1,2,3,4] #WT_medians_index
    WT_ideal = 3 
    bar_width = 50
    color = None

    #source = ColumnDataSource(data=data)

    p = figure(plot_width=len(WT_medians)*bar_width, plot_height=400,
                title="Wait Time Cummulative")
    p.xaxis.axis_label = "Recitation"
    p.yaxis.axis_label = "Wait Time (sec)"
    x_range = range(0,len(WT_medians)) #same as Recitation
    y_range = range(0,11)
    
    #ideal line : LineGlyph
    p.line([0,x[-1]],[3,3], line_color='green', line_width=2,line_dash=[4,4])  #ideal line

    for i in x_range:
        #Bar for each recitation : VBar Glyph 
        Bar_glyph = VBar(x=[i*bar_width,(i+1)*bar_width], top=plot_height, 
                            bottom=0, width=0.5, fill_color="")
        p.add_glyph(source, glyph)
        #median line : Line Glyph 
        if j >= WT_ideal: 
            color = "green"
        elif j < WT_ideal: 
            color = "red"
        M_L_glyph = Line_glyph(x=[i*bar_width,(i+1)*bar_width],     
                                y=[WT_medians[i],WT_medians[i]],
                                line_color=color,line_width=3)
        p.add_Mglyph(source, glyph)
    
    show(p)