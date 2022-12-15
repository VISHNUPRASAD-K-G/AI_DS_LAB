from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score, recall_score, accuracy_score

#loading datas
iris = load_iris()
X = iris.data
y = iris.target
 
#splitting the imported data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=4)
 

gnb = GaussianNB()
gnb.fit(X_train, y_train) 
y_pred = gnb.predict(X_test)
 

print("Gaussian Naive Bayes model accuracy(in %):", metrics.accuracy_score(y_test, y_pred)*100)


cm = confusion_matrix(y_test, y_pred)
print("The confusion matrix is:")
print(cm)


precision = precision_score(y_test, y_pred, average='macro')
recall = recall_score(y_test, y_pred, average='macro')
 
print('Precision: %.3f' %precision)
print('Recall: %.3f' %recall)
