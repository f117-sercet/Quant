# 导入 tushare
import tushare as ts

if __name__ == '__main__':
    token = "06f7fc75f4adac10ab1876df718d29efc90c9fba8d099f1ac1c6c574"
    ts.set_token(token)
    pro = ts.pro_api()

    # 查询当前所有正常上市交易的股票
    # ts_code（类型：str）：TS股票代码，不是必须输入的参数。
    # name(类型：str):股票名称代码
    # market（类型：str）：市场类别，包括主板、创业板、科创板、CDR和北交所，不是必须输入的参数。
    # list_status（类型：str）：上市状态，L代表上市，D代表退市，P代表暂停上市，默认是L，不是必须输入的参数。
    # exchange（类型：str）：交易所，包括SSE上交所、SZSE深交所和BSE北交所，不是必须输入的参数。
    # is_hs（类型：str）：是否为沪深港通标的，N代表否，H代表沪股通，S代表深股通，不是必须输入的参数。

    # 输出参数
    # ts_code（类型：str）：Tushare中的代码，将会默认显示。
    # symbol（类型：str）：股票代码，将会默认显示。
    # name（类型：str）：股票名称，将会默认显示。
    # area（类型：str）：公司地域，将会默认显示。
    # industry（类型：str）：所属行业，将会默认显示。
    # market（类型：str）：市场类型（主板 / 创业板 / 科创板 / CDR），将会默认显示。
    # list_date（类型：str）：上市日期，将会默认显示。
    data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
    # print(data)

    # 获取行情数据 ########

    # 查询单个股票带日线行情
    df = pro.daily(ts_code='000001.SZ', start_date='20180701', end_date='20180718')
    # 查询多个股票的日线行情
    df_list=pro.daily(ts_code='000001.SH',start_date='20180701', end_date='20180718')
    # 查询某一天全部股票的日线行情
    df_one_list = pro.daily(trade_date='20180701')

    # 获取财务数据

