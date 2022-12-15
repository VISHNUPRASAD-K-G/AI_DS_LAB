import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(1,20,100)
def normal_dist(x,mean,sd):
    prob_density = (np.pi*sd) * np.exp(-0.5*((x-mean)/sd)**2)
    return prob_density
mean=np.mean(x)
sd=np.std(x)
pdf = normal_dist(x,mean,sd)

plt.plot(x,pdf , color = 'red')
plt.xlabel('Data points')
plt.ylabel('Probability Density')
plt.show()
---------------------------------------------------------------
VISHNUPRASAD-K-G/AI_DS_LAB
import seaborn as sns
import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[20,40,45,30,25]

z=sns.stripplot(x,y)
z.set(xlabel="Roll No:",ylabel="MARKS")
plt.figure()

plt.plot(x,y)
plt.show()

plt.bar(x,y)
plt.show()

plt.stem(x,y)
plt.show()
