def each_equity_sum (stocks: dict, prices: dict) -> dict:
    result = {key: value * prices[key] for key, value in stocks.items()}
    return result