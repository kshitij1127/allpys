import csv
import pandas as pd 
import statistics
import plotly.figure_factory as ff
import random 

df = pd.read_csv("data.csv")
popdata = df["temp"].tolist()
population_mean = statistics.mean(popdata)
std = statistics.stdev(popdata)
fig = ff.create_distplot([popdata], ["average"], show_hist=False)
fig.show()

def randomset_ofmean(counter):
  dataset = []
  for i in range(0, counter):
    randomindex = random.randint(0, len(popdata) - 1)
    value = popdata[randomindex]
    dataset.append(value)
    
  mean = statistics.mean(dataset)
  return mean 

def showfig(mean_list):
  df = mean_list
  mean = statistics.mean(mean_list)
  print(mean)
  fig = ff.create_distplot([df], ["temp"], show_hist=False)
  fig.show()

def standard_deviation():
  meanlist = []
  for i in range(0, 1000):
    setofmeans = randomset_ofmean(100)
    meanlist.append(setofmeans)
  standarddev = statistics.stdev(meanlist)
  print(standarddev)
  # square root of no of items taken


def setup():
  meanlist = []
  for i in range(0, 1000):
    setofmeans = randomset_ofmean(100)
    meanlist.append(setofmeans)
  
  showfig(meanlist)

standard_deviation()
setup()