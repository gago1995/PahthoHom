Nam_Montsh = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
season = ['Зима', 'Весна', 'Лето', 'Осень']
Montsh = int(input('Введите номер месаца '))
if 0 < Montsh <= 12:
    if 0 <= Nam_Montsh.index(Montsh) <= 2:
        print(f' Время года: {season[0]}')
    elif 3 <= Nam_Montsh.index(Montsh) <= 5:
        print(f' Время года: {season[1]}')
    elif 6 <= Nam_Montsh.index(Montsh) <= 8:
        print(f' Время года: {season[2]}')
    elif 9 <= Nam_Montsh.index(Montsh) <= 11:
        print(f' Время года: {season[3]}')
else:
    print('Нет месяца с таким номером!')
