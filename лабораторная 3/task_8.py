money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05
month = 0
balance = money_capital + salary - spend  # Остаток денег в конце первого месяца
while balance >= 0:  # цикл, пока баланс не станет отрицательным
    spend = spend + (spend * increase)  # траты в месяц с учетом инфляции
    balance = balance + salary - spend  # баланс на остаток месяца
    month += 1
print(month)
