Income = int (input("Enter your monthly income: "))
total_monthly_expenses = int (input("Enter your total monthly expenses: "))
Monthly_Savings = Income - total_monthly_expenses
Projected_Savings = Monthly_Savings * 12 + ( Monthly_Savings * 12 * 0.05)
print ("Your monthly savings are $",Monthly_Savings)
print("Projected savings after one year, with interest, is: $",Projected_Savings)
