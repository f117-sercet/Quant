# 线性回归
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


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


if __name__ == '__main__':
    # 引入 数据源头
    points = np.genfromtxt('data.csv', delimiter=',')
    # 提取points中的两列数据
    x = points[:, 0]
    y = points[:, 1]
    plt.scatter(x, y)
    plt.show()
