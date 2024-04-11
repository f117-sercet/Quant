# 使用HDFS保存数据
import akshare as ak

import pandas as pd

if __name__ == '__main__':
    #导入数据源
    df = ak.stock_zh_a_hist(symbol="600000", period="daily", start_date="20200101", end_date='20221231',
                            adjust="")  # 通过akshare接口获取数据
    print(df)  # 输出数据查看

    # 设置文件保存的路劲和文件名称
    file_path = 'd:temp/60000.h5'
    # 将数据表格df 保存到 为HDF5文件
    df.to_hdf(file_path,key='df',mode='w')
    df = pd.read_hdf(file_path)  # 从指定文件位置file_path导入表格数据
    print(df)  # 输出数据查看
