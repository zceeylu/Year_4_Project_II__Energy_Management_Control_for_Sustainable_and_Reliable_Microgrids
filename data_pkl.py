
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import json

file_path = 'E:/acn_data/acndata_sessions_1.json'  # 文件路径
with open(file_path, 'r') as file:
    data = json.load(file)

# 预处理步骤，确保每个'userInputs'至少是空列表
for item in data["_items"]:
    if item.get("userInputs") is None:
        item["userInputs"] = []

# 使用json_normalize处理数据
df = pd.json_normalize(data["_items"], record_path='userInputs', 
                       meta=['_id', 'clusterID', 'connectionTime', 'disconnectTime', 
                             'doneChargingTime', 'kWhDelivered', 'sessionID', 
                             'siteID', 'spaceID', 'stationID', 'timezone', 'userID'],
                       errors='ignore', record_prefix='userInputs_')

# 转换日期时间字段
date_fields = ['connectionTime', 'disconnectTime', 'doneChargingTime', 'userInputs_modifiedAt', 'userInputs_requestedDeparture']
for field in date_fields:
    # 使用 errors='coerce' 来处理无法解析为日期的任何值，将它们转换为NaT
    df[field] = pd.to_datetime(df[field], utc=True, errors='coerce')


# 计算充电时长（分钟）
df['chargingDuration'] = (df['disconnectTime'] - df['connectionTime']).dt.total_seconds() / 60

# 提取充电开始的小时
df['startHour'] = df['connectionTime'].dt.hour

# 规范化kWhDelivered
scaler = MinMaxScaler()
df['kWhDelivered_normalized'] = scaler.fit_transform(df[['kWhDelivered']].astype(float))

# 查看处理后的DataFrame
print(df.head())