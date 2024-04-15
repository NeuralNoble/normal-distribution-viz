from bokeh.io import curdoc
from bokeh.layouts import column
from bokeh.models import Slider, ColumnDataSource
from bokeh.plotting import figure
import numpy as np
from scipy.stats import norm

x = np.linspace(-5, 5, 1000)
mu = 0
sigma = 1
pdf = norm.pdf(x, mu, sigma)

source = ColumnDataSource(data={'x': x, 'pdf': pdf})

plot = figure(title='Normal Distribution', height=400, width=600,
              background_fill_color='#f0f0f0')
plot.line('x', 'pdf', source=source, line_width=3, line_color='blue')

mean_slider = Slider(title='Mean', value=mu, start=-5, end=5, step=0.1)
stddev_slider = Slider(title='Standard Deviation', value=sigma, start=0.1, end=5, step=0.1)

def update_data(attrname, old, new):
    mu = mean_slider.value
    sigma = stddev_slider.value
    pdf = norm.pdf(x, mu, sigma)
    source.data = {'x': x, 'pdf': pdf}

for slider in [mean_slider, stddev_slider]:
    slider.on_change('value', update_data)

layout = column(plot, mean_slider, stddev_slider)
curdoc().add_root(layout)
