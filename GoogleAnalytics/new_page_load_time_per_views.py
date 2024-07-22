# _*_coding:utf-8 _*_
# @Time     : 2024/7/22 23:31
# @Author   : anliu
# @File     : new_page_load_time_per_views.py
# @Theme    : PyCharm

import pandas as pd
df_csv = pd.read_csv(r'./new_page_load_time_per_views/download_0708-0721.csv', skiprows=2, header=[3, 4])
df_csv.reset_index(inplace=True, drop=False)
print(df_csv.head())
country_list = list(df_csv.iloc[:, 0])
print(country_list)

columns_list = list(df_csv.columns)[2:]
print(columns_list)

df = pd.DataFrame()
for idx, tup in enumerate(columns_list):
    dt = tup[0]
    metric_name = tup[1]
    metric = df_csv.iloc[:, idx + 1].tolist()
    l = len(metric)

    tmp_df = pd.DataFrame(
        {
            'country': country_list,
            'dt': [dt] * l,
            'metric_name': [metric_name] * l,
            'metric': metric
        }
    )
    df = pd.concat([df, tmp_df], axis=0)
df.reset_index(inplace=True, drop=True)
df['metric2'] = df.apply(lambda row: row['metric']/1000 if row['metric_name']== 'new_page_load_time per views' else row['metric'], axis=1)

df.to_excel(r'./new_page_load_time_per_views_merge.xlsx')



