import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy import stats

CSV=pd.read_csv('data1.csv')
print(CSV)
X=CSV.loc[:, 'Height']
y=CSV.loc[:, 'Weight']

slope, intercept, r, p, std_err = stats.linregress(X, y)

def value_y(X):
    return (slope * X) + intercept

model=list(map(value_y,X))

plt.title("Height X Weight")
plt.scatter(X,y)
plt.plot(X,model)
plt.xlabel("HEIGHT IN cm")
plt.ylabel("WEIGHT IN kg")
plt.show()
num=float(input("Enter The Height To Predict Weight:  "))
print("The Predicted Value=  ",value_y(num))
