import csv
import numpy as np

def getData(data_path):
    size_of_tv=[]
    average_time_spent=[]
    with open(data_path) as f:
        reader=csv.DictReader(f)
        for row in reader:
            size_of_tv.append(float(row['Size of TV']))
            average_time_spent.append(float(row['\tAverage time spent watching TV in a week (hours)']))
    return{'x':size_of_tv,'y':average_time_spent}

def findCorrelation(data_source):
    correlation=np.corrcoef(data_source['x'],data_source['y'])
    print(correlation[0,1])

def setup():
    data_path='tv.csv'
    data_source=getData(data_path)
    findCorrelation(data_source)
setup()