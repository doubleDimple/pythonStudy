#条件语句：在 Python 中，条件语句使用 if、elif 和 else 关键字来实现。
x = 10
y = 5
if x > y:
    print("x 大于 y")
elif x < y:
    print("x 小于 y")
else:
    print("x 等于 y")

#循环语句：Python 中有两种循环语句，分别是 for 循环和 while 循环。


fruits = ["apple","banana","cherry"]
#for 循环：
for fruit in fruits:
    print(fruit)

#while 循环：
i = 0
while i < 5:
    print(i)
    i +=1
#函数：在 Python 中，函数使用 def 关键字定义。

def add(x,y):
    return x+y

result = add(3,5)
print(result)


