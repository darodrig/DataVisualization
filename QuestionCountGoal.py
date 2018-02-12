from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource, Range1d

SAMPLE = { 
			'x' : [0, 5, 10, 15, 20],
			'y' : [0, 1, 4, 4, 6]
		}
def plot_question_count(data):
	source = ColumnDataSource(data=data)
	plot = figure(tools = "")
	plot.title.text = 'Question Count'
	plot.title.align = 'center'
	plot.title.text_font_size = '24px'

	plot.xaxis.axis_label = 'Time (minutes)'
	plot.yaxis.axis_label = 'Number of Quesions'

	output_file("line.html")

	plot.patch([0, data['x'][-1], 0], [0, data['y'][-1], data['y'][-1]],
				fill_color = "#CCFFD1", line_color = "#CCFFD1", legend = 'Goal')
	plot.line(data['x'], data['y'], line_width=2, line_color = "black")
	plot.circle(data['x'], data['y'], fill_color="black", size=8)
	plot.x_range = Range1d(0, data['x'][-1])
	plot.y_range = Range1d(0, data['y'][-1])

	show(plot)


plot_question_count(SAMPLE)