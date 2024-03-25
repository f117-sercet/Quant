import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm

if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6]
    # 求和
    sum_value = np.sum(data)
    product = np.prod(data)  # 求积
    cumulative_sum = np.cumsum(data)  # 计算累积和
    cumulative_product = np.cumprod(data)  # 计算累积
    print(sum_value)
    print(product)
    print(cumulative_sum)
    print(cumulative_product)

    # 线性回归
    # 生成样本数据
    np.random.seed(0)
    X = np.random.rand(100)
    Y = 3 * X + np.random.rand(100)
    # 添加常数列，因为statsmodels的线性回归默认不包含截距项
    X = sm.add_constant(X)
    # 建立并拟合模型
    model = sm.OLS(Y,X)
    results = model.fit()

    # 打印回归结果
    print(results.summary())
