n = int(input('Введите число от 1 до 9\n'))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, sep='', end='')
    print()
#второйй вариант решения
s=''
for i in range(1, n + 1):
    s+=str(i)
    print()