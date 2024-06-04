# 导入相关的库
import numpy as np
import pandas as pd

import alphalens as al
# 关闭警告信息
import warnings

if __name__ == '__main__':
    # 关闭警告信息
    warnings.filterwarnings('ignore')
    # 从CSV文件读取数据
    file_path = 'e:temp/factor_data.csv'  # 文件的路径和文件名
    data = pd.read_csv(file_path, encoding='gbk', index_col=0)
    # 统一日期格式
    data['日期'] = pd.to_datetime(data['日期'])

    data['对数流通市值'] = np.log(data['流通市值'])

    # 生成符合要求Alphalens 要求格式的因子值数据
    factor = data.set_index(['日期', '股票代码'])['对数流通市值']
    prices = data.pivot(index='日期', columns='股票代码', values='开盘价')
    # 将第二天的开盘价作为交易价格，避免用到“未来数据”
    prices = prices.shift(-1)
    # 预处理因子数据,得到符合Alphalens
    factor_data = al.utils.get_clean_factor_and_forward_returns(
        factor=factor,
        prices=prices,
        quantiles=10,
        periods=(1, 10)
    )
    # 生成因子性能评价报告
    al.tears.create_full_tear_sheet(factor_data)
