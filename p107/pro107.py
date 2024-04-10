import pandas as pd 
import plotly.express as px 

df = pd.read_csv("data.csv")
sc = df.groupby(["student_id", "level"], as_index = False)["attempt"].mean()

fig = px.scatter(sc, x="student_id", y="level", color="attempt", size="attempt")
fig.show()