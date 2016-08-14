from bokeh.plotting import figure
import pandas as pd
from bokeh.charts import TimeSeries
from bokeh.embed import components

def plot_data(data, desired_columns, stock):
    
    note = ""
    if len(desired_columns)==0:
        desired_columns = ['Close']
        note = "NOTE: No desired features selected!"

    desired_columns.append('Date')
    plot = TimeSeries(data.loc[:,desired_columns],index='Date',legend=True,title=stock)
    script, div = components(plot)  
    return script, div, note