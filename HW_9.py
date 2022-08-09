#Дано словник, який містить «Прізвище»-«оцінка».
#На його основі створити новий словник, який буде містити лише учнів, які навчаються на 4 та 5.
#Повторити усі методи і функції над множинами, рядками і списками.



#d = {'Obukhov': 12}
d = dict(Shkarupa = 4, Obukhov = 4, Shkulip = 2, Bondarenko = 3, Shevchenko = 5)
d['Stepanenko'] = 1 #додавання елементу
print(d)
d['Stepanenko'] = 3 #зміна значення
print(d)
del d['Shkulip'] #видалення елемента
print(d)
print(d.keys())  #виведення ключів
print(d.values()) #виведення значень
print(d.items()) #виведення елементів
toprates = {} #довідник учнів з високими оцінками
for i in d:
    if d[i] >= 4:
        toprates[i] = d[i]
print(toprates)
