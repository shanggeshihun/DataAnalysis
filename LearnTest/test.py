# _*_coding:utf-8 _*_

# @Time     :2023/11/23 23:52
# @Author   :anliu
# @File     :test.py
# @Theme    :PyCharm

import pandas as pd
from pivottablejs import pivot_ui
from GenerateOrders import generate_order_data

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 1000)

df = generate_order_data(num_orders=10000)
pivot_ui(df)