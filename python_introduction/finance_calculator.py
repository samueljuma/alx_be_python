def calculate_monthly_savings(income, expenses):
    return income - expenses


def calculate_annual_savings(monthly_savings):
    return monthly_savings * 12 + (monthly_savings * 12 * 0.05)


def main():
    monthly_income = float(input("Enter your monthly income: "))
    monthly_expenses = float(input("Enter your total monthly expenses: "))
    monthly_savings = calculate_monthly_savings(monthly_income, monthly_expenses)
    projected_annual_savings = calculate_annual_savings(monthly_savings)
    print(f"Your monthly savings are {round(monthly_savings)}.")
    print(
        f"Projected savings after one year, with interest, is: ${round(projected_annual_savings)}."
    )


if __name__ == "__main__":
    main()
