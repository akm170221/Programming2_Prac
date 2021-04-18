

sales = float(input("Enter sales: $"))
if sales>=0 and sales < 1000:
    low_bonus = sales * 0.1
    print("The bonus is {:.2f} ".format(low_bonus))
elif sales>= 1000:
    high_bonus = sales * 0.15
    print("The bonus is {:.2f} ".format(high_bonus))
else:
    print("Error")