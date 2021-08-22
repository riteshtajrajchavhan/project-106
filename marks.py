import csv
import numpy as np
import plotly.express as px



def getDataSource(data_path):
    marks=[]
    days=[]
    with open(data_path, encoding='utf-8') as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            marks.append(float(row["Marks In Percentage"]))
            days.append(float(row["Days Present"]))
    return {"x":marks, "y":days}

def findCorrelation(datasource):
    correlation=np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between marks and days present in school -----",correlation[0,1])

def setup():
    data_path="marks.csv"
    datasource=getDataSource(data_path)
    findCorrelation(datasource)
    


setup()

