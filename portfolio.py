from investor.initial_port_calc import portfolio_revenue_calculation
from investor.portfolio_growth import calculate_portfolio_return
from investor.profit_cal import get_most_profitable_stock, max_growth_in_money
from investor.equities_one_by_one import each_equity_sum


initial_stocks = {"AAPL": 30, "GOOGL": 5, "MSFT": 8 }
initial_prices = {"AAPL": 150.25, "GOOGL": 2500.75, "MSFT": 300.50}
current_prices = {"AAPL": 200.25, "GOOGL": 2750.75, "MSFT": 350.50} 


initial_portfolio_sum = portfolio_revenue_calculation(initial_stocks,initial_prices)
current_portfolio_sum = portfolio_revenue_calculation(initial_stocks,current_prices)
growth = calculate_portfolio_return(initial_portfolio_sum, current_portfolio_sum)
sum_each = each_equity_sum(initial_stocks, current_prices)
most_profit_eq = get_most_profitable_stock(initial_stocks, current_prices)
max_equity_growth = max_growth_in_money (initial_stocks, initial_prices, current_prices)


print(f"Базовая стоимость портфеля - {initial_portfolio_sum}")
print(f"Текущая стоимость портфеля - {current_portfolio_sum}")
print(f'Прирост составляет - {growth}%')
print(f"Стоимость каждой из акций отдельно {sum_each}")
print(f"Самая дорогая акция в портефел - {most_profit_eq}")
print(f"Максимальный прирост показала акция - {max_equity_growth}")