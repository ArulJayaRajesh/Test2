"""
class Arith():
    __pi = 3.14
    def __add(self):
        print("Addition")
    def sub(self):
        print("Subtraction")
    def test(self):
        self.__add()
        area =self.__pi*2*2
        print(area)
class project(Arith):
    def mul():
        print("Multiplication")
a=Arith()
a.test()
"""
# Polimorphism
class Arith:
    def add(self,a):
        total=0
        for x in a:
            total=total+x
        print(total)
#a=int(input("Enter First Value:"))
#b=int(input("Enter Second  Value:"))
#z=int(input("Enter third Value:"))
obj=Arith()
a=[1,2,3,4,5,6,7,8,9,10]
obj.add(a)
