# while loop适用于不知道循环几次 # 2 dimensional

import os #operating system

# 读取档案
def read_file(filename):
    products = []
    with open(filename,'r') as f:
        for line in f:
            if 'product,price' in line:
                continue # 跳到下一回的意思，并没有逃出回圈
            name, price= line.strip().split(',')
                #把尾巴换行去掉; use , as the split标准，遇到，就切割
                #split切割完的结果是list
            products.append([name,price])
    return products 

# 让使用者输入
def user_input(products): 
    while True:
        name = input('Please enter product name:')
        if name == 'q':
            break
        price = input('Please enter product price:')
        # print = int(price)
        products.append([name,price])
    print(products)
    return products

# 印出所有购买记录
def print_products(products):
    for p in products:
        print(p[0], ' price is' , p[1])

# write a file --> w
# read a file --> r
# save the file as 'f'
# 写入档案
def write_file(filename, products):
    with open(filename, 'w') as f:
        f.write('product, price\n')
        for p in products:
            f.write(p[0] + ',' + p[1] + '\n')
# addition of four strings


# main(function) 程式的进入点
def main():
    filename = 'products.csv'
    if os.path.isfile(filename): #os.path.isfile()用来检查档案在不在
        print('yeah!found the file!')
        products = read_file(filename) #执行读档案这个function
    else:
        print('file not found....')

    #products = read_file('products.csv')
    products = user_input(products)
    print_products(products)
    write_file('products.csv', products)
    
main() #use this function
