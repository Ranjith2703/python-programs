
import pandas as pd
import matplotlib.pyplot as plt

d=pd.read_csv("matplotlib/WineQT.csv")
#print(d.drop_duplicates())
#print(d.describe())
d.columns()
d.tail()
print(d.columns)
print(d.iloc[100:110])
print(d.dtypes)
print(d.describe())
print(d.info())
#print(d.to_string())


#print(d.info())
#d.fillna(40,inplace=True)#fillna is 
#d.dropna(inplace=True)
d.plot()
d["alcohol"].plot(kind = 'hist')
plt.show()