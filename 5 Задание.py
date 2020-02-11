my_list = [7, 5, 3, 3, 2]
a = int(input('Введите целое положительное число'))
n = 0
m = len(my_list)
while n <= m:
    if a > my_list[n]:
        my_list.insert(0, a)
        break
    elif a == my_list[n]:
        my_list.insert((n+1), a)
        break
    elif a < my_list[n]:
        n = n + 1
        continue
print(my_list)