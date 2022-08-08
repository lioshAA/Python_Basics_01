import math

#1
H1 = 3.5
L1 = 50

H2 = 4
L2 = 60

q = 3
l = 2
h = 0.25

#1.1
Q1 = math.ceil((H1 * L1) / (h * q * l))
print('House1 needs', Q1, 'trees')

#1.2
Q2 = math.ceil((H2 * L2) / (h * q * l))
print('House1 needs', Q2, 'trees')


#2
x = 1467 // 6
print('Answer for second exersice',  x)