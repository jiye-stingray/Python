# import this 
import sys

print(sys.stdin.encoding)
print(sys.stdout.encoding)

print(" My Name is KMK")

myname = 'KMK'

if myname == 'KMK':
    print("Hello")

for i in range(1, 10):
    for j in range(1,10):
        print('%d * %d = '%(i,j), i*j)


이름 = "김미경"
print(이름)

def 인사():
    print("안녕하세요?! 반갑습니다.")

인사()

class Cookie:
    pass

cookie = Cookie()

print(id(cookie))
print(dir(cookie))
