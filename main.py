import pandas as pd
from helpful_functions.aggregateTimeFrames import aggregate_time_frame


df = pd.read_csv("data/btcusd_cleaned.csv")

df.index = pd.to_datetime(df["timestamp"], unit="s", utc="True")

df_30min = aggregate_time_frame(df[29:], 30)

print(df_30min.head())

df.to_csv("data/btcusd_30-min_data.csv")