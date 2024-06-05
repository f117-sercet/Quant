# 使用Alphalens 库进行因子评价

# 导入相关的库存
import numpy as np
import pandas as pd
import statsmodels.api as sm
import alphalens as al
import warnings

if __name__ == '__main__':
    # 关闭警告信息
    warnings.filterwarnings('ignore')

    # 从CSV文件读取数据
    file_path = 'e:temp/value_factor.csv'
    data_df = pd.read_csv(file_path, encoding='gbk', index_col=0)
    # 统一日期格式
    data_df['日期'] = pd.to_datetime(data_df['日期'])

    # 设置将要评价的因子
    factor_name = 'pe_ttm'
    factor = data_df.set_index(['日期', '股票代码'])[factor_name]

    # 生成交易数据
    prices = data_df.pivot(index='日期', columns='股票代码', values='开盘价')

    # 将第二天的开盘价作为交易价格
    prices = prices.shift(-1)

    # 生成符合要求的数据
    factor_data = al.utils.get_clean_factor_and_forward_returns(
        factor=factor,
        prices=prices,
        quantiles=10,
        periods=(1,10)

    )

    # 生成因子性能报告
    al.tears.create_full_tear_sheet(factor_data)
