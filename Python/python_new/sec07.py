# 클래스
# 선언
# class 클래스 명: (클래스명 첫 글자: 대문자, ex)Stu, StuInfo
#       함수~~
# class UserInfo:
#     def __init__(self, name, hp, add):
#         self.name = name
#         print('Name:',self.name)
    
# user1 = UserInfo('Kim')
# user2 = UserInfo('Park')

# print(id(user1))
# print(id(user2))

# print('user1:',user1.__dict__)
# print('user2:',user2.__dict__)

class Student:
    name = 'student'
    age = 0
    def __init__(self,name, age) -> None:
        print('객체 초기화')
        self.name = name
        self.age = age
    def __del__(self):
        print('객체 삭제')
    def info(self):
        print('My name is', self.name)
        print('I am ',self.age,'years old' )

s = Student('JaeHyun',22)
s.info()
del s
print(type(s))

class Student1:
    def __init__(self, name, age) -> None:
        self.university = 'SNU'
        self.name = name
        self.age = age
        self.isStudying = True
        self.studyHour = 0

    def study(self):
        if self.isStudying:
            self.studyHour += 1
    
    def hourofstudy(self):
        print('{}현재 공부 시간: {}시간'.format(self.name, self.studyHour))