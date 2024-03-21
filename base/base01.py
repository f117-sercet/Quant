# 引入 pandas和 akshare
import pandas as pd
import akshare as ak

if __name__ == '__main__':
    # 获取股票池
    stocks_df = ak.index_stock_cons(symbol="000043")
    print(stocks_df)  # 打印查看
    # 获取股票代码列表，数据结构为list
    ck_list = stocks_df['品种代码'].tolist()
    print(ck_list)

    data_list = []  # 用于存放每次获取的数据
    for stock_code in ck_list:  # for循环，逐个股票获取行情数据
        df = ak.stock_zh_a_hist(symbol=stock_code, start_date="20191201", end_date='20230630', adjust="qfq")
        df['股票代码'] = stock_code  # 增加一列“股票代码”
        data_list.append(df)  # 将获取的数据存放在data_list中

    # print("dataList", data_list)

    # 合并DataFrame
    data_df = pd.concat(data_list)
    data_df = data_df.sort_values(by=['日期', '股票代码'], ignore_index=True)  # 按照日期和股票代码进行排序
    print(data_df)

    # 计算股票收益率
    data_df['日收益率'] = data_df.groupby('股票代码')['收盘'].pct_change()

    # 计算每日涨跌比
    date_list = set(data_df['日期'])
    date_list = sorted(list(date_list))
    count_df = pd.DataFrame(index=date_list)
    count_df['上涨股票数量'] = data_df.loc[data_df['日收益率'] > 0].groupby('日期')['日收益率'].count()
    count_df['下跌股票数量'] = data_df.loc[data_df['日收益率'] < 0].groupby('日期')['日收益率'].count()
    count_df['日涨跌比'] = count_df['上涨股票数量'] / count_df['下跌股票数量']

    print("count_df",count_df)