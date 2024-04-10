import csv 
import numpy as np

def get_data_source(data_path):
    size = []
    avg = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            size.append(float(row['Size']))
            avg.append(float(row['Avg']))
    
    return{
        "x": size,
        "y": avg,
    }

def find_correlation(data_source):
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print("correlation between the size and the average is: ", correlation[0,1])

def setup():
    data_path = "tv-rel.csv"
    data_source = get_data_source(data_path)
    find_correlation(data_source)

setup()