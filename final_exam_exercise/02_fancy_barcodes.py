import re

num_of_line = int(input())
pattern = r"@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@#+"

for n in range(num_of_line):
    text = input()
    result = re.findall(pattern, text)
    if result:
        result = str(result)
        product_group = re.findall(r"\d", result)
        if product_group:
            print(f'Product group: {"".join(product_group)}')
        else:
            print("Product group: 00")
    else:
        print("Invalid barcode")
