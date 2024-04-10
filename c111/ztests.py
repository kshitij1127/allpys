import csv 
import statistics
import pandas as pd 
import plotly.figure_factory as ff 
import plotly.graph_objects as go 
import random 

df = pd.read_csv("studentMarks.csv")
data = df["Math_score"].tolist()

# fig = ff.create_distplot([data], ["math score"], show_hist=False)
# fig.show()

# avg = statistics.mean(data)
# st_dev = statistics.stdev(data)
# print(avg, st_dev)

def randomset_ofmean(counter):
    dataset = []
    for i in range(0, counter):
        randomindex = random.randint(0, len(data) - 1)
        value = data[randomindex]
        dataset.append(value)
    
    mean = statistics.mean(dataset)
    return mean 

meanlist = []
for i in range(1, 1000):
    setofmeans = randomset_ofmean(100)
    meanlist.append(setofmeans)

samplemean = statistics.mean(meanlist)
sampledev = statistics.stdev(meanlist)

print(samplemean)
print(sampledev)

first_start, first_end = samplemean - sampledev, samplemean + sampledev
second_start, second_end = samplemean - (2*sampledev), samplemean + (2*sampledev)
third_start, third_end = samplemean - (3*sampledev), samplemean + (3*sampledev)
print("std1", first_start, first_end)
print("std2", second_start, second_end)
print("std3", third_start, third_end)


fig = ff.create_distplot([meanlist], ["math score"], show_hist=False)
# fig.add_trace(go.Scatter(x = [samplemean, samplemean], y = [0, 0.2], mode='lines', name="mean"))
# fig.add_trace(go.Scatter(x = [first_start, first_start], y = [0, 0.17], mode='lines', name="mean"))
# fig.add_trace(go.Scatter(x = [first_end, first_end], y = [0, 0.17], mode='lines', name="mean"))
# fig.add_trace(go.Scatter(x = [second_start, second_start], y = [0, 0.17], mode='lines', name="mean"))
# fig.add_trace(go.Scatter(x = [second_end, second_end], y = [0, 0.17], mode='lines', name="mean"))
# fig.add_trace(go.Scatter(x = [third_start, third_start], y = [0, 0.17], mode='lines', name="mean"))
# fig.add_trace(go.Scatter(x = [third_end, third_end], y = [0, 0.17], mode='lines', name="mean"))

# fig.show()

# finding the mean of the first new data of improved math score
# given tablets
data1 = pd.read_csv("data1.csv")
d1 = data1["Math_score"].tolist()

mean_1 = statistics.mean(d1)
print("mean for data 1" ,mean_1)
figure = ff.create_distplot([meanlist], ["student marks"], show_hist=False)
figure.add_trace(go.Scatter(x = [samplemean, samplemean], y = [0, 0.17], mode='lines', name="mean"))
figure.add_trace(go.Scatter(x = [first_end, first_end], y = [0, 0.17], mode='lines', name="mean"))
figure.add_trace(go.Scatter(x = [mean_1, mean_1], y=[0, 0.17], mode='lines', name='mean data 1'))
figure.show()

# daily extra classes
data2 = pd.read_csv("data2.csv")
d2 = data2["Math_score"].tolist()

mean_2 = statistics.mean(d2)
print("mean for data 2" ,mean_2)
figure2 = ff.create_distplot([meanlist], ["student marks"], show_hist=False)
figure2.add_trace(go.Scatter(x = [samplemean, samplemean], y = [0, 0.17], mode='lines', name="mean"))
figure2.add_trace(go.Scatter(x = [first_end, first_end], y = [0, 0.17], mode='lines', name="mean"))
figure2.add_trace(go.Scatter(x = [mean_2, mean_2], y=[0, 0.17], mode='lines', name='mean data 2'))
figure2.show()

# worksheets regular 
data3 = pd.read_csv("data3.csv")
d3 = data3["Math_score"].tolist()

mean_3 = statistics.mean(d3)
print("mean for data 3" ,mean_3)
figure3 = ff.create_distplot([meanlist], ["student marks"], show_hist=False)
figure3.add_trace(go.Scatter(x = [samplemean, samplemean], y = [0, 0.17], mode='lines', name="mean"))
figure3.add_trace(go.Scatter(x = [first_end, first_end], y = [0, 0.17], mode='lines', name="mean"))
figure3.add_trace(go.Scatter(x = [mean_3, mean_3], y=[0, 0.17], mode='lines', name='mean data 3'))
figure3.show()