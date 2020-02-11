my_list = input('Введите слова ').split()
n = 1
for el in my_list:
    print(f'{n} {el[0:10]}')
    n = n + 1