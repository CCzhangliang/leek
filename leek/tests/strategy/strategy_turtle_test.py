#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/5/7 22:40
# @Author  : shenglin.li
# @File    : strategy_turtle_test.py
# @Software: PyCharm
import decimal
import unittest

import numpy as np
import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots

from leek.common import EventBus
from leek.runner.view import ViewWorkflow
from leek.strategy import BaseStrategy
from leek.strategy.common import PositionDirectionManager
from leek.strategy.common.strategy_common import PositionRateManager
from leek.strategy.strategy_turtle import TurtleTradingStrategy, TurtleTrading1Strategy, TurtleTrading2Strategy, \
    TurtleTrading3Strategy
from leek.trade.trade import PositionSide


class TestTurtle(unittest.TestCase):
    def setUp(self):
        self.strategy = TurtleTradingStrategy()
        # self.strategy = TurtleTrading1Strategy()
        # self.strategy = TurtleTrading2Strategy()
        # TurtleTrading1Strategy.__init__(self.strategy)
        # TurtleTradingStrategy.__init__(self.strategy)

        PositionDirectionManager.__init__(self.strategy, PositionSide.FLAT)
        PositionRateManager.__init__(self.strategy, "0.3")
        self.bus = EventBus()
        BaseStrategy.__init__(self.strategy, "V0", self.bus, decimal.Decimal("1000"))

    def test_handle(self):
        self.strategy = TurtleTradingStrategy()
        PositionDirectionManager.__init__(self.strategy, PositionSide.LONG)
        PositionRateManager.__init__(self.strategy, "1")
        TurtleTradingStrategy.__init__(self.strategy)
        self.bus = EventBus()
        workflow = ViewWorkflow(self.strategy, "1d", 1609459200000, 1715159848986, "000300", 1)

        workflow.start()
        df = pd.DataFrame([x.__json__() for x in workflow.kline_data_g])
        df['Datetime'] = pd.to_datetime(df['timestamp'] + 8 * 60 * 60 * 1000, unit='ms')
        fig = make_subplots(rows=1, cols=1, shared_xaxes=True)
        # 添加开仓通道
        fig.add_trace(go.Scatter(x=df['Datetime'], y=df['open_channel_up'], mode='lines', name='上轨(开)'), row=1, col=1)
        # fig.add_trace(go.Scatter(x=df['Datetime'], y=df['close_channel_up'], mode='lines', name='上轨(平)'), row=1, col=1)
        # fig.add_trace(go.Scatter(x=df['Datetime'], y=df['open_channel_lower'], mode='lines', name='下轨(开)'), row=1, col=1)
        fig.add_trace(go.Scatter(x=df['Datetime'], y=df['close_channel_lower'], mode='lines', name='下轨(平)'), row=1, col=1)
        # fig.add_trace(go.Scatter(x=df['Datetime'], y=df['vhf'], mode='lines', name='VHF'), row=2, col=1)
        workflow.draw(fig=fig, df=df)
        print(len(df))
        fig.show()

    def test_handle1(self):
        self.strategy = TurtleTrading1Strategy()
        PositionDirectionManager.__init__(self.strategy, PositionSide.LONG)
        PositionRateManager.__init__(self.strategy, "1")
        TurtleTradingStrategy.__init__(self.strategy)
        self.bus = EventBus()
        workflow = ViewWorkflow(self.strategy, "1d", 1609459200000, 1715159848986, "000300", 1)

        workflow.start()
        df = pd.DataFrame([x.__json__() for x in workflow.kline_data_g])
        df['Datetime'] = pd.to_datetime(df['timestamp'] + 8 * 60 * 60 * 1000, unit='ms')
        fig = make_subplots(rows=1, cols=1, shared_xaxes=True)
        # 添加开仓通道
        fig.add_trace(go.Scatter(x=df['Datetime'], y=df['open_channel_up'], mode='lines', name='上轨(开)'), row=1, col=1)
        # fig.add_trace(go.Scatter(x=df['Datetime'], y=df['close_channel_up'], mode='lines', name='上轨(平)'), row=1, col=1)
        # fig.add_trace(go.Scatter(x=df['Datetime'], y=df['open_channel_lower'], mode='lines', name='下轨(开)'), row=1, col=1)
        fig.add_trace(go.Scatter(x=df['Datetime'], y=df['close_channel_lower'], mode='lines', name='下轨(平)'), row=1, col=1)
        # fig.add_trace(go.Scatter(x=df['Datetime'], y=df['vhf'], mode='lines', name='VHF'), row=2, col=1)
        workflow.draw(fig=fig, df=df)
        print(len(df))
        fig.show()

    def test_handle2(self):
        self.strategy = TurtleTrading2Strategy()
        PositionDirectionManager.__init__(self.strategy, PositionSide.LONG)
        PositionRateManager.__init__(self.strategy, "1")
        TurtleTradingStrategy.__init__(self.strategy)
        TurtleTrading1Strategy.__init__(self.strategy)
        self.bus = EventBus()
        workflow = ViewWorkflow(self.strategy, "1d", 1609459200000, 1715159848986, "000300", 1)

        workflow.start()
        df = pd.DataFrame([x.__json__() for x in workflow.kline_data_g])
        df['Datetime'] = pd.to_datetime(df['timestamp'] + 8 * 60 * 60 * 1000, unit='ms')
        fig = make_subplots(rows=1, cols=1, shared_xaxes=True)
        # 添加开仓通道
        fig.add_trace(go.Scatter(x=df['Datetime'], y=df['open_channel_up'], mode='lines', name='上轨(开)'), row=1, col=1)
        # fig.add_trace(go.Scatter(x=df['Datetime'], y=df['close_channel_up'], mode='lines', name='上轨(平)'), row=1, col=1)
        # fig.add_trace(go.Scatter(x=df['Datetime'], y=df['open_channel_lower'], mode='lines', name='下轨(开)'), row=1, col=1)
        fig.add_trace(go.Scatter(x=df['Datetime'], y=df['close_channel_lower'], mode='lines', name='下轨(平)'), row=1, col=1)
        # fig.add_trace(go.Scatter(x=df['Datetime'], y=df['vhf'], mode='lines', name='VHF'), row=2, col=1)
        workflow.draw(fig=fig, df=df)
        print(len(df))
        fig.show()

    def test_handle3(self):
        self.strategy = TurtleTrading3Strategy()
        PositionDirectionManager.__init__(self.strategy, PositionSide.LONG)
        PositionRateManager.__init__(self.strategy, "1")
        TurtleTradingStrategy.__init__(self.strategy)
        TurtleTrading1Strategy.__init__(self.strategy)
        TurtleTrading2Strategy.__init__(self.strategy)
        self.bus = EventBus()
        workflow = ViewWorkflow(self.strategy, "4h", 1609459200000, 1715159848986, "BTCUSDT")

        workflow.start()
        df = pd.DataFrame([x.__json__() for x in workflow.kline_data_g])
        df['Datetime'] = pd.to_datetime(df['timestamp'] + 8 * 60 * 60 * 1000, unit='ms')
        fig = make_subplots(rows=1, cols=1, shared_xaxes=True)
        # 添加开仓通道
        fig.add_trace(go.Scatter(x=df['Datetime'], y=df['open_channel_up'], mode='lines', name='上轨(开)'), row=1, col=1)
        # fig.add_trace(go.Scatter(x=df['Datetime'], y=df['close_channel_up'], mode='lines', name='上轨(平)'), row=1, col=1)
        # fig.add_trace(go.Scatter(x=df['Datetime'], y=df['open_channel_lower'], mode='lines', name='下轨(开)'), row=1, col=1)
        fig.add_trace(go.Scatter(x=df['Datetime'], y=df['close_channel_lower'], mode='lines', name='下轨(平)'), row=1, col=1)
        # fig.add_trace(go.Scatter(x=df['Datetime'], y=df['vhf'], mode='lines', name='VHF'), row=2, col=1)
        workflow.draw(fig=fig, df=df)
        print(len(df))
        fig.show()


if __name__ == '__main__':
    pass
