# WORKSHOP,Hitesh Sharma , FATHER CONCAICEO RODRIGUES COLLEGE OF ENGINEERING
import matplotlib.pyplot as plt
import pandas as pd


dataset = pd.read_csv('https://s3.us-west-2.amazonaws.com/public.gamelab.fun/dataset/salary_data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3, random_state=0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

viz_train = plt
viz_train.scatter(X_train, y_train, color='red')
viz_train.plot(X_train, regressor.predict(X_train), color='blue')
viz_train.title('Salary VS Experience')
viz_train.xlabel('Years Experience')
viz_train.ylabel('Salary')
viz_train.show()


viz_test = plt
viz_test.scatter(X_test, y_test, color='red')
viz_test.plot(X_train, regressor.predict(X_train), color='blue')
viz_test.title('Salary VS Experience ')
viz_test.xlabel('Years  Experience')
viz_test.ylabel('Salary')
viz_test.show()
