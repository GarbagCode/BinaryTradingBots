def support_resistance(df, lookback=5):
    """
    Calculate support and resistance levels
    
    Returns:
    - resistance: 1 if close > max close of last N bars, else 0
    - support: 1 if close < min low of last N bars, else 0
    """
    try:
        if df.empty:
            raise ValueError("DataFrame is empty")
        
        if 'close' not in df.columns or 'low' not in df.columns:
            raise KeyError("'close' and 'low' columns required")
        
        # Resistance: close higher than previous N bars' closes
        resistance = (df['close'] > df['close'].shift(1).rolling(window=lookback).max()).astype(int)
        
        # Support: close lower than previous N bars' lows
        support = (df['close'] < df['low'].shift(1).rolling(window=lookback).min()).astype(int)
        
        return df.assign(
            resistance=resistance,
            support=support
        )
    
    except Exception as e:
        print(f"Error in support_resistance: {e}")
        return None