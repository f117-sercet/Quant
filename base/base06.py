# 导入ashare

import akshare as ak

if __name__ == '__main__':
    # 获取不复权的历史行情数据
    stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol="000001", period="daily", start_date="20170301", end_date='20210907',
                                            adjust="")

    # 获取前复权的历史行情数据
    stock_zh_a_hist_df_qfq = ak.stock_zh_a_hist(symbol="000001", period="daily", start_date="20170301",
                                                end_date='20210907',
                                                adjust="qfq")

    # 获取后复权的历史行情数据
    stock_zh_a_hist_df_hfq = ak.stock_zh_a_hist(symbol="000001", period="daily", start_date="20170301",
                                                end_date='20210907',
                                                adjust="hfq")

# 股票行情数据接口
# stock_bid_ask_em   提供股票的实时买卖报价信息
# 示例
stock_bid_ask_em_df = ak.stock_bid_ask_em(symbol="000001")

# stock_zh_a_spot_em 提供所有A股上市的实时行情数据，
# 包括了股票代码， 名称，最新价，涨跌幅，涨跌额，成交量，成交额，振幅，市盈率等多个字段。
stock_bid_ask_em_df_test1 = ak.stock_bid_ask_em()
# 指数实时行情数据  stock_zh_index_spot
stock_zh_index_spot_df = ak.stock_zh_index_spot_sina()

# 财务报告 stock_financial_report_sina(资产负债表,利润表,现金流量表)

stock_financial_report_sina_df = ak.stock_financial_report_sina(stock="sh600600", symbol="资产负债表")

# 获取股票代码为 "600004" 的财务关键指标
stock_financial_abstract_df = ak.stock_financial_abstract(symbol="600004")
# 接口示例 预测年报每股收益
stock_profit_forecast_ths_df = ak.stock_profit_forecast_ths(symbol="600519", indicator="预测年报每股收益")

# 特色数据
# 1. 主力控盘：机构参与度，stock_comment_detail_zlkp_jgcyd_em
tock_comment_detail_zlkp_jgcyd_em_df = ak.stock_comment_detail_zlkp_jgcyd_em(symbol="600000")

# 2. 资金流向 stock_individual_fund_flow
# 输出：
# 日期、收盘价、涨跌幅（单位: %）、主力净流入-净额、主力净流入-净占比（单位: %）、超大单净流入-净额、超大单净流入-净占比（单位: %）、
# 大单净流入-净额、大单净流入-净占比（单位: %）、中单净流入-净额、中单净流入-净占比（单位: %）、小单净流入-净额、小单净流入-净占比
stock_individual_fund_flow_df = ak.stock_individual_fund_flow(stock="600094", market="sh")