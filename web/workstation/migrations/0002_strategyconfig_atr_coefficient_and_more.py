# Generated by Django 4.2.8 on 2024-02-20 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workstation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='strategyconfig',
            name='atr_coefficient',
            field=models.DecimalField(decimal_places=6, default=1, max_digits=36, verbose_name='ATR动态止损系数'),
        ),
        migrations.AlterField(
            model_name='strategyconfig',
            name='strategy_cls',
            field=models.CharField(choices=[('leek.strategy.strategy_atr|ATRHeikinAshiStrategy', 'ATR混合策略'), ('leek.strategy.strategy_mean_reverting|MeanRevertingStrategy', '均值回归'), ('leek.strategy.strategy_bollinger_bands|BollingerBandsStrategy', '布林带策略'), ('leek.strategy.strategy_grid|SingleGridStrategy', '单标的单方向网格策略')], default='', max_length=200, verbose_name='策略'),
        ),
        migrations.AlterField(
            model_name='strategyconfig',
            name='total_amount',
            field=models.DecimalField(decimal_places=12, default='1000', max_digits=36, verbose_name='投入总资产'),
        ),
    ]
