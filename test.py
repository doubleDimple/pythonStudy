numbers = [1, 2, 3, 4, 5]
sequres = [x ** 2 for x in numbers]
print(sequres)

add = lambda x, y: x + y
result = add(3, 5)
print(result)


# 面向对象编程
class Animal:
    def __int__(self,name,age):
        self.name = name
        self.age = age

    # 定义一个方法
    def make_sund(self):
        pass


class Dog(Animal):
    def make_sund(self):
        print("汪汪汪! ")


dog = Dog()
