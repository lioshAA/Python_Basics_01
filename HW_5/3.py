#lis = [1, 34, 8, 0, -5, 7, 32, 74, 59, 92, 41, 10, -2]
# Знайдіть найменший елемент списку та видаліть його. Після цього якщо число було менше 0,
# то помістіть його в кінець списку, інакше на початок списку.

lis1 = [1, 34, 8, 0, -5, 7, 32, 74, 59, 92, 41, 10, -2]
print('Our list:', lis1)

lis2 = lis1
lis2.sort()
print('Sorted list:', lis2)
if lis2[0] < 0:
    lis1.append(lis1[0])
    lis1.remove(lis1[0])
    print('Our list Updated:', lis1)
else:
    lis1.insert(0, lis2[0])
    lis1.remove(lis1[0])
    print('Our list Updated:', lis1)