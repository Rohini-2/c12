import numpy as np
import pandas as pd
import plotly.express as pe
df=pd.read_csv("university.csv")
gre=df['GRE Score'].tolist()
chances=df['Chance of Admit '].tolist()
m,c=np.polyfit(gre,chances,1)
print(m)
print(c)
newchances=[]
for x in gre:
  y=m*x+c
  newchances.append(y)
fig=pe.scatter(df,x="GRE Score",y="Chance of Admit ",color="GRE Score")
fig.update_layout(shapes=[dict(type="line",x0=min(gre),x1=max(gre),y0=min(newchances),y1=max(newchances))])
fig.show()
print("if gre score is 1000 then chances of admit is", m*1000+c)
