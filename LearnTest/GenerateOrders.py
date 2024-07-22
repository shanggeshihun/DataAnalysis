# _*_coding:utf-8 _*_

# @Time     :2023/11/23 23:47
# @Author   :anliu
# @File     :GenerateOrders.py
# @Theme    :PyCharm

import pandas as pd
import numpy as np
import random
from faker import Faker

def generate_order_data(num_orders=10000, num_customers=100, num_products=40, num_addresses=100,
                        num_categories=10, num_promotions=8, seed=42):
    # 设置随机数种子，以确保每次运行生成相同的数据
    np.random.seed(seed)
    random.seed(seed)

    # 创建Faker对象，用于生成虚假数据
    fake = Faker()

    # 生成指定数量的不同顾客姓名、产品名称、地址、产品类别、促销活动
    customer_names = [fake.name() for _ in range(num_customers)]
    product_names = [fake.word() for _ in range(num_products)]
    shipping_addresses = [fake.address() for _ in range(num_addresses)]
    product_categories = [fake.word() for _ in range(num_categories)]
    promotion_activities = [fake.word() for _ in range(num_promotions)]

    # 生成订单数据
    order_data = {
        'order_id': [f"ORD{i}" for i in range(1, num_orders + 1)],
        'customer_name': random.choices(customer_names, k=num_orders),
        'product_name': random.choices(product_names, k=num_orders),
        'product_price': [round(random.uniform(10, 1000), 2) for _ in range(num_orders)],
        'product_quantity': [random.randint(1, 10) for _ in range(num_orders)],
        'order_date': [fake.date_time_this_decade() for _ in range(num_orders)],
        'shipping_company': [fake.company() for _ in range(num_orders)],
        'tracking_number': [fake.uuid4() for _ in range(num_orders)],
        'shipping_status': [random.choice(['shipped', 'delivered', 'in_transit']) for _ in range(num_orders)],
        'shipping_address': random.choices(shipping_addresses, k=num_orders),
        'contact_number': [fake.phone_number() for _ in range(num_orders)],
        'email_address': [fake.email() for _ in range(num_orders)],
        'payment_method': [random.choice(['alipay', 'wechat_pay', 'credit_card']) for _ in range(num_orders)],
        'order_status': [random.choice(['completed', 'pending_payment', 'cancelled']) for _ in range(num_orders)],
        'product_category': random.choices(product_categories, k=num_orders),
        'discount_information': [fake.word() for _ in range(num_orders)],
        'refund_information': [fake.word() for _ in range(num_orders)],
        'invoice_information': [fake.word() for _ in range(num_orders)],
        'customer_review': [fake.text() for _ in range(num_orders)],
        'customer_level': [random.choice(['regular_member', 'advanced_member', 'vip_member']) for _ in range(num_orders)],
        'after_sales_service': [fake.word() for _ in range(num_orders)],
        'promotion_activity': random.choices(promotion_activities, k=num_orders)
    }

    # 创建DataFrame
    df = pd.DataFrame(order_data)
    return df

if __name__ == '__main__':
    # 示例：生成包含1000行数据的订单信息
    order_df = generate_order_data(num_orders=1000)
    # 显示前5行数据
    print(order_df.head())
