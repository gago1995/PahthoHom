Nam = {1: 'Зима', 2:'Зима', 3: 'Весна', 4: 'Весна', 5: 'Весна',
              6: 'Лето', 7: 'Лето', 8: 'Лето', 9: 'Осень', 10: 'Осень', 11: 'Осень', 12: 'Зима'}
n = list(Nam.keys())
n.insert(0, 0)
Montsh: int = int(input('Введите номер месаца '))
if 0 < Montsh <= 12:
    for el in range(int(len(n))):
        if n [el] == Montsh:
            print(f'Время года: {Nam.get(el)}')
else:
    print('Нет месяца с таким номером!')