from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource, Title, Range1d, BoxAnnotation

recitation_dates = ["12/1", "12/8", "12/15", "12/22"]
#wait times for box plot
# mins = [1, 1, 2, 1]
# first_quart = [2, 3, 4, 2]
# medians = [5, 4, 6, 3]
# third_quart = [6, 5, 8, 5]
# maxs = [9, 8, 9, 7]

mins = [None]
first_quart = [None]
medians = [None]
third_quart = [None]
maxs = [None]

#output_file("WT_Cumulative.html")

def main(data):
    p = figure(x_range=recitation_dates, y_range=(0,11), title="Wait Time Multiple Days")
    
    p.toolbar_location=None
    p.add_layout(BoxAnnotation(bottom=3, top=11, fill_alpha=0.1, fill_color='#3FE258')) #GoodWT
    p.add_layout(BoxAnnotation(top=3, fill_alpha=0.1, fill_color='#E2793F')) #BadWT
    
    p.xaxis.axis_label = "Class Date"
    p.yaxis.axis_label = "Wait Time (seconds)"
    
    #goal line    
    p.line([0,len(recitation_dates)],[3,3], line_color="#3FE258", line_dash=[4,4], line_width=3)
    
    if len(mins)>=1 and (None not in mins) and (None not in first_quart) and (None not in medians) and (None not in third_quart) and (None not in maxs):
        for i in range(len(recitation_dates)):
            #horizontal boxplot lines
            p.line(x=[i+.375,i+.625], y=[mins[i],mins[i]], line_color="black", line_width=3)
            p.line(x=[i+.25,i+.75], y=[first_quart[i],first_quart[i]], line_color="black", line_width=3)
            p.line(x=[i+.25,i+.75], y=[medians[i],medians[i]], line_color="black", line_width=3)
            p.line(x=[i+.25,i+.75], y=[third_quart[i],third_quart[i]], line_color="black", line_width=3)
            p.line(x=[i+.375,i+.625], y=[maxs[i],maxs[i]], line_color="black", line_width=3)
            
            #vertical boxplot lines
            p.line(x=[i+.25,i+.25], y=[first_quart[i],third_quart[i]], line_color="black", line_width=3)
            p.line(x=[i+.75,i+.75], y=[first_quart[i],third_quart[i]], line_color="black", line_width=3)
            p.line(x=[i+.5,i+.5], y=[first_quart[i],mins[i]], line_color="black", line_width=3)
            p.line(x=[i+.5,i+.5], y=[third_quart[i],maxs[i]], line_color="black", line_width=3)

    #style
    p.title.text_font_size = '28pt'
    p.title.align = 'center'
    p.xaxis.axis_label_text_font_size = '20pt'
    p.yaxis.axis_label_text_font_size = '20pt'
    p.yaxis.axis_label_text_font_style = "normal"
    p.xaxis.axis_label_text_font_style = "normal"
    p.xaxis.major_label_text_font_size = '16pt'
    p.yaxis.major_label_text_font_size = '16pt'

    show(p)
    
data = [recitation_dates, medians]
main(data)