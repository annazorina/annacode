s=input().split(',')#пользователь вводит числа через запятую
for i in range(len(s)):
    s[i]=int(s[i])
    print(s.count(0))#считаем количество нулей