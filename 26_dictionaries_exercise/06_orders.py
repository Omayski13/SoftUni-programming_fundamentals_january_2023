line = input()
product_quantities = {}
product_prices = {}
while line != "buy":
    product, price, quantity = line.split()
    price = float(price)
    quantity = int(quantity)
    if product not in product_quantities:
        product_quantities[product] = quantity
    else:
        product_quantities[product] += quantity
    product_prices[product] = price

    line = input()

for product in product_prices:
    price = product_prices[product]
    quantity = product_quantities[product]
    total_price = price * quantity
    print(f"{product} -> {total_price:.2f}")


