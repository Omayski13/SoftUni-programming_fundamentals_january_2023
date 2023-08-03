command = input()
stock = {}
while command != 'statistics':
    product, product_stock = command.split(": ")
    product_stock = int(product_stock)
    if product not in stock:
        stock[product] = product_stock
    else:
        stock[product] += product_stock
    command = input()
print("Products in stock:")
for product, product_stock in stock.items():
    print(f"- {product}: {product_stock}")
print(f"Total Products: {len(stock.keys())}")
print(f"Total Quantity: {sum(stock.values())}")