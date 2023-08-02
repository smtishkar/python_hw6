# будет содержать функции для выполнения следующих операций:
# Расчет общей стоимости портфеля акций: Функция calculate_portfolio_value(stocks: dict, prices: dict) -> float принимает 
# два аргумента: stocks - словарь, где ключами являются символы акций (например, "AAPL" для Apple Inc.), 
# и значениями - количество акций каждого символа. prices - словарь, где ключами являются символы акций, а значениями 
# - текущая цена каждой акции. Функция должна вернуть общую стоимость портфеля акций на основе количества акций и их текущих цен. 
# Пример: Пришло
# stocks = {"AAPL": 10, "GOOGL": 5, "MSFT": 8}
# prices = {"AAPL": 150.25, "GOOGL": 2500.75, "MSFT": 300.50}
# Вышло:
# 16410,25



initial_stocks = {"AAPL": 10, "GOOGL": 5, "MSFT": 8 }
initial_prices = {"AAPL": 150.25, "GOOGL": 2500.75, "MSFT": 300.50}

# initial_stocks = {"AAPL": 10, "GOOGL": 5, "MSFT": 8 }  #Беру что количество акций постоянно
current_prices = {"AAPL": 200.25, "GOOGL": 2750.75, "MSFT": 350.50} 


def portfolio_revenue_calculation(stocks: dict, prices: dict) -> float:
    portfolio = {key : value * prices[key] for key, value in stocks.items() if key in prices}
    sum_portf = sum(portfolio.values()) 
    return sum_portf


initial_portfolio_sum = portfolio_revenue_calculation(initial_stocks,initial_prices)
print(initial_portfolio_sum)
current_portfolio_sum = portfolio_revenue_calculation(initial_stocks,current_prices)
print(current_portfolio_sum)


# portfolio = {key : value * current_prices[key] for key, value in initial_stocks.items() if key in current_prices}
# sum_portf = sum(portfolio.values()) 

# print(portfolio)
# print(sum_portf)


# Расчет доходности портфеля: Функция calculate_portfolio_return(initial_value: float, current_value: float) -> float 
# принимает два аргумента: initial_value - начальная стоимость портфеля акций. current_value - текущая стоимость портфеля акций.
#  Функция должна вернуть процентную доходность портфеля. Пример:
# Пришло:
# 10000.0
# 15000.0
# Вышло:
# 50%

def calculate_portfolio_return(initial_value: float, current_value: float) -> float:            #Сделать округление
    result = ((current_value-initial_value)/initial_value)*100
    return result

growth = calculate_portfolio_return(initial_portfolio_sum, current_portfolio_sum)
print(f'Прирост составляе - {growth}%')


# Определение наиболее прибыльной акции: Функция get_most_profitable_stock(stocks: dict, prices: dict) -> str 
# принимает два аргумента: stocks - словарь с акциями и их количеством. prices - словарь с акциями и их текущими ценами. 
# Функция должна вернуть символ акции (ключ), которая имеет наибольшую прибыль по сравнению с ее начальной стоимостью. 
# Начальная стоимость - первый вызов calculate_portfolio_value, данные из этого вызова следует сохранить в защищенную 
# переменную на уровне модуля.
# Пример:
# Пришло:
# stocks = {"AAPL": 10, "GOOGL": 5, "MSFT": 8}
# prices = {"AAPL": 155.25, "GOOGL": 2600.75, "MSFT": 800.50}
# Вышло:
# MSFT


def get_most_profitable_stock(stocks: dict, prices: dict) -> str:
    dict_result = {key: value * prices[key] for key, value in stocks.items()}
    max_valueable_equity = max(dict_result, key=dict_result.get)
    return max_valueable_equity


def each_equity_sum (stocks: dict, prices: dict) -> dict:
    result = {key: value * prices[key] for key, value in stocks.items()}
    return result


b = get_most_profitable_stock(initial_stocks, current_prices)
print(b)