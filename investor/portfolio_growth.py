def calculate_portfolio_return(initial_value: float, current_value: float) -> float:
    result = ((current_value-initial_value)/initial_value)*100
    return result
