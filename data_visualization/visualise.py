import pandas as pd 
import plotly.express as px

df = pd.read_csv("line_chart.csv")
 
# Create a line chart
fig = px.line(df, x="Year", y="Per capita income", title="Per capita income of countries", color="Country")
fig.show()