from asyncore import read
import csv
from statistics import correlation
import plotly.express as px
import pandas as pd 
import numpy as np

def get_data_source(data_path):
    icecream_sales = []
    colddrink_sales = []
    with open(data_path) as csv_file:
    # df = csv.DictReader(csv_file)
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            icecream_sales.append(float(row['Temperature']))
            colddrink_sales.append(float(row['Ice-cream Sales']))

    return {
        "x": icecream_sales,
        "y": colddrink_sales,
    }
        # df = pd.read_csv('ice-cold-rel.csv')
        # df.sort_values(by='Temperature', ascending=True)
        # fig = px.scatter(df, x='Temperature', y='Ice-cream Sales')
        # fig.show()

def find_correlation(data_source):
    correlation = np.corrcoef(data_source['x'], data_source['y'])
    print("correlation between the temperature and the icecream sales is: ", correlation[0,1])

def setup():
    data_path = "ice-cold-rel.csv"
    data_source = get_data_source(data_path)
    find_correlation(data_source)

setup()
