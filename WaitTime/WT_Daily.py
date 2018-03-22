from bokeh.plotting import figure, show
from bokeh.models import Title, Range1d, BoxAnnotation
import numpy as np
from bokeh.core.properties import value

# output_file("WTDaily1.html")

# Data Set (Variable inputs)
class_duration = 80  # how long class was (in minutes)
x = [8, 80]  # when questions were asked
y = [5,7]  # wait times
date = "12/07/2018"

# Figure
def main(data):
    y_axis_range = Range1d(0,10)
    if max(filter(None, y)) >= 10: 
        y_axis_range = Range1d(0,12)
    p = figure(plot_width=325, plot_height=325)
    p.add_layout(Title(text="Wait Time After Question", align="center", text_font_size="14pt",
                          text_font_style="bold", text_alpha=1), "above")
                          
    # background fill color : Box Annotations
    p.toolbar_location = None
    # The background color stuff
    p.add_layout(BoxAnnotation(bottom=3, top=12, fill_alpha=0.1, fill_color='#3FE258'))  # GoodWT
    p.add_layout(BoxAnnotation(top=3, fill_alpha=0.1, fill_color='#E2793F'))  # BadWT

    p.line([0, class_duration+2], [3, 3], line_color='#3FE258', line_width=2, line_dash=[4, 4])  # ideal line

    p.circle(x, y, size=10, color="black", alpha=1, legend=value("Content Question"))
    p.grid.grid_line_color = None
    p.background_fill_color = "white"
    p.y_range = y_axis_range
    p.x_range = Range1d(0, class_duration+2)
    p.xaxis.axis_label = "Class Duration (minutes)"
    p.yaxis.axis_label = "Wait Time (seconds)"

    # style
    p.title.text_font_size = '18pt'
    p.title.align = 'center'
    p.xaxis.axis_label_text_font_size = '11pt'
    p.yaxis.axis_label_text_font_size = '11pt'
    p.yaxis.axis_label_text_font_style = "normal"
    p.xaxis.axis_label_text_font_style = "normal"
    p.xaxis.major_label_text_font_size = '10pt'
    p.yaxis.major_label_text_font_size = '10pt'
    p.xaxis.minor_tick_line_color = None
    p.legend.location = "top_right"
    p.legend.label_height =10
    p.legend.glyph_width = 8
    p.legend.glyph_height = 5
    p.legend.spacing = 1
    p.legend.padding = 3
    p.legend.margin = 1
    p.legend.label_text_font_size = '6pt'
    p.legend.background_fill_alpha = 0.8
    
    # Date
    p.add_layout(Title(text="Data from %s" % date, align="left", text_font_size="12px",
                          text_font_style="italic", text_alpha=.5), "below")

    if y:
        WT_median = np.median(y)
        if WT_median >= 3:
            WT_median_color = "#3FE258"
        else:
            WT_median_color = "#E2793F"

        p.line([0, class_duration+2], [WT_median, WT_median],
               line_color=WT_median_color, line_width=2, legend=value("Median Wait Time"))  # median line


    show(p)


data = [x, y, class_duration, date]
main(data)
