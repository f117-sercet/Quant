# 导入需要使用的库存
import akshare as ak
import pandas as pd
import numpy as np
# 关闭警告信息
import warnings

warnings.filterwarnings('ignore')
if __name__ == '__main__':
    # 获取沪深300指数10年的收盘价
    start_date = '20140101'  # 开始日期
    end_date = '20231229'  # 结束日期

    bars = ak.stock_zh_index_hist_csindex(symbol='000300', start_date=start_date, end_date=end_date)
    price_df = bars[['日期', '收盘']]
    # 将日期设置为datetime格式
    price_df['日期'] = pd.to_datetime(price_df['日期'])

    # 日收益率
    # 指某个投资在但一交易日内的收益率。
    # DataFrame的pct_change()函数的功能是计算数据序列的百分比变化，可以用来计算日收益率。
    # 日收益率
    price_df['日收益率'] = price_df['收盘'].pct_change()
    # print(price_df['日收益率'])

    # 周收益率和月收益率
    # 设置日期索引
    price_df.set_index('日期', inplace=True)

    # 计算周收益率 使用resample 来重新采样
    weekly_return = (1 + price_df['日收益率']).resample('W').prod() - 1

    # 计算月收益率
    monthly_return = (1 + price_df['日收益率']).resample('M').prod() - 1

    # 累计收益率
    # 计算累计收益
    price_df['累计收益'] = (1 + price_df['日收益率']).cumprod() - 1

    # 年华收益
    # 计算公式：年化收益 = (1+总收益率)^(1/投资年数)-1
    year_return = (1 + price_df['累计收益率'][-1]) ** (1 / 10) - 1
    # 如果数据的跨度不是整年，我们可以用以下公式计算投资年数：
    # 投资年数 = 总的投资期数 / 一年的投资期数
    # 确定投资期数可以用自然日天数，也可以用交易日天数。
    # 用自然日天数计算年化收益
    # 计算投资年数
    years = (price_df.index[-1] - price_df.index[0]).days / 365
    # 计算年华收益
    annualized_return_type1 = (1 + price_df['累计收益'][-1]) ** (1 / years) - 1
    # 用交易日天数计算年化收益 ########################################

    # 计算年化收益率，用交易日天数计算投资年数
    # 计算投资年数，一年约有244个交易日
    years = len(price_df) / 244
    # 计算年化收益率
    annualized_return_type2 = (1 + price_df['累计收益率'][-1]) ** (1 / years) - 1

    # 对数收益率 对数收益率的公式是取价格序列的自然对数的差分。 对数收益率具有时间可加性的特点， 即多个连续时间段的对数收益率可以直接相加来得到总的收益率

    # 计算对数收益
    log_prices = np.log(price_df)

    # 计算差分
    price_df['对数收益率'] = log_prices.diff()

