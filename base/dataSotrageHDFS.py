# 使用HDFS保存数据
import akshare as ak

if __name__ == '__main__':
    #导入数据源
    df = ak.stock_zh_a_hist(symbol="600000", period="daily", start_date="20200101", end_date='20221231',
                            adjust="")  # 通过akshare接口获取数据
    print(df)  # 输出数据查看
