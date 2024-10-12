# Define the input variables
initial_investment = 1_000_000  # Initial investment in dollars
fixed_costs = 200_000           # Annual fixed costs in dollars
variable_cost_percent = 0.50    # Variable costs as a percentage of sales

# Define the sales projections for each scenario
optimistic_sales = 800_000  # Sales in booming economy
base_sales = 500_000        # Sales in average economy
pessimistic_sales = 300_000 # Sales in recession economy

# Define a function to calculate profit based on sales
def calculate_profit(sales):
    variable_costs = sales * variable_cost_percent
    profit = sales - variable_costs - fixed_costs
    return profit

# Calculate profits for each scenario
optimistic_profit = calculate_profit(optimistic_sales)
base_profit = calculate_profit(base_sales)
pessimistic_profit = calculate_profit(pessimistic_sales)

# Display the results
print("Scenario Analysis for New Product Line Launch:")
print("-" * 50)
print(f"Initial Investment: ${initial_investment:,}")
print(f"Fixed Costs: ${fixed_costs:,} per year")
print(f"Variable Costs: {variable_cost_percent * 100}% of sales")
print("-" * 50)
print(f"Optimistic Scenario (Booming Economy): Sales = ${optimistic_sales:,}, Profit = ${optimistic_profit:,}")
print(f"Base Scenario (Average Economy): Sales = ${base_sales:,}, Profit = ${base_profit:,}")
print(f"Pessimistic Scenario (Recession): Sales = ${pessimistic_sales:,}, Profit = ${pessimistic_profit:,}")

# Conclusion based on the results
def conclude_scenario(profit, scenario_name):
    if profit > 0:
        print(f"In the {scenario_name}, the company makes a profit of ${profit:,} per year.")
    else:
        print(f"In the {scenario_name}, the company incurs a loss of ${abs(profit):,} per year.")

# Generate conclusion for each scenario
print("\nConclusions:")
conclude_scenario(optimistic_profit, "Optimistic Scenario")
conclude_scenario(base_profit, "Base Scenario")
conclude_scenario(pessimistic_profit, "Pessimistic Scenario")
