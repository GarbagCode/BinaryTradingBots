import pandas as pd


def vwap(df: pd.DataFrame) -> pd.Series:
    try:
        if df.empty:
            raise ValueError("DataFrame is empty")
        
        required_cols = ['high', 'low', 'close', 'volume']
        missing_cols = [col for col in required_cols if col not in df.columns]
        if missing_cols:
            raise KeyError(f"Missing required columns: {missing_cols}")
        
        if df[required_cols].isnull().any().any():
            raise ValueError("Null values found in required columns")
        
        if not isinstance(df.index, pd.DatetimeIndex):
            raise TypeError("DataFrame index must be DatetimeIndex")
        
        typical_price = (df['high'] + df['low'] + df['close']) / 3
        df["vwap"] = (typical_price * df['volume']).cumsum() / df['volume'].cumsum()
        
        return df["vwap"]
    
    except Exception as e:
        print(f"Error in Vwap: {e}")
        return None