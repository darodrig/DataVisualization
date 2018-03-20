from bokeh.plotting import figure, show
from bokeh.models import Title, Range1d, BoxAnnotation
import numpy as np
from bokeh.core.properties import value

# output_file("WTDaily1.html")

# Data Set (Variable inputs)
class_duration = 80  # how long class was (in minutes)
x = [8, 80]  # when questions were asked
y = [5,10]  # wait times
date = "12/07/2018"

# Figure
def main(data):
    p = figure(plot_width=600, plot_height=600, title="Wait Time After Question")

    # background fill color : Box Annotations
    p.toolbar_location = None
    # The background color stuff
    p.add_layout(BoxAnnotation(bottom=3, top=12, fill_alpha=0.1, fill_color='#3FE258'))  # GoodWT
    p.add_layout(BoxAnnotation(top=3, fill_alpha=0.1, fill_color='#E2793F'))  # BadWT

    p.line([0, class_duration+2], [3, 3], line_color='#3FE258', line_width=2, line_dash=[4, 4])  # ideal line

    p.circle(x, y, size=15, color="black", alpha=1, legend=value("Content Question"))
    p.grid.grid_line_color = None
    p.background_fill_color = "white"
    p.y_range = Range1d(0, 12)
    p.x_range = Range1d(0, class_duration+2)
    p.xaxis.axis_label = "Class Duration (minutes)"
    p.yaxis.axis_label = "Wait Time (seconds)"

    # style
    p.title.text_font_size = '18pt'
    p.title.align = 'center'
    p.xaxis.axis_label_text_font_size = '14pt'
    p.yaxis.axis_label_text_font_size = '14pt'
    p.yaxis.axis_label_text_font_style = "normal"
    p.xaxis.axis_label_text_font_style = "normal"
    p.xaxis.major_label_text_font_size = '10pt'
    p.yaxis.major_label_text_font_size = '10pt'
    p.xaxis.minor_tick_line_color = None
    p.legend.location = "top_right"

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
