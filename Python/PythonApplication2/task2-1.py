a=int(input('Введите число\n'))
b=int(input('Введите число\n'))
if a<b:
    arr=list(range(a,b+1))
    for i in arr:
        print(i,end=' ')
else:
    arr=list(range(b,a+1))
    arr.reverse()
    for i in arr:
        print(i,end=' ')