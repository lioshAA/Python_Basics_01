words = ['купити', 'продати', 'реклама']

text = input("Введіть Ваше повідомлення:")
print(text)

for i in words:
    if text.find(i) != -1:
        print('SPAM')
        break
