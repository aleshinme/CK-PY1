salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен
money_capital = 0  # количество денег, чтобы прожить 10 месяцев

for cash in range(1, 11): # цикл из 10 итераций
    balance = -(salary - spend) #баланс на конец месяца (отрицательный, потому что расходы больше доходов)
    spend = spend + (spend * increase)  #траты с учетом месячной инфляции
    money_capital += balance  #необходимая финансовая подушка
print(round(money_capital))
