from numpy import array,dot
from sklearn.linear_model import LinearRegression
X = array([[1, 1], [1, 2], [2, 2], [2, 3]])
# y = 1 * x_0 + 2 * x_1 + 3
y = dot(X, array([1, 2])) + 3
reg = LinearRegression().fit(X, y)
reg.score(X, y)

reg.coef_

reg.intercept_
if __name__ == "__main__":
    print(reg.predict(array([[3, 5]])))