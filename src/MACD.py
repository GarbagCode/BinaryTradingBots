def macd(df, fast=12, slow=26, signal=9):
    """
    Calculate MACD (Moving Average Convergence Divergence)
    
    Returns dataframe with:
    - macd_line: fast EMA - slow EMA
    - signal_line: EMA of MACD line
    - macd_histogram: MACD line - signal line
    """
    try:
        if df.empty:
            raise ValueError("DataFrame is empty")
        
        if 'close' not in df.columns:
            raise KeyError("'close' column not found")
        
        # Calculate EMAs
        ema_fast = df['close'].ewm(span=fast, adjust=False).mean()
        ema_slow = df['close'].ewm(span=slow, adjust=False).mean()
        
        # MACD line
        macd_line = ema_fast - ema_slow
        
        # Signal line (EMA of MACD)
        signal_line = macd_line.ewm(span=signal, adjust=False).mean()
        
        # Histogram
        macd_histogram = macd_line - signal_line
        
        return macd_line

    
    except Exception as e:
        print(f"Error in MACD: {e}")
        return None