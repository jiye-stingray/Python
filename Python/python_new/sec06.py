# 함수
# def function_name():

def hello_retrun(world):   
    val = "Hello, "+str(world)
    return val

str = hello_retrun('jyp')
print(str)
    
#다중 리턴

def func_mull(x):
    y1 = x * 10
    y2 = x * 100
    y3 = x * 1000

    return y1,y2,y3
val1 , val2, val3 = func_mull(5)
print(type(val1),val2,val3)

def func_mull(x):
    y1 = x * 10
    y2 = x * 100
    y3 = x * 1000

    return [y1,y2,y3]
lt= func_mull(5)
print(type(lt),lt)

def func_mull(x):
    y1 = x * 10
    y2 = x * 100
    y3 = x * 1000

    return (y1,y2,y3)
tupe= func_mull(5)
print(type(tupe),tupe)


def func_mull(x):
    y1 = x * 10
    y2 = x * 100
    y3 = x * 1000

    return {'ret1':y1,'ret2':y2,'ret3':y3}
dic= func_mull(5)
print(type(dic),dic.items())

def args_func(*args):
    for i, v in enumerate(args):
        print(i, v)
args_func('kim','park','lee')

def kwargs_func(**kwargs):
    print(kwargs)

kwargs_func(name1 = 'Kim', name2 = 'park', name3 = 'Lee')

#혼합
def example(arg_1,arg_2,*args, **kwargs):
    print(arg_1,arg_2,args,kwargs)

example(10,20,'park','kim','lee',age = 33,age2 = 34,age3=20)

#중첩 함수
def nested_func(num:int)->int:
    def func_in_func(num):
        print('>>>',num)
    print("in func")
    func_in_func(num+100)

nested_func(20)

def wordlist (string):
    return string.upper()


print(wordlist('abc'))