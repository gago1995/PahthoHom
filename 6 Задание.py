my_list = []
n = 0
nambar = 0
while True:
    my_list.insert(n, (tuple(input('Введите номер')),
                       {'Название': input('Введите название'),
                        'Цена': input('Введите цену'),
                        'Количество': input('Введите количество'),
                        'Ед': input('Введите единицы')}))
    n = n + 1
    a = input('Если хотите закончить ввод данных введите N')
    if a == 'N': break
    else: continue
Name = []
price = []
quantity = []
unit = []
m = 0
for el in my_list:
    price.insert(m,el[1].get('Цена'))
    Name.insert(m,el[1].get('Название'))
    quantity.insert(m, el[1].get('Количество'))
    unit.insert(m, el[1].get('Ед'))
    m = m + 1
print('\n','Название: ', Name,'\n',
      'Цена: ', price, '\n',
      'Количество: ', quantity, '\n',
      'Ед: ', unit)



