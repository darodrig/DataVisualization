from bokeh.plotting import figure, output_file, show
from bokeh.models.glyphs import Line as Line_glyph
from bokeh.models import ColumnDataSource, Title, Range1d, BoxAnnotation
import numpy as np

output_file("WTDaily.html")

#Data Set
>>>import WTData
>>>import TimeData
x = TimeData
y = WTData

#Figure
def main(data) 
    source = ColumnDataSource(data=data)

    p = figure(plot_width=400, plot_height=400,title="Wait Time Daily", 
                xlabel="Class Duration", ylabel="Wait Time")
    p.inverted_triangle(x, y,size=15, color="navy", alpha=0.5)
    p.grid.grid_line_color = None
    p.background_fill_color = "white"
    p.y_range = Range1d(0, 11)
    p.x_range = Range1d(0,x[-1])

#background fill color : Box Annotations
    Box Annotations
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
    median(WTData)
    M_L_glyph = Line_glyph(x=[0,x[-1]], y=[WT_median,WT_median],
                            line_color='WT_median_color', line_width=2)
    p.add_Mglyph(source, glyph)

#ideal line : LineGlyph
    I_L_glyph = Line_glyph([0,x[-1]],[3,3], line_color='green', line_width=2)
    p.add_Iglyph(source, glyph)

main(data)