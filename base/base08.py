import empyrical as ep
import quantstats as qs

if __name__ == '__main__':
    # 收益评价指标
    # 总收益率 = (投资结束时的资产价值 / 投资初始时的资产价值 - 1) * 100 %

    ep.cum_returns_final(returns="")

    # 年华收益率 年化收益率的计算公式为：
    # 年化收益率 = (1 + 总收益率) ^ (1 / 投资年数) - 1
    ep.annual_return(returns="", period='monthly')
    # 胜率= 盈利交易次数 / 总交易次数
    win_rate = qs.stats.win_rate(returns="")
    # 盈亏次数比 = 盈利交易次数 / 亏损交易次数
    win_rate / (1 - win_rate)
    # 赔率=平均盈利金额 / 平均亏损金额 或  赔率 = 总盈利金额 / 总亏损金额
    qs.stats.win_loss_ratio(returns="")  # 平均盈利金额 / 平均亏损金额
    qs.stats.profit_factor(returns="")  # 总盈利金额 / 总亏损金额

    # 期望收益 = 胜率 * 平均盈利金额 - (1 - 胜率) * 平均亏损金额

    win_rate = qs.stats.win_rate(returns="")  # 胜率
    avg_win = qs.stats.avg_win(returns="")  # 平均盈利金额
    avg_loss = qs.stats.avg_loss(returns="")  # 平均亏损金额
    win_rate * avg_win - (1 - win_rate) * avg_loss  # 期望收益

    # 期望收益曲线
    qs.plots.returns(returns="", benchmark="")

    # 年度收益柱状图
    qs.plots.yearly_returns(returns="", benchmark="")

    # 分期柱状图
    qs.plots.daily_returns(returns="", benchmark="")

    # 月度收益热图
    qs.plots.monthly_heatmap(returns="")