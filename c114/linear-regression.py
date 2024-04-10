import csv 
import pandas as pd 
import plotly.express as px 

df = pd.read_csv('data.csv')

height = df['Height'].tolist()
weight = df['Weight'].tolist()

m = 1 
c = 0 
y = []
for x in height:
    y_value = m*x + c
    y.append(y_value)

fig = px.scatter(x=height, y=weight, color=height)
fig.update_layout(shapes = [
    dict(type = 'line', y0 = min(y), y1 = max(y), x0 = min(height), x1 = max(height))
])
fig.show()