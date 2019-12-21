# while loop适用于不知道循环几次

# 2 dimensional

# read file
products = []
with open('products.csv','r') as f:
    for line in f:
        if 'product,price' in line:
            continue # 跳到下一回的意思，并没有逃出回圈
        name, price= line.strip().split(',')
        #把尾巴换行去掉; use , as the split标准，遇到，就切割
        # split切割完的结果是list
        products.append([name,price])
print(products)

# 让使用者输入
while True:
    name = input('Please enter product name:')
    if name == 'q':
        break
    price = input('Please enter product price:')
    products.append([name,price])
print(products)

# 印出所有购买记录
for p in products:
    print(p[0], ' price is' , p[1])

# write a file --> w
# read a file --> r
# save the file as 'f'
# 写入档案
with open('products.csv', 'w') as f:
    f.write('product, price\n')
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n')
# addition of four strings
