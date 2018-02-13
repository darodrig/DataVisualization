from bokeh.core.properties import value
from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.transform import dodge
import numpy as np

output_file("dodged_bars.html")

#variable inputs
cq = [16] # number of content questions
ncq = [3] # number of non-content questions
loc = 80 # length of class

dates = ['']
years = ['Content Question', 'Non-content Question']

data = {'dates' : dates,
        'Content Question'   : cq,
        'Non-content Question'   : ncq}

source = ColumnDataSource(data=data)

p = figure(x_range=dates, y_range=(0, cq[0]+.1*cq[0]), plot_height=600, title="Question Count",
           toolbar_location=None, tools="")

p.vbar(x=dodge('dates', -0.25, range=p.x_range), top='Content Question', width=0.4, source=source,
       color="#3FA5E2", legend=value("Content Question"))

p.vbar(x=dodge('dates',  0.2,  range=p.x_range), top='Non-content Question', width=0.4, source=source,
       color="#E2793F", legend=value("Non-content Question"))

p.x_range.range_padding = 0.1
p.xgrid.grid_line_color = None
p.legend.location = "top_right"
p.legend.orientation = "vertical"

#Labels
p.yaxis.axis_label = '# of Questions You Asked'

#Goal Line
p.line([0, .5], [loc/5, loc/5], line_width=4, color = '#3FE258', line_dash = 'dashed', legend = 'Goal')

#Style
p.yaxis.major_tick_line_color = None

p.title.text_font_size = '28pt'
p.title.align = 'center'
p.xaxis.axis_label_text_font_size = '20pt'
p.yaxis.axis_label_text_font_size = '20pt'
p.yaxis.axis_label_text_font_style = "normal"
p.xaxis.major_label_text_font_size = '16pt'
p.yaxis.major_label_text_font_size = '16pt'
p.xaxis.major_tick_line_color = None

show(p)