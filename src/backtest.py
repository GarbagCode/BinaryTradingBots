def plot_equity_curve(df, predictions, actual_prices):
    """
    Plot equity curve - line goes up on correct predictions, down on wrong ones
    
    predictions: model predictions (0 or 1)
    actual_prices: actual close prices
    """
    # Calculate if prediction was correct
    actual_direction = (actual_prices.shift(-1) > actual_prices).astype(int)
    correct = (predictions == actual_direction).astype(int)
    
    # Create equity curve (cumulative wins/losses)
    # +1 for correct, -1 for wrong
    pnl = correct.replace(0, -1)
    equity = pnl.cumsum()
    
    plt.figure(figsize=(14, 6))
    plt.plot(df.index, equity, linewidth=2, color='blue')
    plt.axhline(y=0, color='black', linestyle='--', alpha=0.5)
    
    plt.fill_between(df.index, equity, 0, where=(equity >= 0), alpha=0.3, color='green', label='Profit')
    plt.fill_between(df.index, equity, 0, where=(equity < 0), alpha=0.3, color='red', label='Loss')
    
    plt.xlabel('Time')
    plt.ylabel('Cumulative Wins/Losses')
    plt.title('Equity Curve (Wins +1, Losses -1)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
    
    # Print stats
    total_trades = len(equity)
    wins = (correct == 1).sum()
    losses = (correct == 0).sum()
    win_rate = wins / total_trades * 100
    
    print(f"Total Trades: {total_trades}")
    print(f"Wins: {wins}")
    print(f"Losses: {losses}")
    print(f"Win Rate: {win_rate:.2f}%")
    print(f"Final Equity: {equity.iloc[-1]}")

# Usage:
# predictions = model.predict(X_test)
# plot_equity_curve(df_test, predictions, df_test['close'].values)