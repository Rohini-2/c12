import pandas as pd
import plotly.express as pe
df=pd.read_csv("university.csv")
fig=pe.scatter(df,x="GRE Score",y="Chance of Admit ",color="GRE Score")
fig.show()