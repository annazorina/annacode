n=int(input('Введите количество чисел\n'))
sum_value=0
for i in range(n):
    sum+=int(input('Введите число\n'))
print(sum_value)


s=input().split(',')#пользователь вводит числа через запятую
for i in range(len(s)):
    s[i]=int(s[i])
    print(sum(s))
