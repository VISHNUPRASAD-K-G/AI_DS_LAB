import statistics as st
import numpy as np

X=[]
n=int(input("Enter The No OF Elements: "))
print("Enter The Array Elements:")
for i in range(0,n):
    c=int(input())
    X.append(c)
y=np.sort(X)
print("Sorted Array Is:",y)
mean=st.mean(y)
median=st.median(y)
mode=st.mode(y)
sd=st.stdev(y)
per=np.percentile(y,20)
print("Mean= ",mean,"\nMedian= ",median,"\nMode= ",mode,
      "\nStandard Deviation= ",sd,"\nPercentile Of 20= ",per)
