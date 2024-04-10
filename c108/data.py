import csv
import pandas as pd 
import plotly.figure_factory as ff

df = pd.read_csv("data.csv")
fig = ff.create_distplot([df["Height"].tolist()], ["height"], show_hist = False)
fig.show()