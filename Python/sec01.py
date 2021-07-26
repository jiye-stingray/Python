print('hello Python!!')
print("Hello Python")
print()

print('T','E','S','T',sep = '')
print('2021','7','26',sep='-') 
print('stingray','naver.com', sep='@')
print()

print('Welcome to',end=' ')
print('Python World', end=' ')
print('soft school')
print()

#format사용
print('{} and {}'.format('You','Me'))
print('{0} and {1} and {0}'.format('You','Me'))
print('{a} are {b}'.format(a='You',b='happy'))
print()

print("'you'")
print('"you"')
print('\'you\'')
print('\n\n\n test')

#%d: 정수
print("%s's favorite number is %d" %('KMK', 3) )
print("Test1: %5d, price: %4.2f" %(789, 1234.5678))
print("Test1: {0:5d}, price: {1:4.2f}".format(789,1234.5678))
print("Test1: {a: 5d}, price:{b: 4.2f}".format(a=789,b=1234.5678))