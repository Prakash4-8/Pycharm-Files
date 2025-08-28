import numpy as np
import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder
x = [1, 2, 3, 4]
y = [5, 6, 7, 8]
arr = np.array([x, y], float, ndmin=4)  # parameter values 1st object, 2nd type and in last dimension
print(arr)
print(type(arr))
print(arr.shape)  # provides the dimension of the array  left to right == higher to lower dimension
df = pd.read_csv("D:\DOCUMENTS (EDU)\CURAJ\SEM2\ML\Happiest_Index.csv")
print('Original Dataset : \n',
      df.head(10).to_string())  # used to print dataFrame in console in organised format with using set of constraint

x = df[['Economy (GDP per Capita)', 'Freedom', 'Trust (Government Corruption)', 'Dystopia Residual', 'Generosity']]
# x = df[['Economy (GDP per Capita)']]
y = df['Happiness Score']

regr = linear_model.LinearRegression()
regr.fit(x.values, y.values)  # use of values in this line is doubt
# fit used to train the model
# print('Features of the model : ', regr.feature_names_in_)
predict = regr.predict([[1.33723, 0.62433, 0.18676, 2.5332, 0.33088]])
# predict = regr.predict([[1.459]])
print('The predicted value of the model is : ', predict)
# plt.scatter(x, y, color ='green')
# plt.plot(x,regr.predict(x.values))
# plt.plot(x,y)

# plt.title('Linear Regression')
# plt.xlabel('Freedom')
# plt.ylabel('Happiness Score')
# plt.show()



# data visualization

x1 = df['Economy (GDP per Capita)']
y1 = df['Happiness Score']
plt.boxplot([x1, y1])
plt.xticks([1, 2], ['x1', 'y1'])
plt.xlabel("Economy")
plt.title("My box plot")
plt.ylabel('Happiness')
oh = OneHotEncoder()
x2 = pd.DataFrame(oh.fit_transform(df.iloc[:, [0,1]]))
df = pd.concat([df, x2], axis=1)
print(df.to_string())


# for scatter plot
plt.scatter(x1,y1)

plt.show()