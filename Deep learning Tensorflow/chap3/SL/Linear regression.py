#calling libs
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as seabornInstance
from sklearn.model_selection import train_test_split
fromsklearn import metrics
%matplotlib inline

#calling dataset
dataset = pd.read_csv('https://replit.com/@Jaejuna/LearningDLTool#Deep%20learning%20Tensorflow/chap3/data/weather.csv')

#visualizing data relationship
dataset.plot(x='MinTemp', y-MaxTemp, style='o')
plt.title("MinTemp vs MaxTemp")
plt.xlabel('MinTemp')
plt.ylabel('MaxTemp')
plt.show()

#separating independent var & dependent var and creating model
X = dataset['MinTemp'].values.reshape(-1,1)
y = dataset['MaxTemp'].values.reshape(-1,1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

regressor = LinearRegression()
regressor.fit(X_train, y_train)

#metrics on model
y_pred = regressor.predict(X_test)
df = pd.DataFrame({'Acutal': y_test.flatten(), "Predicted": y_pred.flatten()})
df

#expressiong of regress with validating dataset
plt.scatter(X_test, y_test, color='gray')
plt.plot(X_test, y_pred, color='red', linewidth=2)
plt.show()

#evaluating model
print('mean square method: ', metrics.mean_squared_error(y_test, y_pred))
print('root of mean square method: ', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))