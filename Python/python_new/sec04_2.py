# 딕셔너리 (tnstj, 중복x, 수정, 삭제o)
# 선언
a = {'name' : 'Kim', 'phone': '01012345678', 'birth': '050827'}
b = {0:'Hello python!'}
c = {'arr':[1,2,3,4]}

print(type(a))

print(a['name'])
print(a.get('name'))
print(b[0])
print(c['arr'][2])

print(a.keys())
print(list(a.keys()))

print(a.values())
print(list(a.values()))

print(a.items())
print(list(a.items()))
print('===='*20)

print('name' in a)
print('addr' in a)

a['address'] = 'Gwangju'
print(a.items())
a['rank'] = [1,2,3]
print(a)


#set(집합)(순서, 중복 x)
a = set()
b = set([1,2,3,4])
c = set([1,4,5,6])
d = set([1,2,'banana','pine','apple'])
print(type(a), type(b), type(c),type(d))
t = tuple(b)
print(type(t),t)
print(t[0],t[1:3])

l = list(c)
print(type(l),l)
print(l[0],l[1:3])


#집합 자료형 활용
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

print(s1 & s2)
print(s1.intersection(s2))

print(s1 | s2)
print(s1.union(s2))

print(s1 - s2)
print(s1.difference(s2))

s1 = set([1,2,3,4])
s1.add(5)
print(s1)
s1.remove(2)
print(s1)