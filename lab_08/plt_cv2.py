# Modified From https://github.com/kevinwlu/iot/blob/master/lesson8/plt_cv2.py

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import cross_val_predict
from sklearn import linear_model

X = pd.read_csv("rpidata1.csv", usecols=[1])
X = X.assign(t=X.index)
y = pd.read_csv("rpidata1.csv", usecols=[2])
lr = linear_model.LinearRegression()
predicted = cross_val_predict(lr, X, y, cv=10)
plt.plot(y, predicted, "ro")
plt.plot([y.min(), y.max()], [y.min(), y.max()], "b-", lw=2)
plt.xlabel("Temperature C")
plt.ylabel("Predicted")
plt.title("Linear Regression")
plt.savefig("stats_predictions.png")

plt.show()
