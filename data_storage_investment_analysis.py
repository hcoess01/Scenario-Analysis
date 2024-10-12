# Define the input variables
initial_investment = 100_000  # Initial investment cost in dollars
annual_maintenance = 10_000    # Annual maintenance cost in dollars
expected_lifespan = 5          # Expected lifespan in years

# Define the benefits
efficiency_savings_per_year = 500 * 30  # 500 hours saved per year at $30/hour
downtime_savings_per_year = 8 * 12 * 30  # 8 hours saved per month at $30/hour
scalability_savings = 20_000              # Estimated savings from scalability
security_savings = 50_000                  # Estimated savings from improved security

# Calculate total costs over the lifespan
total_costs = initial_investment + (annual_maintenance * expected_lifespan)

# Calculate total benefits over the lifespan
total_efficiency_savings = efficiency_savings_per_year * expected_lifespan
total_downtime_savings = downtime_savings_per_year * expected_lifespan
total_benefits = (
    total_efficiency_savings +
    total_downtime_savings +
    scalability_savings +
    security_savings
)

# Calculate net benefit
net_benefit = total_benefits - total_costs

# Display the results
print("Cost-Benefit Analysis for Data Storage Investment:")
print("-" * 50)
print(f"Initial Investment: ${initial_investment:,}")
print(f"Annual Maintenance Cost: ${annual_maintenance:,}")
print(f"Expected Lifespan: {expected_lifespan} years")
print("-" * 50)
print(f"Total Costs Over {expected_lifespan} Years: ${total_costs:,}")
print(f"Total Benefits Over {expected_lifespan} Years: ${total_benefits:,}")
print(f"Net Benefit: ${net_benefit:,}")

# Conclusion based on the results
if net_benefit > 0:
    print("\nConclusion: The investment is financially justifiable with a net benefit of ${:,}.".format(net_benefit))
else:
    print("\nConclusion: The investment is not financially justifiable, resulting in a net loss of ${:,}.".format(abs(net_benefit)))
