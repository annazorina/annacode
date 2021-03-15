s=input('Введите словосочетание\n')
index=s.find(' ')
print(s[index+1:]+' '+s[:index+1])

