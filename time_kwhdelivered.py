import pandas as pd
import json
from datetime import timedelta

# 加载数据
file_path = 'E:/acn_data/acndata_sessions_3.json'
with open(file_path, 'r') as file:
    data = json.load(file)
df = pd.json_normalize(data["_items"], errors='ignore')

# 保留需要的字段并转换日期时间格式
df['connectionTime'] = pd.to_datetime(df['connectionTime'], errors='coerce', utc=True)
df['disconnectTime'] = pd.to_datetime(df['disconnectTime'], errors='coerce', utc=True)
df = df.dropna(subset=['connectionTime', 'disconnectTime', 'kWhDelivered'])

# 计算每个会话的小时分布和对应的kWh
def distribute_kwh_over_hours(row):
    start_hour = row['connectionTime'].floor('H')
    end_hour = row['disconnectTime'].ceil('H')
    total_hours = int((end_hour - start_hour).total_seconds() / 3600)
    kwh_per_hour = row['kWhDelivered'] / total_hours if total_hours > 0 else 0
    hours = pd.date_range(start=start_hour, end=end_hour, freq='H')

    return pd.Series([kwh_per_hour] * len(hours), index=hours)

# 应用函数并创建一个新的DataFrame
hourly_kwh = df.apply(distribute_kwh_over_hours, axis=1).stack().reset_index(level=1)
hourly_kwh.columns = ['Hour', 'kWhDeliveredPerHour']

# 聚合数据以计算每小时的平均kWh
hourly_kwh_avg = hourly_kwh.groupby('Hour').mean()

# 保存到CSV文件
output_file_path = 'E:/acn_data/hourly_kwh_delivered_3.csv'
hourly_kwh_avg.to_csv(output_file_path)

print(f"文件已保存至 {output_file_path}")
