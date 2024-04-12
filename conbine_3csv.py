import pandas as pd

# 读取三个CSV文件
df_location1 = pd.read_csv('E:/acn_data/hourly_kwh_delivered_1.csv', parse_dates=['Hour'])
df_location2 = pd.read_csv('E:/acn_data/hourly_kwh_delivered_2.csv', parse_dates=['Hour'])
df_location3 = pd.read_csv('E:/acn_data/hourly_kwh_delivered_3.csv', parse_dates=['Hour'])

# 为每个地点的数据设置时间索引
df_location1.set_index('Hour', inplace=True)
df_location2.set_index('Hour', inplace=True)
df_location3.set_index('Hour', inplace=True)

# 对齐三个数据集，使用outer join确保所有时间点都被保留
combined_df = pd.concat(
    [df_location1, df_location2, df_location3],
    axis=1,
    join='outer',
    keys=['Location1_kWh', 'Location2_kWh', 'Location3_kWh']
)

# 填充NaN值为0，如果你更倾向于保留NaN，可以跳过这一步
combined_df.fillna(0, inplace=True)

# 计算总充电量
combined_df['Total_kWh'] = combined_df.sum(axis=1)

# 重置索引以将时间列变回一个普通列
combined_df.reset_index(inplace=True)

# 将合并后的DataFrame保存为新的CSV文件
combined_df.to_csv('E:/acn_data/combined0_csv.csv', index=False)
