annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(
    input("Enter percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter cost of your dream home: "))
portion_down_payment = float(0.25 * total_cost)
current_savings = 0
r = 0.04
interest = float(current_savings * r)
months = 0

# calculate how many months it will take to save down payment

while current_savings < portion_down_payment:
    current_savings += interest + (float(portion_saved) * (annual_salary / 12))
    interest = float(current_savings * r)
    months += 1
    # print(current_savings)

    if current_savings >= portion_down_payment:
        print("Number of months to reach your dream: " + str(months))
