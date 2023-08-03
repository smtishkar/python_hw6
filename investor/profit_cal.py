def get_most_profitable_stock(stocks: dict, prices: dict) -> str:
    dict_result = {key: value * prices[key] for key, value in stocks.items()}
    max_valueable_equity = max(dict_result, key=dict_result.get)
    return max_valueable_equity


def max_growth_in_money(stocks: dict, initial_prices: dict, current_prices: dict) -> dict:
    result = {key: value * (current_prices[key] - initial_prices[key])
              for key, value in stocks.items() if key in initial_prices}
    max_result = max(result, key=result.get)
    print(f"Прирост за период по кадой акции - {result} ")
    return max_result
