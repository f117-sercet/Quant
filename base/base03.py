import akshare as ak

if __name__ == '__main__':
    # 获取可转债代码列表
    conbon_list = ak.bond_zh_cov()['债券代码'].tolist()
    #print(conbon_list)
