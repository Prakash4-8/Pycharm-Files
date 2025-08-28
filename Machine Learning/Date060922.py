import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("D:\DOCUMENTS (EDU)\CURAJ\SEM2\ML\Happiest_Index.csv")

X = dataset.iloc[:, 5:6].values  # Independent Variable : Economy
y = dataset.iloc[:, 3:4].values  # Dependent Variable : Happiness Score

# train and fit
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1, test_size=0.25, shuffle=True)

# fitting the linear regression model
from sklearn.linear_model import LinearRegression

lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)

# Prediction time
prediction = lin_reg.predict(X_test)
# print(prediction)

# compute mean
output = np.mean(prediction)
print('Mean', output)

# Mean squared error
MSE = np.square(np.subtract(y_test, prediction)).mean()
print('Mean Sqaured Error ', MSE)

# Using sklearn

from sklearn.metrics import mean_squared_error

mean_squared_error(y_test, prediction)
import numpy as np


# Gradient Descent Function
def gradient_descent(x, y, theta_1, theta_0):
    iteration = 100
    n = len(x)
    learningrate = 0.9
    for i in range(iteration):
        y_predicted = theta_1 * x + theta_0
        # Calculate cost function
        cost = (1 / n) * sum([val ** 2 for val in (y_predicted - y)])
        # Partial derivative with respect to thetha_1
        md = (1 / n) * sum(x * (y_predicted - y))
        # Partial derivative with respect to thetha_0
        bd = (1 / n) * sum(y_predicted - y)
        theta_1 = theta_1 - learningrate * md
        theta_0 = theta_0 - learningrate * bd
        # Print all values
        print("m {} ,b{} , iteration {}".format(theta_1, theta_0, i))
    return theta_0, theta_1


# x = dataset.iloc[:, 5:6].values  # Independent Variable : Economy
# y = dataset.iloc[:, 3:4].values  # Dependent Variable : Happiness Score
theta_1 = theta_0 = 0
theta_0, theta_1 = gradient_descent(X_train, y_train, theta_1, theta_0)

for i in X_test:
    y = theta_0*i + theta_1
    print('y{}, i{}'.format(y, i))