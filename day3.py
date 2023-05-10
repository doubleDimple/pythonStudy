#列表推导式：列表推导式是一种快速创建列表的方法。
numbers = [1,2,3,4,5]
squares = [x**2 for x in numbers]
print(squares)
#lambda 表达式：lambda 表达式是一种创建匿名函数的方法。
add = lambda x, y: x + y
result = add(3,5)
print(result)

#面向对象编程：Python 是一种面向对象的语言，支持类、对象、继承和多态等特性。
class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def make_sund(self):
        pass
class Dog(Animal):
    def make_sund(self):
        print("汪汪汪! ")

dog = Dog("小狗",3)
print(dog.name)
dog.make_sund()

#异常处理：在 Python 中，使用 try、except 和 finally 关键字来捕获和处理异常。
try:
    x = 1 / 0
except ZeroDivisionError:
    print("除数不能为0")
finally:
    print("无论如何都会执行的代码")
