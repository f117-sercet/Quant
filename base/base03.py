
import pymongo

if __name__ == '__main__':
    # 获取可转债代码列表
    # conbon_list = ak.bond_zh_cov()['转债代码'].tolist()
    # print(conbon_list)

    # 连接mongo
    client = pymongo.MongoClient(host='localhost', port=27017)
    dbs=client.list_database_names()
    print(dbs)
