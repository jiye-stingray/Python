## 1. 입력한 숫자 n번만큼 *를 출력하는 함수를 작성하시오
# 함수명 starprint(n)

def starprint(n):
    print('*'*n)
#starprint(int(input('숫자를 입력하세요')))

## 2. 두수를 입력받아 합, 차, 곱을 저장하여 리스트로 출력하시오.
# 함수명 operator(a,b)

def operator(a,b):
    hap = a + b
    ch =  a - b
    gop = a * b
    return [hap,ch,gop]
# a =int(input('수를 입력하세요'))
# b =int(input('수를 입력하세요'))
# print(operator(a,b))


## 3. 문장을 입력받아서 각 알파벳을 대문자로 바꾸어 출력하는 함수작성.
# 함수명: wordlist(string)def wordlist (string):
def wordlist (string):
    return string.upper().split(' ')
#print(wordlist(input('문자를 입력(영어)')))
    
## 4. 두 자연수를 입력받아 최대공약수를 리턴하는 함수, 최소공배수를 리턴하는 함수를 완성하시오.
# 함수명: 최대공약수 gcd(n,m), 최소공배수 lcm(n,m)
# def gcn(n,m):
#     def lcm(n,m):
#         return int(n/m)
#     c = n * m
#     if n < m:
#         t = m
#         m = n
#         n = t
#     temp = n%m
#     while temp != 0:
#         n = m
#         m = temp 
#         temp = n%m
#     g = m
#     l = lcm(c, g)
#     return g, l
# n = int(input('수 입력: '))
# m = int(input('수 입력: '))
# print(gcn(n,m))

def gcn(n,m):
    i = 2
    j = max(n,m)
    while i >= j:
        if m%i == 0 and n%i == 0:
            break
    return i

def lcd(n,m):
    i = max(n,m)
    while True:
        if i % n == 0 and i % m == 0:
            break
        i += 1
    return i

# n = int(input('입력'))
# m = int(input('입력'))
# print(gcn(n,m))
# print(lcd(n,m))

## 5 아래의 조건을 만족하면서, 100000보다 작은 자연수 중
# 3의 배수 또는 5의 배수를 모두 더한 합을 출력하는 프로그램을 작성하시오.
# 조건: 3의배수를 판정하는 함수-ismulThree(n), 
#       5의 배수를 판정하는 함수 - ismulfive(n),
#       전체코드는 15줄 내에서 완성하기

def ismulThree(n):
    return not bool(n%3)
def ismulfive(n):
    return not bool(n%5)
hap = 0
for c in range(1,100000):
    if ismulThree(c) == True or ismulfive(c) == True:
        hap += c
print(hap)