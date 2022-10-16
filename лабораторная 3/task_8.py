money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05
month = 0
grow = 1.05
balance = salary - spend
while money_capital + balance >= spend:
    money_capital += balance
    spend = spend * grow

    month += 1
print(month)
