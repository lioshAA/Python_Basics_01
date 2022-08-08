#Створити список материків західної півкулі.
# Доповнити список материками зі східної півкулі.
# Відсортувати материки за алфавітом і вивести на екран
west = ['North America', 'South America', 'Antarctica']
print(" Материки Західної півкулі:")
number = 1
for materic in west:
    print(materic)
    number +=1

east = ['Eurasia', 'Africa', 'Australia']
print(" Усі Материки:")
materics = west
materics.extend(east)
number = 1
for materic in materics:
    print(materic)
    number += 1
materics.sort()
print('Усі материки в алфавітному порядку:', materics)