import csv 
import pandas as pd
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go 

df = pd.read_csv("p.csv")

data = df["math score"].tolist()

# math_df = df.groupby("gender")["math score"].mean()
# print(math_df)

mean = statistics.mean(data)
std = statistics.stdev(data)
print(mean, std)

fst, fend = mean - std, mean + std
sst, send = mean - (2*std), mean + (2*std)
tst, tend = mean - (3*std), mean + (3*std)

data1 = [result for result in data if result > fst and result < fend]
data2 = [result for result in data if result > sst and result < send]
data3 = [result for result in data if result > tst and result < tend]

print("{}% of data lies within first standard deviation".format(len(data1)*100/len(data)))
print("{}% of data lies within second standard deviation".format(len(data2)*100/len(data)))
print("{}% of data lies within third standard deviation".format(len(data3)*100/len(data)))
