from bokeh.plotting import figure, output_file, show, figure as bf
from bokeh.models import ColumnDataSource, NumeralTickFormatter, TickFormatter
from bokeh.models import Span, DatetimeTickFormatter, Range1d, BoxAnnotation
from bokeh.sampledata.autompg import autompg as df
from bokeh.resources import CDN
from bokeh.embed import file_html
from bokeh.layouts import gridplot
import pandas as pd
import numpy as np


SAMPLE = { 
			'x' : ['12/1', '12/3', '12/5', '12/7'],
			'y' : [20, 2, 2, 2]
		}

def plot_talk_ratio(data):
	source = ColumnDataSource(data=data)

	plot = bf(tools = "", x_range = source.data["x"])

	plot.title.text = 'Minutes Elapsed per Question'

	plot.xaxis.axis_label = 'Date'
	plot.yaxis.axis_label = 'Minutes'
	plot.xaxis.minor_tick_line_color = None
	plot.yaxis.minor_tick_line_color = None
	plot.y_range = Range1d(0, max(int(max(data['y']) * 1.5), 10))
	plot.xgrid.grid_line_color = None

	plot.add_layout(BoxAnnotation(top=5,fill_alpha = .25, fill_color='#3FE258'))
	plot.add_layout(BoxAnnotation(bottom=5, fill_alpha = .25, fill_color='#FFD479'))
	plot.vbar(x='x', bottom = 0, top = 'y',width=0.5, source=source, color = "black")
	goal_line = Span(location=5, dimension='width', line_color='#3FE258', line_width=2, line_dash = "dashed")

	plot.title.text_font_size = '18pt'
	plot.title.align = 'center'
	plot.xaxis.axis_label_text_font_size = '10pt'
	plot.yaxis.axis_label_text_font_size = '10pt'
	plot.yaxis.axis_label_text_font_style = "normal"
	plot.xaxis.major_label_text_font_size = '10pt'
	plot.yaxis.major_label_text_font_size = '10pt'
	plot.xaxis.major_tick_line_color = None

	plot.renderers.extend([goal_line])
	show(plot)

plot_talk_ratio(SAMPLE)

