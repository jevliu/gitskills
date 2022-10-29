"""class A(object):
    a = 1

    def __init__(self,num):
        self.b = num

obj1 = A(123)
obj2 = A(555)

print(obj1.b)
print(obj1.a)

obj1.a = 22
obj1.b = 13

print(obj1.b)
print(obj1.a)

print(obj2.a)
print(obj2.b + A.a)
print(obj2.b + obj1.a)
"""

"""class A(object):
    @classmethod
    def f(cls):
        print(cls)

A.f()

obj = A()
obj.f()"""

"""def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)"""
"""x = 0
def outer():
    x = 1
    def inner():
        global x
        x = 2
        print("inner:", x,id(x))

    inner()
    print("outer:", x,id(x))

outer()
print("global:", x,id(x))
"""


# class Dog:
#     species = "Canis familiaris"
#
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age
#
#     # Instance method
#     def description(self):
#         return f"{self.name} is {self.__age} years old"
#
#     # Another instance method
#     def speak(self, sound):
#         return f"{self.name} says {sound}"
#
# qiuqiu = Dog('QIUQIU',5)
# print(qiuqiu.description())

class Student(object):

    # 将性别变量设置为外部不可直接访问的私有变量
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    # 定义访问性别的方法
    def get_gender(self):
        return self.__gender

    # 定义修改性别的方法
    def set_gender(self, gender):
        self.__gender = gender


new_student = Student('Mingling', 'male')
print(new_student.get_gender())

new_student.set_gender('female')
print(new_student.get_gender())