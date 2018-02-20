from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource, Range1d, Title

SAMPLE = { 
			'x' : [0, 5, 10, 15, 20],
			'y' : [0, 0, 0, 0, 0]
		}


def plot_question_count(data, date):
    source = ColumnDataSource(data=data)
    plot = figure(tools = "")
    plot.title.text = 'Content Question Count'

    plot.xaxis.axis_label = 'Time (minutes)'
    plot.yaxis.axis_label = 'Number of Content Questions'
    plot.xaxis.minor_tick_line_color = None
    plot.yaxis.minor_tick_line_color = None
    output_file("line.html")

    last_question = data['y'][-1]
    last_time = data['x'][-1]
    goal_height = last_time/5

    if last_question > goal_height:
        plot.patch([0, 0, last_time, last_time], [0, last_question, last_question, goal_height],
                   fill_color="#CCFFD1", line_color="#CCFFD1", legend='Goal')
        plot.y_range = Range1d(0, last_question)
    else:
        plot.patch([0, 0, last_time], [0, goal_height, goal_height],
                   fill_color="#CCFFD1", line_color="#CCFFD1", legend='Goal')
        plot.y_range = Range1d(0, goal_height)

    plot.legend.location = "bottom_right"
    plot.line(data['x'], data['y'], line_width=2, line_color = "black")
    plot.circle(data['x'], data['y'], fill_color="black", size=8)
    plot.x_range = Range1d(0, data['x'][-1])


    plot.add_layout(Title(text="Data from %s" % date, align = "left", text_font_size = "12px",
                          text_font_style = "italic", text_alpha = .5), "below")
    plot.title.text_font_size = '18pt'
    plot.title.align = 'center'
    plot.xaxis.axis_label_text_font_size = '10pt'
    plot.yaxis.axis_label_text_font_size = '10pt'
    plot.yaxis.axis_label_text_font_style = "normal"
    plot.xaxis.major_label_text_font_size = '10pt'
    plot.yaxis.major_label_text_font_size = '10pt'
    plot.xaxis.major_tick_line_color = None

    show(plot)


plot_question_count(SAMPLE, "12/07/2018")