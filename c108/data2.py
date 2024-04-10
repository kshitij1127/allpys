import pandas as pd
import csv
import plotly.figure_factory as ff  

df = pd.read_csv("data.csv")
fig = ff.create_distplot([df["Weight"].tolist()], ["weight"], show_hist=False)
fig.show()
