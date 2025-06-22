def cournot_duopoly(a=100, b=1, c=20):
    # Best response functions for symmetric firms:
    # q_i = (a - c - q_j) / 2
    
    # In Cournot-Nash equilibrium with symmetric costs:
    # q_A = q_B = (a - c) / (3b)
    q_star = (a - c) / (3 * b)
    Q_total = 2 * q_star
    P = a - b * Q_total
    profit = (P - c) * q_star

    print("Cournot-Nash Equilibrium Results:")
    print(f"Firm A Quantity: {q_star:.2f}")
    print(f"Firm B Quantity: {q_star:.2f}")
    print(f"Total Quantity (Q): {Q_total:.2f}")
    print(f"Market Price (P): {P:.2f}")
    print(f"Firm A Profit: {profit:.2f}")
    print(f"Firm B Profit: {profit:.2f}")

# Run the model with default values
cournot_duopoly()


# Output

Cournot-Nash Equilibrium Results:
Firm A Quantity: 26.67
Firm B Quantity: 26.67
Total Quantity (Q): 53.33
Market Price (P): 46.67
Firm A Profit: 711.11
Firm B Profit: 711.11
