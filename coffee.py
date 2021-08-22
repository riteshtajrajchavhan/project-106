import csv
import numpy as np
import plotly.express as px



def getDataSource(data_path):
    coffee=[]
    sleep=[]
    with open(data_path, encoding='utf-8') as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            coffee.append(float(row["Coffee in ml"]))
            sleep.append(float(row["sleep in hours"]))
    return {"x":coffee, "y":sleep}

def findCorrelation(datasource):
    correlation=np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between coffee in ml and sleep in hours -----",correlation[0,1])

def setup():
    data_path="coffee.csv"
    datasource=getDataSource(data_path)
    findCorrelation(datasource)
    


setup()

