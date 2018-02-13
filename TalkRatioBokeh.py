from bokeh.plotting import figure, output_file, show, figure as bf
from bokeh.models import ColumnDataSource, NumeralTickFormatter, TickFormatter
from bokeh.models import Span, DatetimeTickFormatter, Range1d, Legend, LegendItem
from bokeh.sampledata.autompg import autompg as df
from bokeh.resources import CDN
from bokeh.embed import file_html
from bokeh.layouts import gridplot
import pandas as pd
import numpy as np


SAMPLE = { 
			'x' : ['12/1', '12/3', '12/5', '12/7'],
			'ta_talk_perc' : [.343434, .343434, .129032, .281250],
			'st_talk_perc' : [.656566, .656566, .870968, .718750]
		}

def plot_talk_ratio(data):
	source = ColumnDataSource(data=data)

	plot = bf(tools = "xpan", x_range = source.data["x"])

	plot.title.text = 'Talk Ratio'
	plot.title.align = 'center'
	plot.title.text_font_size = '24px'

	plot.xaxis.axis_label = 'Date'
	plot.y_range = Range1d(0, 1)
	plot.yaxis.formatter = NumeralTickFormatter(format="0.0%")

	st = plot.vbar(x='x', bottom=0, top='ta_talk_perc', width=0.5,
				   source=source, color = '#3FA5E2', legend = 'Student')
	ta = plot.vbar(x='x', bottom='ta_talk_perc', top=1, width=0.5,
				   source=source, color = '#E2793F', legend = 'TA')	
	goal = plot.ray(x=0, y=.2, length=0, angle = 0, line_width = 2,
					line_color = "#3FE258", line_dash = "dashed", legend = "Goal")
	gridplot([[plot]], sizing_mode='scale_width')
	file_html(plot, CDN, "talk_ratio")
	show(plot)
plot_talk_ratio(SAMPLE)

