import numpy as np
import csv
import plotly_express as px

def marks_present(path):
    marks=[]
    days_present=[]
    with open(path) as f:
        df=csv.DictReader(f)
        fig=px.scatter(df,x="Marks In Percentage",y="Days Present")
        fig.show()

        for i in df:
            marks.append(float(i["Marks In Percentage"]))
            days_present.append(float(i["Days Present"]))
        return {"x":marks,"y":days_present}

def correlation(source):
    correlation=np.corrcoef(source["x"],source["y"])
    print(correlation[0,1])

def setup():
    path="marks_vs_present.csv"
    marksPresent=marks_present(path)
    correlation(marksPresent)

setup()