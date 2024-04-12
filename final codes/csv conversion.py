import pandas as pd

file_path = r'C:\Users\Lu34\OneDrive\Desktop\Year 4 Project II\Matlab simulation\acn_data\final codes\combined_hourly_csv.pkl'

df = pd.read_pickle(file_path)

print(df.describe())
# Display the first few rows of the DataFrame
print("First few rows of the DataFrame:")
print(df.head(100))

# Export DataFrame to CSV
csv_output_path = r'C:\Users\Lu34\OneDrive\Desktop\Year 4 Project II\Matlab simulation\acn_data\final codes\combined_hourly_csv.csv'
df.to_csv(csv_output_path, index=True)

