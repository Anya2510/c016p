import plotly.express as px
import csv
import numpy as np

def plot(data_path):
    with open(data_path) as f:
        df=csv.DictReader(f)
        fig=px.scatter(df,x='Days Present',y='Marks In Percentage')
        fig.show()

def getData(data_path):
    marks=[]
    present=[]
    with open(data_path) as f:
        reader=csv.DictReader(f)
        for row in reader:
            marks.append(float(row['Marks In Percentage']))
            present.append(float(row['Days Present']))
    return{'x':marks,'y':present}

def findCorrelation(data_source):
    correlation=np.corrcoef(data_source['x'],data_source['y'])
    print(correlation[0,1])

def setup():
    data_path='school.csv'
    data_source=getData(data_path)
    findCorrelation(data_source)
    plot(data_path)
setup()