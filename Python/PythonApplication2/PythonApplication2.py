s=input('Введите строку\n')
x=len(s)-2
print(s[:x])

print(s[-3:])

print(s[::2])

num=input('Ведите число\n')
if len(num)==7:
   temp=num[::-1]
   temp1=temp[:3]+' '+temp[3:6]+' '+temp[6:]
   num=temp1[::-1]
   print (num)
if len(num)==6:
   temp=num[::-1]
   temp1=temp[:3]+' '+temp[3:]
   num=temp1[::-1]
   print (num)
if len(num)==5:
   temp=num[::-1]
   temp1=temp[:3]+' '+temp[3:]
   num=temp1[::-1]
   print (num)
