"""
#Single Level:
class A:
    def add(this):
        print("Addition")
class B(A):
    def sub(this):
        print("Subtraction")
b=B()
b.add()

#multilevel
class A:
    def add(this):
        print("Addition")
class B(A):
    def sub(this):
        print("Subtraction")
class C(B):
    def add(this):
        print("Multiplication")
c=C()
c.add()

#Multiple
class A:
    def add(this):
        print("Addition")
class B:
    def sub(this):
        print("Subtraction")
class C(A,B):
    def mul(this):
        print("Multiplication")
a=A()
a.add()
b=B()
b.sub()
c=C()
c.add()

#Hiereachial
class A:
    def add(this):
        print("Addition")
class B(A):
    def sub(this):
        print("Subtraction")
class C(A):
    def mul(this):
        print("Multiplication")
a=A
a.add()
b=B()
b.sub()
c=C()
c.add()

#Hybrid
class A:
    def add(this):
        print("Addition")
class B(A):
    def sub(this):
        print("Subtraction")
class C(A):
    def mul(this):
        print("Multiplication")
class D(B,C):
    def div(this):
        print("division")
"""
