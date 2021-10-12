import csv
import plotly_express as px
import pandas as pd
import plotly.figure_factory as ff

df=pd.read_csv("data_1.csv")
counter=[]
fig = ff.create_distplot([df["Avg Rating"].tolist()], ["ratings"])
fig.show()