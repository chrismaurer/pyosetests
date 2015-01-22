# python imports
import sys 

# commontests imports
from commontests.order_server.order_management.suites import (OrderManagementSmokeSuiteGenerator,
                                                              LARGE_SMOKE_GROUP,
                                                              SMALL_SMOKE_GROUP)
from ose.tests.features import gateway
from ose.tests.order_alterations import *

large_smoke_suite_gen = OrderManagementSmokeSuiteGenerator(gateway, LARGE_SMOKE_GROUP)
large_smoke_suite_gen(sys.modules[__name__])

small_smoke_suite_gen = OrderManagementSmokeSuiteGenerator(gateway, SMALL_SMOKE_GROUP)
small_smoke_suite_gen(sys.modules[__name__])