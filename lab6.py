
def calculate_income_tax(salary):
    # Define tax threshold
    if salary < 11850:
        return 0  # No tax for salaries below the personal allowance
    elif salary <= 34500:
        return (salary - 11850) * 0.2  # Basic rate (20%) for income above personal allowance
    elif salary <= 150000:
        return 4530 + ((salary - 34500) * 0.4)  # Higher rate (40%) for income above basic threshold
    else:
        return 50370 + ((salary - 150000) * 0.45)  # Additional rate (45%) for income above upper threshold


# Example salary
salary = 100000
tax_amount = calculate_income_tax(salary)

# Output formatted result
print(f"Tax amount for salary £{salary} is £{tax_amount:.2f}")
