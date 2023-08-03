number_of_cities = int(input())
total_income = 0
total_expenses = 0

for day in range(1, number_of_cities + 1):
    city_name = input()
    current_city_income = float(input())
    current_city_expenses = float(input())
    if day % 3 == 0:
        if day % 5 == 0:
            pass
        else:
            current_city_expenses *= 1.5
    if day % 5 == 0:
        current_city_income *= 0.9

    current_city_profit = current_city_income - current_city_expenses
    total_income += current_city_profit
    print(f"In {city_name} Burger Bus earned {current_city_profit:.2f} leva.")


print(f"Burger Bus total profit: {total_income:.2f} leva.")


