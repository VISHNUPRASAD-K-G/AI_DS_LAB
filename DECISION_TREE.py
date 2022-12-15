from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score

data=load_iris()
                
X=data.data
y=data.target

n=int(input("Enter The No: of Trainig Data: ")) 

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=n)

dtc=tree.DecisionTreeClassifier()
model=dtc.fit(X_train,y_train)
pred=dtc.predict(X_test)

plt.figure(figsize=(10,10))
tree.plot_tree(dtc, filled=True)
plt.show()
print(f"Accuracy: {round(accuracy_score(pred, y_test)*100, 2)}%")
