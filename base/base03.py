# 导入需要的库
import numpy as np
import pandas as pd
import akshare as ak
import empyrical as ep
import quantstats as qs
import pymongo
import warnings
warnings.filterwarnings('ignore')

if __name__ == '__main__':
    # 获取可转债代码列表
    conbon_list = ak.bond_zh_cov()['债券代码'].tolist()

# print(conbon_list)

# 连接mongo
# client = pymongo.MongoClient(host='localhost', port=27017)
# dbs=client.list_database_names()
# print(dbs)

# 获取可转债收盘价和转股溢价率
# 用于存放每只可转债的数据
data_list = []
i = 0
for code in conbon_list:
    j = 1
    while True:
        try:
            # 逐个获取可转债数据
            data = ak.bond_zh_cov_value_analysis(symbol=code)
            data['转债代码'] = code
            data_list.append(data)  # 将每只可转债的数据添加到data_list
            break
            # 如遇出错则重试三次
        except:
            j += 1
            if j > 3:
                break
    i += 1
    # 输出处理进度
    print("\r已获取[{}/{}]只可转债的数据".format(i, len(conbon_list)), end="")

    data_df = pd.concat(data_list)  # 合并dataFrame

    print(data_list)

    # 数据处理
    data_df['日期'] = pd.to_datetime(data_df['日期'])

    # 删除收盘价和转股溢价率缺失的数据行：
    data_df = data_df.dropna(subset=['收盘价', '转股溢价率'])

    # 选取指定时间范围数据
    start_date = pd.to_datetime('20171229')  # 数据开始日期
    end_date = pd.to_datetime('20230630')  # 数据结束日期
    data_df = data_df[(data_df['日期'] >= start_date) & (data_df['日期'] <= end_date)]

    # 按照转债代码和日期进行排序
    data_df = data_df.sort_values(by=['转债代码', '日期'])

    # 设置时间重采样聚合时的取值规则

    agg_dict = {
        '收盘价': 'last',
        '转股溢价': 'last',
    }
    data_df = data_df.set_index('日期')
    resample_df = data_df.groupby('转债代码').apply(lambda x: x.resample('1M').agg(agg_dict))
    resample_df = resample_df.reset_index()  # 重置索引
