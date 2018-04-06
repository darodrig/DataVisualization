from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource, Title, Range1d, BoxAnnotation

#recitation_dates = ("12/1", "12/8", "12/15", "12/22")
#wait times for box plot
#mins = (1,None, 2, 1)
#first_quart =(2, 3, 4, 2)
#medians = (5, None, 6, 3)
#third_quart = (6, 5, 8, 5)
#maxs = (9, None, 10, 7)

data = dict(
mins=[1,None, 2, 1], 
first_quart=[2, 3, 4, 2],
medians=[5, None, 6, 3],
third_quart=[6, 5, 8, 5],
maxs=[9, None, 9, 7],
recitation_dates=["12/1", "12/8", "12/15", "12/22"]
)


def main(data):
    source = ColumnDataSource(data=data)
    y_axis_range = (0,11)
    p = figure(plot_width=325, plot_height=325,x_range=source.data['recitation_dates'], y_range=y_axis_range)
    p.add_layout(Title(text="Wait Time Multiple Days", align="center", text_font_size="14pt",
                          text_font_style="bold", text_alpha=1), "above")
                          
    p.toolbar_location=None
    p.add_layout(BoxAnnotation(bottom=3, top=11, fill_alpha=0.1, fill_color='#3FE258')) #GoodWT
    p.add_layout(BoxAnnotation(top=3, fill_alpha=0.1, fill_color='#E2793F')) #BadWT
    
    p.xaxis.axis_label = "Class Date"
    p.yaxis.axis_label = "Wait Time (seconds)"
    
    #goal line    
    p.line([0,len(source.data['recitation_dates'])],[3,3], line_color="#3FE258", line_dash=[4,4], line_width=3)
    line_w = 1
    
    for i in range(len(source.data['recitation_dates'])):
        if source.data['medians'][i] == None:
            continue
        #horizontal boxplot lines
        p.line(x=[i+.375,i+.625], y=[source.data['mins'][i],source.data['mins'][i]], line_color="black", line_width=line_w)
        p.line(x=[i+.25,i+.75], y=[source.data['first_quart'][i],source.data['first_quart'][i]], line_color="black", line_width=line_w)
        p.line(x=[i+.25,i+.75], y=[source.data['medians'][i],source.data['medians'][i]], line_color="black", line_width=line_w+1, 
                legend=("Median of Day"))
        p.line(x=[i+.25,i+.75], y=[source.data['third_quart'][i],source.data['third_quart'][i]], line_color="black", line_width=line_w)
        p.line(x=[i+.375,i+.625], y=[source.data['maxs'][i],source.data['maxs'][i]], line_color="black", line_width=line_w)
        
        #vertical boxplot lines
        p.line(x=[i+.25,i+.25], y=[source.data['first_quart'][i],source.data['third_quart'][i]], line_color="black", line_width=line_w)
        p.line(x=[i+.75,i+.75], y=[source.data['first_quart'][i],source.data['third_quart'][i]], line_color="black", line_width=line_w)
        p.line(x=[i+.5,i+.5], y=[source.data['first_quart'][i],source.data['mins'][i]], line_color="black", line_width=line_w)
        p.line(x=[i+.5,i+.5], y=[source.data['third_quart'][i],source.data['maxs'][i]], line_color="black", line_width=line_w)

    #style
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
    p.legend.label_text_font_size = '10pt'
    p.legend.background_fill_alpha = 0.8

    show(p)
    
main(data)