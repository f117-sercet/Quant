# 线性回归
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


# 定义损失函数
def compute_cost(w, b, points):
    total_cost = 0
    M = len(points)
    #逐渐计算误差，然后求平均数
    for i in range(M):
        x = points[i, 0]
        y = points[i, 1]
        total_cost += (y - w * x - b) ** 2

    return total_cost


# 定义拟合函数
def average(data):
    sum = 0
    num = len(data)
    for i in range(num):
        sum += data[i]
    return sum / num


# 定义其他函数

if __name__ == '__main__':
    # 引入 数据源头
    points = np.genfromtxt('data.csv', delimiter=',')
    # 提取points中的两列数据
    x = points[:, 0]
    y = points[:, 1]
    plt.scatter(x, y)
    plt.show()

    lr = LinearRegression()
    x_new =x.reshape(-1,1)
    y_new = y.reshape(-1,1)

    # 从训练好的模型种提取系数和截距
    lr.fit(x_new, y_new)
    w = lr.coef_
    b = lr.intercept_
