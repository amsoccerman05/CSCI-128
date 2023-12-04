import random

seed = input("SEED> ")
random.seed(seed)

months = int(input("MONTHS> "))
monthly_interest_rate = float(input("INTEREST> "))
method = int(input("METHOD> "))

initial_investment = 2000

# Function to simulate savings account
def simulate_savings_account(initial_investment, monthly_interest_rate, num_months):
    ending_balance = initial_investment
    for _ in range(num_months):
        ending_balance *= (1 + monthly_interest_rate)  # Compounding interest
    return ending_balance

# Function to simulate index fund investment
def simulate_index_fund(initial_investment, num_months):
    ending_balance = initial_investment
    for _ in range(num_months):
        probability = random.random()
        if probability <= 0.7:
            pass  # Account stays the same
        elif 0.7 < probability <= 0.9:
            ending_balance *= (1 + 0.01)  # Increase by 1%
        else:
            ending_balance *= (1 - 0.03)  # Decrease by 3%
            ending_balance = max(0, ending_balance)  # Ensure balance doesn't go negative
    return ending_balance

# Function to simulate roulette
def simulate_roulette(initial_investment, num_months):
    ending_balance = initial_investment
    for _ in range(num_months):
        winning_number = random.randint(0, 36)
        if winning_number == 15:
            ending_balance += 2000 * 35  # Winning amount
        else:
            ending_balance -= 2000  # Betting amount for each month
            ending_balance = max(0, ending_balance)  # Ensure balance doesn't go negative
    return ending_balance

# Function to simulate investment based on the chosen method
def simulate_investment(initial_investment, monthly_interest_rate, num_months, method):
    if method == 1:
        ending_balance = simulate_savings_account(initial_investment, monthly_interest_rate, num_months)
    elif method == 2:
        ending_balance = simulate_index_fund(initial_investment, num_months)
    elif method == 3:
        ending_balance = simulate_roulette(initial_investment, num_months)
    return round(ending_balance, 2)

ending_balance = simulate_investment(initial_investment, monthly_interest_rate, months, method)
print(f"OUTPUT {ending_balance:.2f}")
