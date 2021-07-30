
class Cakcakator:
    def __init__(self) -> None:
        self.result = 0
    
    def add(self,num):
        self.result += num
        return self.result

cal = Cakcakator()
Cal2 = Cakcakator()

print(cal.add(3))
print(cal.add(5))
print(Cal2.add(7))
print(Cal2.add(10))

print('*'*50)

class FourCal:
    def setdata(self, first, second) -> None:
        self.first = first
        self.second = second

    def add(self):
        return self.first + self.second

    def mul(self):
        return self.first * self.second

a = FourCal()
b = FourCal()
 

a.setdata(3,5)
print(a.add())
print(a.mul())
b.setdata(10,39)
print(b.add(), b.mul())
