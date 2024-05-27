#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/5/7 22:40
# @Author  : shenglin.li
# @File    : strategy_turtle_test.py
# @Software: PyCharm
import decimal
import unittest

import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objs as go

from leek.common import EventBus
from leek.runner.view import ViewWorkflow
from leek.strategy.common import PositionDirectionManager
from leek.strategy.common.strategy_common import PositionRateManager
from leek.strategy.common.strategy_filter import JustFinishKData, DynamicRiskControl
from leek.strategy.strategy_rsi import RSIStrategy
from leek.strategy.strategy_td import TDStrategy
from leek.trade.trade import PositionSide


class TestRSI(unittest.TestCase):
    def test_handle(self):
        self.strategy = RSIStrategy(period=14, over_buy=85, over_sell=20)
        # self.strategy.rsi_type = ["CLA", "MOM", "IBS"]
        self.strategy.rsi_type = ["CLA"]

        PositionDirectionManager.__init__(self.strategy, PositionSide.LONG)
        PositionRateManager.__init__(self.strategy, "1")
        JustFinishKData.__init__(self.strategy, "False")
        DynamicRiskControl.__init__(self.strategy, "1.3", "0.02")
        self.bus = EventBus()

        workflow = ViewWorkflow(self.strategy, "1d", "2006-01-01", "2024-02-28", "000300", 1)
        # workflow = ViewWorkflow(self.strategy, "15m", "2024-03-15", "2024-05-24", "ETH-USDT-SWAP")
        # workflow = ViewWorkflow(self.strategy, "4h", "2024-03-15", "2024-05-24", "BTC-USDT-SWAP")

        workflow.start()
        df = pd.DataFrame([x.__json__() for x in workflow.kline_data_g])
        df['Datetime'] = pd.to_datetime(df['timestamp'] + 8 * 60 * 60 * 1000, unit='ms')
        fig = make_subplots(rows=3, cols=1, shared_xaxes=True)
        df["benchmark"] = df["close"] / df.iloc[1]["close"]
        df["profit"] = df["balance"] / decimal.Decimal("1000")
        fig.add_trace(go.Scatter(x=df['Datetime'], y=df['benchmark'], mode='lines', name='benchmark'), row=2, col=1)
        fig.add_trace(go.Scatter(x=df['Datetime'], y=df['profit'], mode='lines', name='profit'), row=2, col=1)
        fig.add_trace(go.Scatter(x=df['Datetime'], y=df['rsi'], mode='lines', name='rsi'), row=3, col=1)
        workflow.draw(fig=fig, df=df)
        print(len(df))
        fig.show()


if __name__ == '__main__':
    unittest.main()
