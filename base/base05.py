# 后复权价格 = 当日不复权价格*当日复权因子
# 前复权价格 = 当日不复权价格 × 当日复权因子 / 最新复权因子

# 导入需要的包

import pandas as pd
import tushare as ts

if __name__ == '__main__':
    # 生成凭证码：https://tushare.pro
    token = "06f7fc75f4adac10ab1876df718d29efc90c9fba8d099f1ac1c6c574"
    ts.set_token(token)
    pro = ts.pro_api()
    # 获取平安银行（000001）不复权的行情数据，数据的时间范围从2023年6月12日至2023年6月20日
    price_df = pro.daily(ts_code='000001.SZ', start_date='20230612', end_date='20230620').set_index('trade_date')

    # 获取平安银行的复权因子
    adj_factor_df = pro.adj_factor(ts_code='000001.SZ', trade_date='').set_index('trade_date')

    # 将不复权的收盘价和复权因子放在一个DataFrame数据表中
    df = pd.DataFrame()
    df['收盘价——不复权'] = price_df['close']
    df['复权因子'] = adj_factor_df['adj_factor']

    # 计算复权后的收盘价

    df['收盘价_后复权'] = df['收盘价_不复权'] * df['复权因子']
    df['收盘价_前复权'] = df['收盘价_不复权'] * df['复权因子'] / df['复权因子'].iloc[-1]
    print(df)
