products = ['Mac10', 'Mac9']
products_sold = list()
products_new = list()

print('Продукти в наявності:')
number = 1
for product in products:
    print(number, product)
    number +=1

print('Постачання продуктів')
print('Введіть назву продукту або 0 для виходу')
while True:
    product = input()
    if product == '0':
        break
    else:
        products_new.append(product)
products.extend(products_new)

print('Продукти в наявності:')
number = 1
for product in products:
    print(number, product)
    number +=1


print('Продаж продуктів за назвою:')
print('Введіть назву продукту, який бажаєте купити')
product = input()
if product in products:
    products.remove(product)
    products_sold.append(product)
    print('Дякуємо за покупку')
else:
    print('Вказаного продукту немає в наявності')


print('Продаж продуктів за номером:')
print('Введіть номер продукту, який бажаєте купити')
product_index = int(input())
if 0 <= product_index < len(products):
    product = products.pop(product_index-1)
    products_sold.append(product)
    print('Ви купили', product)
    print('Дякуємо за покупку')
else:
    print('Неправильно вказаний номер')

print('Продукти продані за день:')
products_sold.reverse()

for product in products_sold:
    print(product)
print('Надходження продуктів за день:')
for product in products_new:
    print(product)


