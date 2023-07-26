from bokeh.plotting import figure, show

plot = figure(width = 600, height = 600, tools = "pan, wheel_zoom, box_zoom, reset")

year =[2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 
       2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
rainfall = [35.85, 36.72, 46.27, 28.45, 45.32, 16.54, 21.34, 47.25, 13.76, 
            30.69, 37.39, 17.58, 39.40, 32.00, 28.20, 44.22, 43.92, 27.33, 41.20, 22.02, 20.70, 34.61, 11.51]
plot.line(year, rainfall, line_width = 2)

show(plot)
