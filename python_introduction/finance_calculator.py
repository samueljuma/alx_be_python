monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses
projected_annual_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print(f"Your monthly savings are {round(monthly_savings)}.")
print(f"Projected savings after one year, with interest, is: ${round(projected_annual_savings)}.")