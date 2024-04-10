import csv 
import numpy as np 

def get_data_source(data_path):
    sleep = []
    coffee = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            sleep.append(float(row['sleep']))
            coffee.append(float(row['Coffee']))
    
    return{
        "x": sleep,
        "y": coffee,
    }

def find_correlation(data_source):
    correlation = np.corrcoef(data_source['x'], data_source['y'])
    print("correlation between the sleep and the coffee is: ", correlation[0,1])

def setup():
    data_path = "coffee-sleep-rel.csv"
    data_source = get_data_source(data_path)
    find_correlation(data_source)

setup()