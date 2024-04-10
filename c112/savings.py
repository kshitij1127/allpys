import pandas as pd 
import statistics
import random 
import plotly.express as px 
import csv

df = pd.read_csv("savings_data_final.csv")
fig = px.scatter(df, y = "quant_saved", color = "rem_any")
fig.show()

# storing file as object in f 
with open("savings_data_final.csv", newline = "") as f:
    reader = csv.reader(f)
    savings_data = list(reader)

savings_data.pop(0)

total_entries = len(savings_data)
total_people_given_reminder = 0 

for data in savings_data:
    if int(data[3]) == 1:
        total_people_given_reminder += 1


import plotly.graph_objects as go 

fig = go.Figure(go.Bar(x = ["reminded", "not reminded"], y = [total_people_given_reminder, (total_entries - total_people_given_reminder)]))
fig.show()

# finding mean median and mode of all the savings data 
allsavings = []
for data in savings_data:
    allsavings.append(float(data[0]))

print(f"mean of savings - {statistics.mean(allsavings)}")
print(f"median of savings - {statistics.median(allsavings)}")
print(f"mode of savings - {statistics.mode(allsavings)}")

reminded_savings = []
not_reminded_savings = []

for data in savings_data:
    if int(data[3]) == 1:
        reminded_savings.append(float(data[0]))
    else:
        not_reminded_savings.append(float(data[0]))
    
print("result for people who were reminded to save: ")
print(f"reminded savings mean = {statistics.mean(reminded_savings)}")
print(f"reminded savings median = {statistics.median(reminded_savings)}")
print(f"reminded savings mode = {statistics.mode(reminded_savings)}")

print("\n\n")
print("result for people who were not reminded to save: ")
print(f"not reminded savings mean = {statistics.mean(not_reminded_savings)}")
print(f"not reminded savings median = {statistics.median(not_reminded_savings)}")
print(f"not reminded savings mode = {statistics.mode(not_reminded_savings)}")

print(f"standard deviation of all data: {statistics.stdev(allsavings)}")
print(f"standard deviation of reminded data: {statistics.stdev(reminded_savings)}")
print(f"standard deviation of not reminded data: {statistics.stdev(not_reminded_savings)}")

# finding correlation between age and savings 
import numpy as np
age = []
savings = []

for data in savings_data:
    if float(data[5]) != 0:
        age.append(float(data[5]))
        savings.append(float(data[0]))

correlation = np.corrcoef(age, savings)
print(f"correlation between the age and savings is: {correlation[0,1]}")

import plotly.figure_factory as ff

figure = ff.create_distplot([df["quant_saved"].tolist()], ["savings"], show_hist=False)
figure.show()

# inter quartile range method(IQr) to remove outliers 