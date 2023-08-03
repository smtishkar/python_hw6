def portfolio_revenue_calculation(stocks: dict, prices: dict) -> float:
    portfolio = {key: value * prices[key]
                 for key, value in stocks.items() if key in prices}
    sum_portf = sum(portfolio.values())
    return sum_portf
