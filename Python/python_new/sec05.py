# print(type(True))
# print(type(False))

# if True:
#     print("Yes")
# if False:
#     print("No")

# if False:
#     print("You can't reach here")
# else:
#     print("Oh, you are here")


# #관계 연산자
# a = 10
# b = 0

# print(a==b)
# print(a!=b)
# print(a>b)
# print(a>=b)
# print(a<b)
# print(a<=b)

# #참, 거짓
# # 참: "내용",[내용],(내용),{내용}
# # 거짓: "", [], {}, ()
# city = ""
# if city:
#     print("You are in: ", city)
# else:
#     print("Please enter your city")

# city = "Gwangju"
# if city:
#     print("You are in: ", city)
# else:
#     print("Please enter your city")

# a = 100
# b = 60
# c = 15

# print('and:',a>b and b>c)
# print('or:',a>b or b>c)
# print('not:', not a>b)
# print('not:', not b>c)
# print(not True)
# print(not False)


# print('ex1:',3 + 12 > 7 + 3)
# print('ex2:',5 + 10 * 3 > 7 + 3 * 20)
# print('ex3:', 5 + 10 > 3 and 7 + 3 == 10)
# print('ex4:',5 + 10 > 0 and not 7 + 3 == 10)


score1 = 90
score2 = 'A'
if score1 >= 90 and score2 == 'A':
    print("합격하셨습니다")
else:
    print("불합격하셨습니다")

id = 'gold'
id2 = 'admin'
grade = 'super'

if id == 'gold' or id2 == 'admin':
    print('관리자 로그인 성공')
if id2 == 'admin' and grade == 'super':
    print('최고 관리자 로그인 성공')

is_work = False

if not is_work:
    print("is work!")

num = 90

if num >= 70:
    print('A학점 입니다')
elif num >= 80:
    print('B학점')
else:
    print('C')

age = 27
height = 165
if age >= 20:
    if height >= 170:
        print('A지망 지원가능')
    elif height >= 160:
        print('B지망 지원가능')
    else:
        print('지원 불가')
else:
    print('20세 이상 지원가능')

# in, not in

q = [1,2,3]
w = {7,8,9,9}
e = {'name':'Kim','city':'Gwangju','grade':'B'}
r =(10,12,14)

print(1 in q)
print(6 in w)
print(12 not in r)
print("name" in e)
print('Gwangju' in e.values())

#반복문
# for, while

v1 = 1

while  v1 < 11:
    print('v1:',v1)
    v1+=1

for i in range(10):
    print('i is:',i)

for i in range(1,11,2):
    print('i is:',i)

s = 0
for i in range(1,101):
    s += i
print(s)
print('1~100까지의 합:',sum(range(1,101)))
print('1~100까지의 3의 배수의 합:',sum(range(1,101,3)))


# a = int(input('enter 1st number:'))
# b = int(input('enter 1st number:'))
# print('두수의 합', a+b)

#입력받은 수가 소수인지 판별    
# num = int(input('enter the number:'))
# if num == 1:
#     print('1은 소수가 아닙니다')
# for i in range(1, num):
#     if num % i == 0 and i != 1:
#         print('소수가 아닙니다')
#     if i == num -1:
#         print(num,'은 소수')


names = ['Kim', 'Park', 'Cho', 'Lee', 'Choi', 'Yoo']
for name in names:
    print("U are ",name)

lotto_numbers = [11,25,43,28,36,37]
for number in lotto_numbers:
    print("Your number",number)


word = 'Dreams'
for s in word:
    print('word:',s)

my_info = {'name': 'Kim', 'age': 30, 'city': 'Gwangju'}
for key in my_info:
    print(key,':', my_info[key])

for val in my_info.values():
    print(val)

name = 'Judy'
for n in name:
    if n.isupper():
        print(n, end='')
    else:
        print(n.upper(), end = '')

print()
numbers = [14,3,4,7,10,24,17,2,33,15,34,36,38]
for num in numbers:
    if num == 33:
        print('찾았다:',num) 
        break
    else:
        print("not found!:",num)

lt = ["1", 2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is float:
        print('type:',type(v))

f = True
numbers = [14,3,4,7,10,24,17,2,33,15,34,36,38]
while f:
    for v in numbers:
        if v == 33:
            print('Found:',v)
            f = False