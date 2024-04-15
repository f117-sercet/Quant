import pandas as pd
import numpy as np

# 错误值处理
if __name__ == '__main__':
    # df_A、df_B、df_B为三个数据表，这三张表的数据本应相同，但现在有错误的数据在里面
    df_A = pd.DataFrame({'value_A': [10, 20, 30]}, index=['2020-02-01', '2020-02-02', '2020-02-03'])
    df_B = pd.DataFrame({'value_B': [10, 20, 31]}, index=['2020-02-01', '2020-02-02', '2020-02-03'])
    df_C = pd.DataFrame({'value_C': [10, 22, 30]}, index=['2020-02-01', '2020-02-02', '2020-02-03'])

    # 将df_A、df_B、df_B合并为1个DataFrame
    df = df_A.join([df_B, df_C], how='outer')
    # 比较value_A、value_B两列,如果值相等，则'correct'的值设为True(数据正确)，否则为False(存在错误数据)
    df['correct'] = (df['value_A'] == df['value_B'])
    # 如果'correct'列的值设为True，则取value_A为结果值，否则取value_C的值为结果值
    df['value'] = df.apply(lambda x: x['value_A'] if x['correct'] else x['value_C'], axis=1)
    print(df)

    # 缺失值处理
    df_01 = pd.DataFrame({
        'A': [1, 2, np.nan, 6],
        'B': [5, np.nan, np.nan, 8],
        'C': [9, 10, 11, 12]
    })

    # 使用列的平均值来填充缺失值，fillna()为填充缺失值的函数
    df_01.fillna(value=df.mean(), inplace=True)

    # 异常值处理
    df_02 = pd.DataFrame({
        'A': [1, 2, 3, 4, 5, 1000]
    })
    # 使用IQR方法来识别异常值
    q1 = df_02['A'].quantile(0.25)  # 第一分位数字
    q3 = df_02['A'].quantile(0.75)  # 第二分位数
    IQR = q3 - q1
    # 正常值范围在(Q1 - 1.5 * IQR)和(Q3 + 1.5 * IQR)之间，不在这个范围内的就是异常值，对异常值作删除处理
    df_02 = df_02[~((df['A'] < (q1 - 1.5 * IQR)) | (df['A'] > (q3 + 1.5 * IQR)))]

# 重复数据处理
# 假设我们有一个包含重复行的数据集
df_03 = pd.DataFrame({
    'A': [1, 2, 2, 4],
    'B': [5, 6, 6, 8],
    'C': [9, 10, 10, 12]
}, index=['2020-02-01', '2020-02-02', '2020-02-02', '2020-02-03'])
# 删除重复的行
df_03 = df_03.drop_duplicates()

# 数据格式不一致或数据类型错误的处理
df_04 = pd.DataFrame({
    'date': ['2023/07/26', '26-07-2023', '2023.07.26']
})
# 将日期转换为统一的格式
df_04['date'] = pd.to_datetime(df_04['date'])
