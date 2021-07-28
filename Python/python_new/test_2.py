# Section05-3
# 파이썬 흐름제어(제어문)
# 제어문 관련 퀴즈(정답은 영상)

# 1 ~ 5 문제 if 구문 사용
# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
q1 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}
for a in q1:
    if a == '가을':
        print(q1[a])
        
        

# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.
q2 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}
b = False
for a in q1:
    if q1[a] == '사과':
        print("포함됨") 
        b = True
    if a == '사과':
        print('포함됨')
if b == False:
    print('안 포함')

# 3. 다음 점수 구간에 맞게 학점을 출력하세요.
# 81 ~ 100 : A학점
# 61 ~ 80 :  B학점
# 41 ~ 60 :  C학점
# 21 ~ 40 :  D학점
#  0 ~ 20 :  E학점

# score = int(input('점수를 입력하세요:'))
# if score == 100 and score > 80:
#     print('A')
# elif score <= 80 and score > 60:
#     print('B')
# elif score <= 60 and score > 40:
#     print('C')
# elif score <= 40 and score > 20:
#     print('D')
# else:
#     print('E')

# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18
a,b,c = 12,6,18
max = a
if max<b:
    max = b
    if max<c:
        max = c
print(max)


# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)

# num = list(input('주민등록 번호를 입력하세요'))
# num = int(num[7])
# if  num == 1 or num == 3:
#     print('남자')
# elif num == 2 or num == 4:
#     print('여자')

number = '000000-2333333'
if int(number[7])%2 == 0:
    print('여자')
else:
    print('남자')


# 6 ~ 10 반복문 사용(while 또는 for)

# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
q3 = ["갑", "을", "병", "정"]
for a in q3:
    if a == "병": 
        continue
    print(a)


# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.
for num in range(1, 101):
    if num%2 != 0:
        print(num, end=' ')


# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q4 = ["nice", "study", "python", "anaconda", "!"]
for i in q4:
    if len(i) >= 5:
        print(i)

print([s for s in q4 if len(s) >= 5])

# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]
for i in q5:
    if not i.isupper():
        print(i)

print([s for s in q5 if s.islower()])

# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
print()
q6 = ["A", "b", "c", "D", "e", "F", "G", "h"]
for i in q6:
    if i.isupper():
        print(i.lower())
    else:
        print(i.upper())

