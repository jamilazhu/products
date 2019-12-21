# while loop适用于不知道循环几次

# 2 dimensional 
products = []
while True:
    name = input('Please enter product name:')
    if name == 'q':
        break
    price = input('Please enter product price:')
    p = []
    p.append(name)
    p.append(price) 
    products.append(p)
print(products)

products[0][0]
