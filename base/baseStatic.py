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

