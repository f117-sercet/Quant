import pandas as pd

# import pandas as pd

if __name__ == '__main__':
    # 引入Series
    # 使用列表创建 Series
    # eries 是 Pandas 中的一种基本数据结构，
    # 它是一个一维的带标签的数组。
    # Series 可以存储任何数据类型，
    # 包括整数、
    # 浮点数、字符串、
    # Python 对象等。它由数据和索引两部分组成。
    s = pd.Series([1, 2, 3])
    print(s)
    # 访问 Series中的元素
    print(s[2])

    # 创建DataFtame
    # 字典创建
    data = {
        'name': ['Alice', 'Bob', 'Charlie'],
        'age': [20, 30, 40],
        'city': ['New York', 'Los Angeles', 'London']
    }
    df = pd.DataFrame(data)
    print(df)
    # 列表创建 DataFrame
    data = [
        ['Alice', 25, 'New York'],
        ['Bob', 30, 'Los Angeles'],
        ['Charlie', 35, 'London']
    ]
    df = pd.DataFrame(data, columns=['name', 'age', 'city'])
    print('df2', df)
