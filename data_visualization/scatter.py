import pandas as pd
import plotly.express as px

# create a scatter plot
df = pd.read_csv("data.csv")
fig = px.scatter(df, x="Population", y="Per capita", title="Comparision", size="Percentage", color="Country", size_max=60)
fig.show()