# 引入包
import pandas as pd
import sqlite3
import akshare as ak

if __name__ == '__main__':
    # 获取数据
    df = ak.stock_zh_a_hist(symbol="600000", period="daily", start_date="20200101", end_date='20221231',
                            adjust="")  # 通过akshare接口获取数据
    print(df)  # 输出数据查看

    file_path = 'd:temp/data.db'  # 设置数据库的路径和文件名
    conn = sqlite3.connect(file_path)  # 创建数据库连接

    # 写入数据库

    df.to_sql("600000", conn, if_exists='replace', index=False)

    # 读取数据
    sql = "select * from '600000'"
    dfs = pd.read_sql_query(sql, conn)

    print("df_01", dfs)

    # 关闭数据库
    conn.close()