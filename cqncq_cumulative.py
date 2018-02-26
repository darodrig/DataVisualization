from bokeh.core.properties import value
from bokeh.io import show, output_file
from bokeh.io.export import *
from bokeh.models import ColumnDataSource, Title, Range1d
from bokeh.plotting import figure
from bokeh.transform import dodge
import numpy as np






data = {'dates' : ['12/7', '12/9'],
        'Content Question'   : [16, 2],
        'Non-content Question'   : [4, 7]
        }

def main(data):

	source = ColumnDataSource(data=data)

	p = figure(x_range= data['dates'], plot_height=600, title="Question Count",
	           toolbar_location=None, tools="")

	p.vbar(x=dodge('dates', -0.25, range=p.x_range), top='Content Question', width=0.4, source=source,
	       color="#3FA5E2", legend=value("Content Question"))

	p.vbar(x=dodge('dates',  0.2,  range=p.x_range), top='Non-content Question', width=0.4, source=source,
	       color="#E2793F", legend=value("Non-content Question"))


	p.x_range.range_padding = 0.1
	p.xgrid.grid_line_color = None
	p.legend.location = "top_right"
	p.legend.orientation = "vertical"
	p.y_range = Range1d(0, int(1.5 * max(data["Content Question"][0],
						data["Non-content Question"][0])))

	#Labels
	p.xaxis.axis_label = "Date"
	p.yaxis.axis_label = '# of Questions You Asked'



	#Style
	p.yaxis.major_tick_line_color = None

	p.title.text_font_size = '18pt'
	p.title.align = 'center'
	p.xaxis.axis_label_text_font_size = '10pt'
	p.yaxis.axis_label_text_font_size = '10pt'
	p.yaxis.axis_label_text_font_style = "normal"
	p.xaxis.major_label_text_font_size = '10pt'
	p.yaxis.major_label_text_font_size = '10pt'
	p.xaxis.major_tick_line_color = None

	p.output_backend = "svg"
	get_svgs(p, height=325, width=325)

	show(p)

main(data)