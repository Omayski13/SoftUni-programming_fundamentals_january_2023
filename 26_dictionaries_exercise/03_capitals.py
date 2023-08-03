countries = input().split(", ")
capitals = input().split(", ")

# dictt = dict(zip(countries,capitals))

# for country,capital in dictt.items():
#     print(f"{country} -> {capital}")


capital_by_country = {f'{countries[index]} -> {capitals[index]}' for index in range(len(countries))}
print("\n".join(capital_by_country))




