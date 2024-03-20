
# 引入 pandas和 akshare
import pandas as pd
import akshare as ak
if __name__ == '__main__':
 #获取股票池
 stocks_df = ak.index_stock_cons(symbol="000043")
 print(stocks_df)  # 打印查看
 # 获取股票代码列表，数据结构为list
 ck_list = stocks_df['品种代码'].tolist()
 print(ck_list)