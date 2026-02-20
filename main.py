import pandas as pd
from helpful_functions.aggregateTimeFrames import aggregate_time_frame


df = pd.read_csv("data/btcusd_cleaned.csv")

df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s", utc=True)
df.set_index("timestamp", inplace=True)

df_30min = aggregate_time_frame(df, 43800)

print(df_30min.head())

df.to_csv("data/btcusd_43800-min_data.csv")