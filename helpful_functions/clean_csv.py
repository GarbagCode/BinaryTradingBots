import pandas as pd

df = pd.read_csv("data/btcusd_1-min_data.csv")
df["Timestamp"] = pd.to_datetime(df["Timestamp"], unit="s")
df.columns = df.columns.str.lower()

df.set_index("timestamp", inplace=True)

# Save to CSV
df.to_csv("data/btcusd_cleaned.csv", index=True)

print(df.tail())