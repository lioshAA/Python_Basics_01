#Дано строку, яка містить довільне речення, слова в якому розділені пробілами.
#З використанням зрізів знайти і вивести слово, як має найбільшу довжину


#1 спосіб
#a = 'I have a phone'
#x = a.split(' ')
#print(max(x, key=len))



#2 спосіб
a = 'I have a phone'
a = a.split(' ')
print(a)
maxword = ''
for i in a:
    if len(maxword) < len(i):
        maxword=i
print(maxword)



