
def exchange_money(budget, exchange_rate):
    result = budget / exchange_rate
    return result



budget = float(input("Ingrese su presupuesto: "))
exchange_rate = float(input("Ingrese la tasa de cambio: "))


converted_money = exchange_money(budget, exchange_rate)


print("El dinero convertido es:", converted_money)