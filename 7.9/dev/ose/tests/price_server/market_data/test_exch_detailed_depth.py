from commontests.price_server.templates.test_exch_detailed_depth_template import BaseDetailedDepth

from ose.tests.utils import (mf_config, mf_option_config, mf_multi_leg_config,
                             futures_filter, fspread_filter, option_filter, ostrategy_filter,
                             bounds_1_1, bounds_20_50, bounds_5_10, bounds_1_10,
                             PFX_enabled, EchoCount)

from ose.tests.overrides import ose_price_overrides

__all__ = ['TestDetailedDepthFutures']

class TestDetailedDepthFutures(BaseDetailedDepth):

    def __init__(self):

        super(TestDetailedDepthFutures, self).__init__()

        self.market_config_and_filters=[(mf_config, [futures_filter])]

        self.visible_levels_and_Aconfig_settings = [(50, [{PFX_enabled : 'true', EchoCount:'0'}])]

        self.price_levels_bounds = bounds_1_1
        self.orders_per_price_level_bounds = bounds_20_50
        self.tradable_price_tick_bounds = bounds_5_10
        self.order_round_lot_multiplier_bounds = bounds_1_10
        self.overrides = ose_price_overrides

class TestDetailedDepthOptions(BaseDetailedDepth):

    def __init__(self):

        super(TestDetailedDepthOptions, self).__init__()

        self.market_config_and_filters=[(mf_option_config, [option_filter])]

        self.visible_levels_and_Aconfig_settings = [(50, [{PFX_enabled : 'true', EchoCount:'0'}])]

        self.price_levels_bounds = bounds_1_1
        self.orders_per_price_level_bounds = bounds_20_50
        self.tradable_price_tick_bounds = bounds_5_10
        self.order_round_lot_multiplier_bounds = bounds_1_10
        self.overrides = ose_price_overrides

class TestDetailedDepthFutures(BaseDetailedDepth):

    def __init__(self):

        super(TestDetailedDepthFutures, self).__init__()

        self.market_config_and_filters=[(mf_multi_leg_config, [fspread_filter, ostrategy_filter])]

        self.visible_levels_and_Aconfig_settings = [(50, [{PFX_enabled : 'true', EchoCount:'0'}])]

        self.price_levels_bounds = bounds_1_1
        self.orders_per_price_level_bounds = bounds_20_50
        self.tradable_price_tick_bounds = bounds_5_10
        self.order_round_lot_multiplier_bounds = bounds_1_10
        self.overrides = ose_price_overrides