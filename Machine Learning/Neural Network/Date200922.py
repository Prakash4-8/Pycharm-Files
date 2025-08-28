import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

df = pd.read_csv("C:/Users/bablu/Downloads/winequality-white.csv", sep=';')

X = df.iloc[:, 0:11]
y = df.iloc[:, 11:12]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=10)

svc_model = SVC(C=.1, kernel='linear', gamma=1)
svc_model.fit(X_train, y_train)

prediction = svc_model.predict(X_test)
print(svc_model.score(X_train, y_train))
print(svc_model.score(X_test, y_test))
