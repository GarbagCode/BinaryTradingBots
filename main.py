import kagglehub

# Download latest version
path = kagglehub.dataset_download("mczielinski/bitcoin-historical-data", output_dir="/workspaces/BinaryTradingBots/data")

print("Path to dataset files:", path)