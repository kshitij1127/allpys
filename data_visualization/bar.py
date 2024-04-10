import pandas as pd
import plotly.express as px

# create a bar graph
df = pd.read_csv("data.csv")
fig = px.bar(df, x="Country", y="InternetUsers", title="Comparision")
fig.show()