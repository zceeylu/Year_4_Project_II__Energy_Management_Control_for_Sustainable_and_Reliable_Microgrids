import pandas as pd
import numpy as np

# 读取三个CSV文件，代码保持不变
df_location1 = pd.read_csv('E:/acn_data/hourly_kwh_delivered_1.csv', parse_dates=['Hour'])
df_location2 = pd.read_csv('E:/acn_data/hourly_kwh_delivered_2.csv', parse_dates=['Hour'])
df_location3 = pd.read_csv('E:/acn_data/hourly_kwh_delivered_3.csv', parse_dates=['Hour'])

# 设置时间索引，代码保持不变
df_location1.set_index('Hour', inplace=True)
df_location2.set_index('Hour', inplace=True)
df_location3.set_index('Hour', inplace=True)

# 对齐三个数据集，代码保持不变
combined_df = pd.concat(
    [df_location1, df_location2, df_location3],
    axis=1,
    join='outer',
    keys=['Location1_kWh', 'Location2_kWh', 'Location3_kWh']
)

# 填充NaN值为0，代码保持不变
combined_df.fillna(0, inplace=True)

# 计算总充电量，代码保持不变
combined_df['Total_kWh'] = combined_df.sum(axis=1)

# 确定时间范围
start_date = combined_df.index.min()
end_date = combined_df.index.max()
all_hours = pd.date_range(start=start_date, end=end_date, freq='H')

# 重新索引以包含所有小时，缺失的时间点将自动填充为NaN
combined_df = combined_df.reindex(all_hours)

# 再次填充NaN值为0
combined_df.fillna(0, inplace=True)

# 重置索引以将时间列变回一个普通列，注意此时索引名为None，需要手动指定
combined_df.reset_index(inplace=True)
combined_df.rename(columns={'index': 'Hour'}, inplace=True)

# 将合并后的DataFrame保存为新的CSV文件
combined_df.to_csv('E:/acn_data/combined_hourly_csv.csv', index=False)
