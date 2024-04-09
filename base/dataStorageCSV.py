# 数据存储方案 CSV

# 导入 akshare
import akshare as ak
# 导入pandas
import pandas as pd

if __name__ == '__main__':
    # 通过akshare接口获取数据
    df_01 = ak.stock_zh_a_hist(symbol="600000", period="daily", start_date="20200101", end_date='20221231',
                               adjust="")

    # 将数据保存为CSV文件
    file_path = 'D:\\data\\60000.csv'
    # 将数据保存为csv文件
    df_01.to_csv(file_path, encoding='gbk')

    # 从CSV中查看数据
    #从指定文件位置file_path 导入数据表格
    df = pd.read_csv('D:/data/60000.csv', encoding='gbk')
    print(df)
