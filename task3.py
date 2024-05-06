def calculate_investment(start, rate, years):
    amount = start * (1 + rate/100) ** years
    return amount

start = int(input("Введите начальную сумму: "))
rate = float(input("Введите процентную ставку (годовую): "))
years = int(input("Введите количество лет: "))

result = calculate_investment(start, rate, years)

print("По истечении", int(years), "лет с начальной суммой", int(start), "и процентной ставкой", float(rate), "% вы получите", float(result))