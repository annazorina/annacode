n=int(input('Введите колличество игр\n'))
win_1=0
win_2=0
for i in range(n):
   s=input('Введите счет игры в формате 3:2 \n').split(':')
   if int(s[0])>int(s[1]):
     win_1+=1
   elif int(s[0])<int(s[1]):
     win_2+=1
print(win_1, ':', win_2, sep='')
