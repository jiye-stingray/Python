v_str1 = "GoodGirl"
v_bool = True
v_float = 10.01
v_int = 6
v_str2 = "Niceboy"
v_list = [v_str1, v_str2]
v_dict = {"name":"KMK","age":30}

print(v_dict)
print(v_list)
print(type(v_int))
print(type(v_float))
print(type(v_bool))
print(type(v_str1))

a = 5.
b = 4
c = .4
d = 7.7
print(type(a),type(b),type(c),type(d))

print(a)
print(int(a))
print(b)
print(float(b))
print(complex(3))
print(int(True))

import math

print(math.ceil(5.1))
print(math.ceil(8.9999))

print(math.floor(3.87))
print(math.floor(-25.5))

print(math.pi)

str1 = "I am a girl"
str2 = 'Good girl'
str3 = """How are You?"""
str4 = '''Thank you'''

print(type(str1))

print(len(str1))
print(len(str2))
print(len(str3))
print(len(str4))

str_t1 = ''
print(type(str_t1),len(str_t1))

escape_str1 = "Do you have a \"big collection\"?"
escape_str2 = 'what\'s on TV?'
escape_str3 = "what's on TV?"
escape_str4 = 'This is "Book".'

print(escape_str1)
print(escape_str2)
print(escape_str3)
print(escape_str4)

str_o1 = "goodgirl"
str_o2 = "Orange"
str_o3 = "This is string example....wow!!! this is really string"
str_04 = "Kim Lee Park Joo"

print(str_o1 * 3)
print(str_o1 + str_o2)
print('x' not in str_o1)
print('g' not in str_o1)

print("Capitalize: ",str_o1.capitalize())
print("Join str:",str_o1.join(["i'm ","!"]))
print("replace1:",str_o1.replace('good','Nice'))
print("replace2: ",str_o3.replace('is','was',3))

print("split: ", str_04.split(' '))
print("sorted:", sorted(str_o1))
print("reversed1: ",list(reversed(str_o2)))

str_sl = 'Nicegirl'

print(str_sl[0:3])
print(str_sl[:len(str_sl)])
print(str_sl[:len(str_sl)-1])
print(str_sl[:])
print(str_sl[1:4:2])
print(str_sl[::3])
print(str_sl[::-1])

print("UPPER:",str_sl.upper())
print("UPPER:",str_sl.lower())